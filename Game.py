import pygame
import time
from Sprite import *
import  Constants

class Game:
	def __init__(self,Width : int,Height : int,IconPath : str,Title : str,BackgroundColor=(0,0,0) ,BackgroundImgPath="" ):
		try:
			if self.bInitialized:
				pass
		except Exception as e:
			self.bInitialized = False
		if not self.bInitialized :
			pygame.init()
			self.m_bRunning = True
			self.m_Screen = pygame.display.set_mode((Width,Height))
			self.Width = Width
			self.Height = Height
			self.GameObjects = SpriteGroup()
			self.BackgroundColor = BackgroundColor
			Game.Obj = self
			IconImg = pygame.image.load(IconPath)
			pygame.display.set_icon(IconImg)
			pygame.display.set_caption(Title)
			self.State = "GameMenu"
			try:
				self.backgroundImg = pygame.image.load(BackgroundImgPath)
			except:
				self.backgroundImg = None
			self.bInitialized = True
		else:
			self.__dict__ = self.__shared_state
	def End(self):
		self.m_bRunning = False
		return
	__shared_state = dict()
	def GameInit(self):
		raise Exception("Method not overriden")

	def GameLoop(self):
		raise Exception("Method not overriden")

	def Running(self):
		self.GameInit()
		while self.m_bRunning:
			if self.backgroundImg != None:
				self.m_Screen.blit(self.backgroundImg,(0,0))
			else:
				self.m_Screen.fill(self.BackgroundColor)
			self.GameLoop()
			pygame.display.update()
		return

	def Stop(self):
		#print("Game Stop Called")
		self.m_bRunning = False

	def GetGameObj():
		return Game.Obj
	Obj = None
