import pygame
import sys
import os
import math
import json
import time
#import json
from pygame.locals import *
from pathlib import Path
pygame.font.init()
screen = pygame.display.set_mode((600,500))
pauseScreenOverlay = pygame.Surface((600, 500), pygame.SRCALPHA)
pygame.draw.rect(pauseScreenOverlay, (0,0,0,150), (0,0,pygame.display.Info().current_w,pygame.display.Info().current_h))
Ypos= 0
ygravi = 0
canJump = False
jumpin = False
camX = 0
camY = 0
pause = False
PlacerX = 100
thingAtPlayer = 0
thingAtPlayerSnapTop = 0
thingAtPlayerSnapTopPO = 0
ClickedBtn = False

thingUnderPlayer = 0
playerRow = 1
PlayerRowSnapTop = 1
THISFILE = Path(__file__).resolve().parent
os.chdir(THISFILE)
python = sys.executable
MainMenuDir = "mainMenu.py"
ComicSansFontDir = THISFILE / "fonts" / "Comic Sans MS.ttf"
spikedir = THISFILE / "textures" / "spike.png"
blockdir = THISFILE / "textures" / "block.png"
floordir = THISFILE / "textures" / "floor.png"
cubedir = THISFILE / "textures" / "cube.png"
pausetextdir = THISFILE / "textures" / "pause.png"
OutBtndir = THISFILE / "textures" / "OutBtn.png"
OutBtnImg = pygame.image.load(str(OutBtndir))
blockImg = pygame.image.load(str(blockdir))
spikeImg = pygame.image.load(str(spikedir))
pauseImg = pygame.image.load(str(pausetextdir))
floorImg = pygame.image.load(str(floordir))
cubeImg = pygame.image.load(str(cubedir))

rect = cubeImg.get_rect(center=(100,pygame.display.Info().current_h - 150-Ypos))
cubeRot = 0
jumpsDone = 0
TotalJumpsDone = 0
Attempt = 1
managerJsonDir = THISFILE / "JData" / "MainMNGR.json"
with open(managerJsonDir) as file:
    managerJson = json.load(file)
levelDir = THISFILE / "JData" /(str(managerJson["currentLevel"]) + ".json")
with open(levelDir) as file:
    levelJson = json.load(file)
musicDir = THISFILE / "music" / (str(levelJson["music"]))
pygame.display.set_caption("gomentrie desh: " + str(levelJson["name"]))

