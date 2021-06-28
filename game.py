import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1000, 800))

# icon = pygame.image.load()
# pygame.diplay.set_caption()

# player
playerImg = pygame.image.load('player.png')
playerimg=pygame.transform.scale(playerImg,(100,100))
playerx=250
playery=700
playerychange=280
playerxchange=50

#background
backImg=pygame.image.load('desert.png')
backimg=pygame.transform.scale(backImg,(1000,800))
backgroundx=0
backgroundy=0
backgroundchange=4


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
    screen.blit(backimg,(x-998,y))

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
                playerx+=playerxchange
                
        if event.type==pygame.KEYUP:
            if jump==True and event.key==pygame.K_SPACE:
                jump=False

            if jump==False:
                playerychange=280
                playerx=cactusx+50
                playery+=playerychange

                if playerx>=700:
                    playerx=250
                player(playerx,playery)
            
                    
    screen.fill((0,0,0))
    background(backgroundx,backgroundy)
    backgroundx-=backgroundchange
    if backgroundx<=0:
        backgroundx=998

    player(playerx,playery)
   

    cactus(cactusx,cactusy)
    cactusx-=cactusychange
    if cactusx<=0:
        cactusx=random.randint(600,2400)
    pygame.display.update()
