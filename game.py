import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 800))

# icon = pygame.image.load()
# pygame.diplay.set_caption()

# player
playerImg = pygame.image.load('player.png')
playerimg=pygame.transform.scale(playerImg,(100,100))
playerx=250
playery=700
playerychange=280

#background
backImg=pygame.image.load('desert.png')
backimg=pygame.transform.scale(backImg,(800,800))
backgroundx=0
backgroundy=0
backgroundchange=3


#obstacle
#tubeImg=

cactusImg=pygame.image.load('cactus.png')
cactusimg=pygame.transform.scale(cactusImg,(50,250))
cactusy=560
cactusx=1500
cactusychange=6
# def pillar(x,y):
#     screen.bl

def cactus(x,y):
    screen.blit(cactusimg,(x,y))

def background(x,y):
    screen.blit(backimg,(x,y))
    screen.blit(backimg,(x-798,y))

def player(x,y):
    screen.blit(playerimg,(x,y))
jump=False
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if jump==False and event.key==pygame.K_SPACE :
                jump=True
            if jump==True:
                playery-=playerychange
        if event.type==pygame.KEYUP:
            if jump==True and event.key==pygame.K_SPACE:
                jump=False
            if jump==False:
                playerychange=280
                playery+=playerychange
                player(playerx,playery)
            #     if event.key==pygame.K_UP:
            #         playerychange=-250

                
        #     if event.key==pygame.K_DOWN:
        #         playerychange=250
                
        # if event.type==pygame.KEYUP:
        #     if event.key==pygame.K_UP:
        #         playery=700
                
        #     if event.key==pygame.K_DOWN:
        #         playery=700
                    
    screen.fill((0,0,0))
    background(backgroundx,backgroundy)
    backgroundx-=backgroundchange
    if backgroundx<=0:
        backgroundx=798

    player(playerx,playery)
    # playery-=playerychange
    # if playery<450:
    #     playery=700
    # if playery>=580:
    #     playery=550


    cactus(cactusx,cactusy)
    cactusx-=cactusychange
    if cactusx<=0:
        cactusx=random.randint(600,2400)
    pygame.display.update()
