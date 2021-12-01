import pygame

GAMESPEED=1
SPEED = GAMESPEED * 10
GRAVITY = 0.5
Time = 0
FACTOR=200
PrevTime = 0
JUMP_HEIGHT=30
Dt = 0
FPS=GAMESPEED*60
width=600
height=900
scroll_thresh=(height*(1/4))
PlayerMaxHealth=10000
PlayerGetHealthOnJump=True
TickHealthReducer=0.1
PlayerHealthGainOnJump=100
PlatformDestructionOnCollisionWithPlayer=True
PlayerSizeSmall=128
PlayerSizeNormal=64
PlayerSizeSmall=32

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0,102,0)
BLUE = (0,0,102)
PANEL = (153, 217, 234)





