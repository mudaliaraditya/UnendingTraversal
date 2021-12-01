import pygame
import Constants 
import Variables as Variables
from Sprite import *
from Game import *
from Platform import *
import random
class Player(AnimatedSprite):
	def __init__(self,screen,x : int,y: int,Width : int,Height : int,*ImagePath ):
		super().__init__(screen,x,y,Width,Height,ImagePath)
		self.vel_y = 0
		self.Life = Constants.PlayerMaxHealth
		self.Power = 100
		self.PowerUpTime = 0
		self.PowerUpEnum = 0
		self.LifeEnchancer = 0
	
	def move(self):
		global score
		#print("score:",Variables.score)
		dx = 0
		dy = 0
		self.Life -= 10
		self.Life +=  self.LifeEnchancer
		if self.Life >= Constants.PlayerMaxHealth:
			self.Life = Constants.PlayerMaxHealth
		Variables.score += 0.5
		draw_text(self.Screen,'SCORE: ' + str(int(Variables.score)), Game.GetGameObj().font_small, Constants.WHITE, 0, 0)
		draw_text(self.Screen,'LIFE:', Game.GetGameObj().font_small, Constants.WHITE, 0, 45)
		pygame.draw.rect(self.Screen, Constants.WHITE, (50 ,50 , self.Life * Game.GetGameObj().Width/20000 , 10))
		if self.PowerUpTime == 0:
			self.Power+=30
		PowerColor=Constants.BLUE
		if self.Power >= 10000:
			PowerColor=Constants.GREEN
			self.Power = 10000
		if self.PowerUpTime > 0:
			self.PowerUpTime -= 5
		elif self.PowerUpTime <= 0:
			self.PowerUpTime = 0
			self.LifeEnchancer = 0
			self.PowerUpEnum = 0
			Variables.JUMP_HEIGHT = Constants.JUMP_HEIGHT
			Variables.SPEED = Constants.SPEED
		if self.PowerUpEnum & 2:
			#print("powerup")
			self.LifeEnchancer = random.randint(30,60)
			Variables.JUMP_HEIGHT = random.randint(10,25)
			Variables.SPEED = Constants.GAMESPEED * random.randint(4,7)
			#self.Width = 32
			#self.Height = 10
		pygame.draw.rect(self.Screen, PowerColor, (80 ,70 , self.Power * Game.GetGameObj().Width/20000 , 10))
		draw_text(self.Screen,'POWER:', Game.GetGameObj().font_small, Constants.WHITE, 0, 65)
		#Y Movement due to GRAVITY
		self.vel_y += Constants.GRAVITY
		dy += self.vel_y
		#Variables.JUMP_HEIGHT -= 0.001

		#X MoveMent by Keys
		key = pygame.key.get_pressed()
		if key[pygame.K_a]:
			dx += -Variables.SPEED
			self.SetFlipX()
		if key[pygame.K_d]:
			dx += Variables.SPEED
			self.ResetFlipX()
		if self.Power >= 10000:
			if key[pygame.K_s]:
				self.PowerUpEnum = 2
				self.Power = 0
				self.PowerUpTime = (1000)
		GameObj = Game.GetGameObj()
		ScreenHeight = GameObj.Height
		if self.rect.y  > ScreenHeight:
			GameObj.ChangeState("GameMenu")
			#	dy = 0
		#	self.vel_y = -Variables.JUMP_HEIGHT
		for x in GameObj.GameObjects:
			if type(x) == Platform:
				if x.CheckCollision(self):
					dy = 0
					x.bDissapear = True
					if True or self.vel_y > 0:
						self.vel_y = -Variables.JUMP_HEIGHT
						self.Life += 7
						pygame.mixer.Sound.play(GameObj.GameJumpSound)
						if self.PowerUpTime <= 0:
							self.Power += 30
		dy += self.vel_y

		#scroll check
		scroll = 0
		if self.rect.top <= Constants.scroll_thresh :
			if self.vel_y <= 0:
				scroll = -dy
				GameObj.SetScroll(scroll)
				for x in GameObj.GameObjects:
					if type(x) == Platform:
						x.MoveUp()
		if self.rect.x >= GameObj.Width:
			self.rect.x = 0
		if self.rect.x < 0:
			self.rect.x = GameObj.Width - self.Width
		if dy > 0:
			self.ResetFlipY()
		else:
			self.SetFlipY()
		self.rect.x += (dx)
		self.rect.y += (dy) + scroll
		if dy > 0:
			Variables.score -= 0.5
		elif dy > 0:
			self.Life += 0.3
		if self.Life <= 0:
			GameObj.ChangeState("GameMenu")
		return True

	def update(self):
		self.move()
		super().update()
