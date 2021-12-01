import pygame
import time
#import Game
#Custom Pygame Lib
import Constants
from Sprite import *
from Game import *

from CustomGame import *
from Player import *
from Platform import *
 

def main():
	max_div=20
	GameObj = CustomGame( Constants.width,Constants.height,"BlueFlame1.png","Game",(0,0,0),"")
	PrevTime = time.time()
	GameObj.Running()



if __name__ == "__main__":
	main()
