
import random
from Sprite import *
from Game import *


class Platform(DissaperingSprite):
	def __init__(self,screen,x : int,y: int,Width : int,Height : int,ImagePath : str):
		super().__init__(screen,x,y,Width,Height,ImagePath)
		if   Platform.LastPlatform == None or  self.rect.y < Platform.LastPlatform.rect.y :
				Platform.LastPlatform = self

	def CheckCollision(self,player):
		if self.isinvisible():
			return False
		#print("Collision Check Player x:",player.rect.x," Player y:",player.rect.y, " Platform x:",self.rect.x,"Platform y:",self.rect.y)
		#if ((player.rect.y + player.Height >= self.rect.y) and (player.rect.y + player.Height < self.rect.y + self.Height )  ) and (player.rect.x + (player.Width/2) > self.rect.x and (player.rect.x + (player.Width/2) )  < (self.rect.x + self.Width)):
		if ((player.rect.y + player.Height >= self.rect.y) and (player.rect.y + player.Height < self.rect.y + self.Height )  ) and (player.rect.x + (player.Width) > self.rect.x and (player.rect.x + (player.Width/2) )  < (self.rect.x + self.Width)):
			#print("Collision Check sucess")
			if player.rect.y + player.Height > self.rect.y + 1:
				player.rect.y = self.rect.y - player.Height
			return True
		return False

	def MoveUp(self):
		GameObj = Game.GetGameObj()
		self.rect.y += GameObj.GetScroll()

	LastPlatform=None


	def update(self):
		GameObj = Game.GetGameObj()
		if self.rect.y > GameObj.Height:
			self.rect.y = Platform.LastPlatform.rect.y -  random.randint(200,300)
			Platform.LastPlatform = self
			PlatformWidth  = self.rect.x - random.randint( -GameObj.Width/2, GameObj.Width/2)
			while not (PlatformWidth + self.Width < GameObj.Width and PlatformWidth > 0):
				PlatformWidth  = self.rect.x - random.randint(-GameObj.Width/2, GameObj.Width/2)
			self.rect.x = PlatformWidth
			self.bDissapear = False
		super().update()



class PlatformGroup(SpriteGroup):
	def __init__(self):
		super().__init__()