pygame.mixer.init()
pygame.mixer.music.load(musicDir)
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(managerJson["volume"]/100)
global TextFont
global TextFont0
TextFont = pygame.font.Font(ComicSansFontDir, 20) 
TextFontO = pygame.font.Font(ComicSansFontDir, 20) 
percentUnCalc = 0
percentUnCalcShort = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            ClickedBtn = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP and not pause:
                jumpin = True
            if event.key == pygame.K_ESCAPE:
                pause = not pause
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP and not pause:
                jumpin = False


    if jumpin and canJump:
        ygravi = 10.33
        cubeRot = 180
        jumpsDone += 1
        TotalJumpsDone += 1

    pygame.display.flip()
    pygame.draw.rect(screen, (levelJson["BGColor"]["r"],levelJson["BGColor"]["g"],levelJson["BGColor"]["b"]), (0,0,pygame.display.Info().current_w,pygame.display.Info().current_h))
    clock = pygame.time.Clock()
    clock.tick(60)
    
    playerRow = 1 + (math.floor(Ypos / 50))
    PlayerRowSnapTop = 1 + (math.ceil(Ypos / 50))
    if playerRow < len(levelJson["data"])+1:thingAtPlayer = levelJson["data"]["row" + str(playerRow)][math.floor((camX * 4)/50)]
    else: thingAtPlayer = 0
    if PlayerRowSnapTop < len(levelJson["data"])+1:thingAtPlayerSnapTop = levelJson["data"]["row" + str(PlayerRowSnapTop)][math.floor((camX * 4)/50)]
    else: thingAtPlayerSnapTop = 0
    if PlayerRowSnapTop < len(levelJson["data"])+1 and PlayerRowSnapTop > 2:thingAtPlayerSnapTopPo = levelJson["data"]["row" + str(PlayerRowSnapTop-1)][math.floor((camX * 4)/50)]
    else: thingAtPlayerSnapTopPO = 0
    if playerRow > 1 and playerRow < len(levelJson["data"])+1:
        thingUnderPlayer = levelJson["data"]["row" + str(playerRow)][math.floor((camX * 4)/50)]
    else: thingUnderPlayer = 0
    if ( thingAtPlayer == "1" or thingAtPlayerSnapTop == "1" or thingAtPlayerSnapTop  == "2"):
        print("ded")
        managerJson["totalAtts"] += 1
        managerJson["totalJumps"] += jumpsDone
        jumpsDone = 0
        with open(managerJsonDir, 'w') as f:
            json.dump(managerJson, f, indent=4)
        pygame.mixer.music.stop()
        time.sleep(0.8)
        Attempt += 1
        camX = 0
        camY = 0
        Ypos = 0
        ygravi = 0
        canJump = False
        jumpin = False
        playerRow = 1
        thingAtPlayer = 0
        thingUnderPlayer = 0
        pygame.mixer.music.play(loops=-1)



    #if thingUnderPlayer == "2":print("bottom block text")

    #print(thingAtPlayer)
    if camY < 100:
        for i in range(10):
            screen.blit(floorImg,((i * 100)-100 - math.fmod(camX *4,100),pygame.display.Info().current_h -100 + camY))	

    rotatedCube = pygame.transform.rotate(cubeImg, (cubeRot*1) + (180 * (jumpsDone)))
    if not pause: cubeRot -= 45/10
    if cubeRot < 0: cubeRot = 0
    #cubeImg = pygame.transform.rotate(cubeImg, 359)
    #screen.blit(cubeImg,(100,pygame.display.Info().current_h - 150-Ypos))

    screen.blit(rotatedCube,rotatedCube.get_rect(center=(100,400 - 25 -Ypos + camY)))
    PlacerX = 100
    #print(len(levelJson["data"]))
    for row in range(len(levelJson["data"])):
        #print(row)
        PlacerX = 100
        for i in range(levelJson["len"]):
            if i*50 - camX * 4 < 500 and  i*50 - camX * 4 > -300 and row*50 - camY < 500 and row*50 - camY > -100:
                #print("row" + str(row + 1))
                if levelJson["data"]["row" + str(row +1)][i] == "1":
                    screen.blit(spikeImg,(PlacerX - camX * 4,pygame.display.Info().current_h - 150 - (row * 50) + camY))
                if levelJson["data"]["row" + str(row + 1)][i] == "2":
                    screen.blit(blockImg,(PlacerX - camX * 4,pygame.display.Info().current_h - 150 - (row * 50) + camY))
            PlacerX += 50
        
    
    #pygame.draw.rect(screen, (50,50,200), (0,pygame.display.Info().current_h - 100,pygame.display.Info().current_w,100))
    #pygame.draw.rect(screen, (200,200,50), (100,pygame.display.Info().current_h - 150-Ypos, 50,50))


    if pause:
        pygame.mixer.music.pause()
        screen.blit(pauseScreenOverlay, (0, 0))
        screen.blit(pauseImg, (0, 0))
        jumpin = False
    else:
        camX += 1.15
        camY += 0.2
        Ypos += ygravi
        ygravi -= 0.45
        canJump = False
        pygame.mixer.music.unpause()
    
        
    if Ypos <= 0 or (thingUnderPlayer == "2"): canJump = True
    if Ypos < 0:ygravi = 0
    if Ypos < 0 or (thingUnderPlayer == "2"):
        ygravi = 0
        if not Ypos >= (PlayerRowSnapTop  *50)-50:    
            Ypos = (PlayerRowSnapTop *50)-49
            if Ypos > 0: Ypos -=1
            else:playerRow = 0
    if ygravi < 0 and  Ypos < 15: Ypos = 0
    if math.floor((camX*4)/50)+1 >= levelJson["len"]:
        print("won")
        sys.exit()
    #screen.blit(TextFont.render(str(thingAtPlayer),True,(0,0,0)),(0,0))
    #screen.blit(TextFont.render(str(thingUnderPlayer),True,(0,0,0)),(0,0))
    #screen.blit(TextFont.render(str(playerRow),True,(0,0,0)),(0,15))
    #screen.blit(TextFont.render(str(ygravi),True,(0,0,0)),(0,30))
    percentUnCalc = math.floor((camX * 4)/12.5)/levelJson["len"]
    #print(len(str(percentUnCalc)))
    if len(str(percentUnCalc))> 5:
        sys.quit()
    percentUnCalcShort = round(percentUnCalc,2)
    if pause:
        screen.blit(TextFont.render(str(levelJson["name"]),True,(255,255,255)),(5,120))
        screen.blit(TextFont.render("Attempt: " + str(Attempt),True,(255,255,255)),(5,140))  
        screen.blit(TextFont.render("Jumps Done: " + str(TotalJumpsDone),True,(255,255,255)),(5,160)) 
        screen.blit(OutBtnImg,(0,300)) 
        #pygame.draw.rect(screen, (0,0,0,0), (0,300,200,100))
        if ClickedBtn and pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pos()[1] > 300:
            os.execl(python, python, str(MainMenuDir))
    screen.blit(TextFont.render(str(round(percentUnCalcShort*25,1)) + "%",True,(255,255,255)),((pygame.display.get_window_size()[0]/2) - TextFont.size(str(round(percentUnCalcShort*25,1)) + "%")[0]/2,470*pause))
        #screen.blit(TextFontO.render(str(levelJson["name"]),True,(255,255,255)),(0,0))
    if ClickedBtn:
        ClickedBtn = False
    pygame.display.flip()
    pygame.display.update()
        