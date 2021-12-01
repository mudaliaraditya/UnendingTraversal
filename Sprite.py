import pygame

class Sprite():
	def __init__(self,screen,x : int,y: int,Width : int,Height : int,ImagePath : str):
		self.ImagePath = ImagePath
		self.Image = pygame.image.load(self.ImagePath).convert_alpha()
		self.Image = pygame.transform.smoothscale(self.Image, (Width, Height))
		self.rect = self.Image.get_rect()
		if self.rect == None:
			raise Exception("no rect available")
		self.rect.x = x
		self.rect.y = y
		self.Screen = screen
		self.Height = Height
		self.Width = Width

	def update(self):
		self.Image = pygame.transform.scale(self.Image, (self.Width, self.Height ))
		self.Screen.blit(self.Image,(self.rect.x,self.rect.y))

class FlippingSprite(Sprite):
	def __init__(self,screen,x : int,y: int,Width : int,Height : int,ImagePath : str):
		super().__init__(screen,x,y,Width,Height,ImagePath)
		self.FlipX = False
		self.FlipY = False	

	def SetFlipX(self):
		self.FlipX = True
	def ResetFlipX(self):
		self.FlipX = False

	def SetFlipY(self):
		self.FlipY = True	
	def ResetFlipY(self):
		self.FlipY = False

	def update(self):
		self.Image = pygame.transform.flip(self.Image,self.FlipX,self.FlipY)
		super().update()

class AnimatedSprite(FlippingSprite):
	def __init__(self,screen,x : int,y: int,Width : int,Height : int,ImagePath):
		Image = str(ImagePath[0])
		super().__init__(screen,x,y,Width,Height,Image)
		self.Counter = 0
		self.ListImagePath = ImagePath

	def update(self):
		self.Image = pygame.image.load( self.ListImagePath[self.Counter]).convert_alpha()
		self.Counter +=1
		if self.Counter >= len(self.ListImagePath):
			self.Counter = 0
		super().update()


class DissaperingSprite(Sprite):
	def __init__(self,screen,x : int,y: int,Width : int,Height : int,ImagePath : str):
		super().__init__(screen,x,y,Width,Height,ImagePath)
		self.bDissapear = False
	def isinvisible(self):
		return self.bDissapear
	def update(self):
		if not self.bDissapear:
			super().update()


class SpriteGroup():
	def __init__(self):
		self.List = list()
		self.Len = 0
		self.iter = 0
	def add(self,obj : Sprite):
		self.List.append(obj)
		self.Len = len(self.List)
	def update(self):
		for item  in self.List:
			item.update()
	def clear(self):
		self.List.clear()

	def __iter__(self):
		return self.List.__iter__()
	def __next__(self):
		return self.List.__next__()
		self.iter += 1
		if (self.iter - 1) > self.Len:
			return List[self.iter]
		else:
			self.iter = 0
			raise StopIteration



def draw_text(screen,text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

