import math

import random

import pygame

SCREEN_WIDTH=800

SCREEN_HEIGHT=500

PLAYER_STARTX=370

PLAYER_STARTY=380

ENEMY_STARTY=50

ENEMY_STARTX=150

ENEMY_SPEEDX=4

ENEMY_SPEEDY=40

BULLET_SPEED=10

COLLISSION_DISTANCE=27

pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

background=pygame.image.load('enemy.png')

pygame.display.set_caption("Space Invader")

icon=pygame.image.load('ufo.png')

pygame.display.set_icon(icon)

playerImage=pygame.image.load("player.png")

playerx=PLAYER_STARTX

playery=PLAYER_STARTX

playerx_change=0
enemyimg=[]
enemyx=[]
enemyy=[]
enemyy_change=[]
enemyx_change=[]
number_enemy=6
for enemy in range(number_enemy):
    enemyimg.append(random.randint(0,SCREEN_WIDTH-64))
    enemyy.append(random.randint(ENEMY_STARTX,ENEMY_STARTY))
    enemyx_change.append(ENEMY_SPEEDX)
    enemyy_change.append(ENEMY_SPEEDY)
    bulletx=0
    