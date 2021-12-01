import pygame
import time
import random
import os

import Constants
import Variables as Variables
from Sprite import *
from Platform import *
from Player import *
from Game import *

pygame.mixer.init()


def EncryptInt(no : int) -> str:
	no = int(no)
	string = str(no)
	arr=""
	for x in string:
		a=int(x)
		a = chr(a+4)
		arr += (a)
	return arr


def DecryptInt(char : str) -> int:
	arr=""
	for x in char:
		a = ord(x)
		a = a-4
		arr += str(a)
	return int(arr)



class CustomGame(Game):
	def __init__(self,Width : int,Height : int,IconPath : str,Title : str,BackgroundColor=(0,0,0) ,BackgroundImgPath=""):
		super().__init__(Width,Height,IconPath,Title,BackgroundColor,BackgroundImgPath)
		self.scroll = 0
		self.CurrentState=""
		self.AllStates=["GameMenu","Game","HighScoreScreen"]
		self.font_small=pygame.font.Font('Roboto-Regular.ttf', 20)
		self.font_title=pygame.font.Font('Roboto-Regular.ttf', 40)

	def ChangeState(self,State):
		self.State = State
		self.GameInit()

	def GameLoop(self):
		global high_score
		GameObj = self
		Variables.clock.tick(Constants.FPS)
		if self.State == "GameMenu":
			a = Sprite(self.m_Screen,0,0,self.Width,self.Height,"Game.png")
			a.update()
			#print("HighScore:" + str(Variables.high_score))
			pygame.draw.rect(self.m_Screen, Constants.GREEN, (130 ,300 , self.Width/2 , self.Height/2))
			draw_text(self.m_Screen,'Unending Traversal' , Game.GetGameObj().font_title, Constants.PANEL, 100,self.Height/2 - 250)
			draw_text(self.m_Screen,'A,D to Move Left and Right' , Game.GetGameObj().font_small, Constants.WHITE, self.Width/2 - 150,self.Height/2 - 100)
			draw_text(self.m_Screen,'S to use PowerUp' , Game.GetGameObj().font_small, Constants.WHITE, self.Width/2 - 150,self.Height/2 - 80)
			draw_text(self.m_Screen,'Powerup Increases Health' , Game.GetGameObj().font_small, Constants.WHITE, self.Width/2 - 150,self.Height/2 - 60)
			draw_text(self.m_Screen,'but decreases Jump and Speed' , Game.GetGameObj().font_small, Constants.WHITE, self.Width/2 - 150,self.Height/2 - 40)
			draw_text(self.m_Screen,'PRESS SPACE TO START' , Game.GetGameObj().font_small, Constants.WHITE, self.Width/2 - 150,self.Height/2)
			draw_text(self.m_Screen,'PRESS ESC TO QUIT' , Game.GetGameObj().font_small, Constants.WHITE, self.Width/2-150,self.Height/2 +20)
			draw_text(self.m_Screen,'HIGHSCORE:' + str(Variables.high_score) , Game.GetGameObj().font_small,Constants.WHITE,self.Width/2-150,self.Height/2 + 100)
			draw_text(self.m_Screen,'LASTSCORE:' + str(int(Variables.score)) ,Game.GetGameObj().font_small,Constants.WHITE,self.Width/2-150,self.Height/2 + 120)

			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE]:
				self.ChangeState("Game")
			if key[pygame.K_ESCAPE]:
				self.Stop()
		global Time
		global PrevTime
		global Dt
		Constants.Time = time.time()
		Constants.Dt = Constants.Time - Constants.PrevTime
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				GameObj.End()
		GameObj.GameObjects.update()
		Constants.PrevTime = Constants.Time
		return

	def GameInit(self):
		GameObj = self

		try:
			if os.path.exists('score.txt'):
				with open('score.txt', 'r',encoding='ascii') as pk:
					score_var = str(pk.read())
					Variables.high_score = DecryptInt(score_var)
			if Variables.score > Variables.high_score:
				Variables.high_score = int(Variables.score)
				with open('score.txt', 'w',encoding="ascii") as pk:
					score_var=EncryptInt(int(Variables.high_score))
					pk.write(score_var)
		except Exception as e:
			print(e)

		GameObj.GameObjects.clear()
		self.GameJumpSound = pygame.mixer.Sound("mixkit-quick-jump-arcade-game-239.wav")
		global PrevTime
		if self.State == "Game":
			pygame.mixer.music.stop()
			pygame.mixer.music.load('TheWave.wav')
			pygame.mixer.music.play(loops=-1)
			Variables.score = 0
			PlayerW = Player(GameObj.m_Screen,GameObj.Width/2,GameObj.Height/2,32,32,"BlueFlame1.png","BlueFlame2.png","BlueFlame3.png")
			GameObj.GameObjects.add(PlayerW)
			PlatformX = GameObj.Width/2
			PlatformY = GameObj.Height/2 + 200
			for i in range(0,10):
				PlatformWidth = random.randint(int(self.Width/7),self.Width/4)
				SinglePlatform = Platform(GameObj.m_Screen,PlatformX,PlatformY, PlatformWidth,32,"platform.png")
				PlatformY = SinglePlatform.rect.y - random.randint(200,400)
				PlatformX  = SinglePlatform.rect.x - random.randint( -GameObj.Width/2, GameObj.Width/2)
				while not (PlatformX + SinglePlatform.Width < GameObj.Width and PlatformX > 0):
					PlatformX  = SinglePlatform.rect.x - random.randint(-GameObj.Width/2, GameObj.Width/2)
				GameObj.GameObjects.add(SinglePlatform)
			pass
		if self.State == "GameMenu":
			pygame.mixer.music.stop()
			pygame.mixer.music.load('MenuTheWave.wav')
			pygame.mixer.music.play(loops=-1)

	def SetScroll(self,scroll:int):
		self.scroll = scroll
	def GetScroll(self):
		return self.scroll
	def Stop(self):
		#print("Custom Game Stop Called score:",int(Variables.score)," high_score:",int(Variables.high_score))
		if Variables.score > Variables.high_score:
			Variables.high_score = int(Variables.score)
			with open('score.txt', 'w',encoding="ascii") as pk:
				score_var=EncryptInt(int(Variables.high_score))
				pk.write(score_var)
		super().Stop()
