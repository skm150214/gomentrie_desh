import pygame
import sys
import math
import json
import os
from pygame.locals import *
from pathlib import Path
pygame.font.init()
screen = pygame.display.set_mode((600,500))
THISFILE = Path(__file__).resolve().parent

logo1dir = THISFILE / "textures" / "logo - Gomentrie Desh.png"
logo2dir = THISFILE / "textures" / "logo - Gomentrie Desh (1).png"
logo3dir = THISFILE / "textures" / "logo - Gomentrie Desh (2).png"
logo4dir = THISFILE / "textures" / "logo - Gomentrie Desh (3).png"
logo5dir = THISFILE / "textures" / "logo - Gomentrie Desh (4).png"
logo6dir = THISFILE / "textures" / "logo - Gomentrie Desh (5).png"
logo1Img = pygame.image.load(str(logo1dir))
logo2Img = pygame.image.load(str(logo2dir))
logo3Img = pygame.image.load(str(logo3dir))
logo4Img = pygame.image.load(str(logo4dir))
logo5Img = pygame.image.load(str(logo5dir))
logo6Img = pygame.image.load(str(logo6dir))
logo1Img = pygame.transform.scale(logo1Img, (510,61))
logo2Img = pygame.transform.scale(logo2Img, (510,61))
logo3Img = pygame.transform.scale(logo3Img, (510,61))
logo4Img = pygame.transform.scale(logo4Img, (510,61))
logo5Img = pygame.transform.scale(logo5Img, (510,61))
logo6Img = pygame.transform.scale(logo6Img, (510,61))

floordir = THISFILE / "textures" / "floor.png"
musicDir = THISFILE / "music" / "gomentrie desh menu loop F.wav"
GamePlayerDir = "gomentrie_desh_gamePlayer.py"
os.chdir(THISFILE)
BackArrowdir = THISFILE / "textures" / "backArrow.png"
playBtndir = THISFILE / "textures" / "playBtn.png"
settingsBtndir = THISFILE / "textures" / "settingsBtn.png"
LevelPlayBtndir = THISFILE / "textures" / "LevelPlayBtn.png"
DragBarOutdir = THISFILE / "textures" / "DragBarOutline.png"
DragBarIndir = THISFILE / "textures" / "DragBarInside.png"
DragBarOutImg = pygame.image.load(str(DragBarOutdir))
DragBarOutImg = pygame.transform.scale(DragBarOutImg, (DragBarOutImg.get_width()*1,DragBarOutImg.get_height()*1))
DragBarInImg = pygame.image.load(str(DragBarIndir))
DragBarInImgForSFX = pygame.image.load(str(DragBarIndir))
backArrowImg = pygame.image.load(str(BackArrowdir))
floorImg = pygame.image.load(str(floordir))
playBtnImg = pygame.image.load(str(playBtndir))
playBtnImg = pygame.transform.scale(playBtnImg, (playBtnImg.get_width()/4,playBtnImg.get_height()/4))
LevelPlayBtnImg = pygame.image.load(str(LevelPlayBtndir))
LevelPlayBtnImg = pygame.transform.scale(LevelPlayBtnImg, (62,62))
settingsBtnImg = pygame.image.load(str(settingsBtndir))
settingsBtnImg = pygame.transform.scale(settingsBtnImg, (settingsBtnImg.get_width()/5,settingsBtnImg.get_height()/5))
DMSansFontDir = THISFILE / "fonts" / "DMSans-ExtraLight.ttf"
camX = 0
OfRGBRed = 0
OfRGBGreen = 0
OfRGBBlue = 0
RedT = 1
GreenT = 1 #hehehe sounds like green tea hehehehehehheheheh
blueT = 1  
LogoTick = 0
logoPhase = 0
MouseDown = False
OnSettings = False
OnSettingsBtn = False
OnPlaySelect = False
OnPlaySelectBtn = False
AbleToClickLevels = False
AbleToEditSettings = False
managerJsonDir = THISFILE / "JData" / "MainMNGR.json"
managerJson = {}
with open(managerJsonDir) as file:
    managerJson = json.load(file)
ReusableLevelJsonDir = {}
global TextFont
TextFont = pygame.font.Font(DMSansFontDir, 20) 
FalseHelperNameLen = 0
MouseUp = False
movinAdd = 0
scroll = 0
FScroll = 0
scrollGravi = 0
Held = False
MouseX = 0
MouseY = 0
a = 0
unfocusSetting = False
TransparentScreenOverlay = pygame.Surface((600, 500), pygame.SRCALPHA)
#DrabBarInsideScreenOverlay = pygame.Surface((100, 500), pygame.SRCALPHA)
python = sys.executable
print(f"Launching: {python} {GamePlayerDir}")
pygame.mixer.init()
pygame.mixer.music.load(musicDir)
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(managerJson["volume"]/100)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            MouseDown = False
            MouseUp = True
        if event.type == pygame.MOUSEWHEEL and OnPlaySelect:
            scrollGravi += event.y



    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.draw.rect(screen, (OfRGBRed,OfRGBGreen,OfRGBBlue), (0,0,pygame.display.Info().current_w,pygame.display.Info().current_h))

    if OnPlaySelect:
        scroll += scrollGravi
        scrollGravi *= 0.8
        if scroll >0:
            scroll = 0
        elif scroll <( -100 - ((2-len(managerJson["levelsFileName"]))*110))*2:
            scroll = (-100 - ((2-len(managerJson["levelsFileName"]))*110))*2
        FScroll = math.floor(scroll)
    for i in range(10):
        screen.blit(floorImg,((i * 100)-100 - math.fmod(camX *4,100),pygame.display.Info().current_h -100))
    if LogoTick > 600: LogoTick = 0
    logoPhase = math.floor(LogoTick / 100)
    if logoPhase == 0:
        screen.blit(logo1Img,(50,20)) # used to be 25 instad of 20 cuz of box
    elif logoPhase == 1:
        screen.blit(logo2Img,(50,20))
    elif logoPhase == 2:
        screen.blit(logo3Img,(50,20))
    elif logoPhase == 3:
        screen.blit(logo4Img,(50,20))
    elif logoPhase == 4:
        screen.blit(logo5Img,(50,20))
    elif logoPhase == 5:
        screen.blit(logo6Img,(50,20))
    LogoTick += 1



    camX += 1.0
    OfRGBRed += 1 * RedT
    OfRGBGreen += 0.84 * GreenT
    OfRGBBlue += 1.28 * blueT
    if OfRGBRed > 255:
        RedT = -1
        OfRGBRed = 255
    if OfRGBRed < 0:
        RedT = 1
        OfRGBRed = 0
    if OfRGBGreen > 255:
        GreenT = -1
        OfRGBGreen = 255
    if OfRGBGreen < 0:
        GreenT = 1
        OfRGBGreen = 0
    if OfRGBBlue > 255: 
        blueT = -1
        OfRGBBlue = 255
    if OfRGBBlue < 0: 
        blueT = 1
        OfRGBBlue = 0
    
    screen.blit(settingsBtnImg,(50 - movinAdd*5,150))
    screen.blit(playBtnImg,(250 + movinAdd*5,150))
    PlayBtnWidth = playBtnImg.get_width()
    PlayBtnHeight = playBtnImg.get_height()
    SettingsBtnWidth = settingsBtnImg.get_width()
    SettingsBtnHeight = settingsBtnImg.get_height()

    #had to move this here cuz of held




    if MouseDown:
        Held = True
    if MouseUp and Held:
        Held = False

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        MouseX = x
        MouseY = y
        if not (OnPlaySelect or OnSettings):
            if x > 250 + PlayBtnWidth/12 and x < 250 + PlayBtnWidth - PlayBtnWidth/12 and y > 150 + PlayBtnHeight/12 and y < 150 + PlayBtnHeight  - PlayBtnHeight/12:
                OnPlaySelectBtn = True
                #print("play")
            if x > 50 + SettingsBtnWidth/8 and x < 50 + SettingsBtnWidth - SettingsBtnWidth/4 and y > 150 + SettingsBtnHeight/8 and y < 150 + SettingsBtnHeight  - SettingsBtnHeight/4:
                OnSettingsBtn = True
                #print("settings")
            #print(x)
            #print(y)
    
    if MouseUp:
        JustClicked = False
        Held = False
        MouseUp = False
        
        if OnPlaySelectBtn:
            if OnPlaySelect: AbleToClickLevels = True
            OnPlaySelect = True
            OnSettings = False
            

        if OnSettingsBtn:
            if OnSettings: AbleToEditSettings = True
            OnSettings = True
            OnPlaySelect = False
    if OnPlaySelect or OnSettings:
        movinAdd = 100
        screen.blit(backArrowImg, (5,5))
        if MouseX <= 55 and MouseY <= 55:
            OnSettings = False
            OnPlaySelect = False
            OnPlaySelectBtn = False
            OnSettingsBtn = False
            AbleToClickLevels = False
            AbleToEditSettings = False
    else:
        movinAdd = 0

    if OnPlaySelect and AbleToClickLevels:
        #for i in range(len(managerJson["levelsFileName"])):
            #if MouseX> 410 and MouseX < 475 and MouseY> scroll+(i*110)+100 and MouseY < scroll+(i*110)+200:
                #if MouseDown:   
                    #print(i)
        #pygame.draw.rect(screen, (0,0,0),(0,MouseY+scroll,300,15))
        #pygame.draw.rect(screen, (0,0,0),(410,100,475-410,100))
        #print("hehhashe")
        for i in range(len(managerJson["levelsFileName"])):
            if math.fabs(FScroll + ((i*110)+100+FScroll)-185) <= 110:

                if MouseX> 410 and MouseX < 475 and MouseY+FScroll > (i*110)+100+FScroll and MouseY+FScroll < (i*110)+200+FScroll:
                    #print(i)
                    #with open(managerJsonDir, 'w') as f:
                    #    json.dump(managerJson, f, indent=4)
                    managerJson["currentLevel"] = str(managerJson["levelsFileName"][i])[:-5]
                    with open(managerJsonDir, 'w') as f:
                        json.dump(managerJson, f, indent=4)
                    #os.system("run" + GamePlayerDir)
                    #sys.exit()

                    os.execl(python, python, str(GamePlayerDir))
                #print("skibidi")

    #screen.blit(TextFont.render("by @skm150214 (on discord)",True,(0,0,0)),(0,30))

    #screen.blit(TextFont.render("by @skm150214 (on discord)",True,(0,0,0)),(4,460)) #left
    #screen.blit(TextFont.render("by @skm150214 (on discord)",True,(0,0,0)),(4,459)) #top left
    #screen.blit(TextFont.render("by @skm150214 (on discord)",True,(0,0,0)),(5,459)) # top
    #screen.blit(TextFont.render("by @skm150214 (on discord)",True,(0,0,0)),(6,459)) # top right
    #screen.blit(TextFont.render("by @skm150214 (on discord)",True,(0,0,0)),(6,460)) #right
    #screen.blit(TextFont.render("by @skm150214 (on discord)",True,(0,0,0)),(6,461)) #bottom right
    #screen.blit(TextFont.render("by @skm150214 (on discord)",True,(0,0,0)),(5,461)) #bottom
    #screen.blit(TextFont.render("by @skm150214 (on discord)",True,(0,0,0)),(4,461)) #bottom left
    def MaxMinNum(num,minNum,maxNum):
        return max(min(num,maxNum),minNum)

    screen.blit(TextFont.render("by @skm150214 (on discord)",True,(255,255,255)),(5,460))
    if OnSettings:
        screen.blit(TextFont.render("Total Attempts: " +  str(managerJson["totalAtts"]),True,(255,255,255)),(375,150))
        screen.blit(TextFont.render("Total Jumps: " +  str(managerJson["totalJumps"]),True,(255,255,255)),(375,170))
        screen.blit(TextFont.render("Settings",True,(255,255,255)),(250,100))
        screen.blit(TextFont.render("Volume",True,(255,255,255)),(100,175))
        screen.blit(TextFont.render("Sfx Volume",True,(255,255,255)),(100,275))
        screen.blit(DragBarInImg, (110,200))
        screen.blit(DragBarOutImg, (100,200))
        screen.blit(DragBarInImgForSFX, (110,300))
        screen.blit(DragBarOutImg, (100,300))
        DragBarInImg = pygame.image.load(str(DragBarIndir))
        DragBarInImgForSFX = pygame.image.load(str(DragBarIndir))
        DragBarInImg = pygame.transform.scale(DragBarInImg, (managerJson["volume"]*1.8,DragBarInImg.get_height()))
        DragBarInImgForSFX = pygame.transform.scale(DragBarInImgForSFX, (managerJson["sfxVolume"]*1.8,DragBarInImgForSFX.get_height()))
        screen.blit(TextFont.render(str(managerJson["volume"])+ "%",True,(255,255,255)),(315,212.5))
        screen.blit(TextFont.render(str(managerJson["sfxVolume"])+ "%",True,(255,255,255)),(315,312.5))

        
        if MouseDown and unfocusSetting and MouseX > 100 and MouseX < 300 and MouseY >= 200 and MouseY <= 300:
            unfocusSetting = False
        if AbleToEditSettings and not unfocusSetting:
            if MouseX > 100 and MouseX < 300 and MouseY >= 200 and MouseY <= 300:
                #print(MouseX)
                #print(180/100)
                #print(max(MouseX,100))
                a = math.floor(math.floor(MaxMinNum(MouseX,110,290)-110)/1.8)
                #managerJson["volume"] =math.floor( float((min(max(MouseX-110,110)),290))/1.8 )#   290-110 = 180
                managerJson["volume"] = a
                with open(managerJsonDir, 'w') as f:
                    json.dump(managerJson, f, indent=4)
                #recalc mouse 
                #print(a)
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                MouseX = x
                MouseY = y
                pygame.mixer.music.set_volume(managerJson["volume"]/100)
                if MouseDown or True:
                    unfocusSetting = True
                    #print("unfocus")

        if MouseDown and unfocusSetting and MouseX > 100 and MouseX < 300 and MouseY >= 300 and MouseY <= 400:
            unfocusSetting = False
        if AbleToEditSettings and not unfocusSetting:
            if MouseX > 100 and MouseX < 300 and MouseY >= 300 and MouseY <= 400:
                #print(MouseX)
                #print(180/100)
                #print(max(MouseX,100))
                a = math.floor(math.floor(MaxMinNum(MouseX,110,290)-110)/1.8)
                #managerJson["volume"] =math.floor( float((min(max(MouseX-110,110)),290))/1.8 )#   290-110 = 180
                managerJson["sfxVolume"] = a
                with open(managerJsonDir, 'w') as f:
                    json.dump(managerJson, f, indent=4)
                #recalc mouse 
                #print(a)
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                MouseX = x
                MouseY = y
                if MouseDown or True:
                    unfocusSetting = True
                    #print("unfocus")





    if OnPlaySelect:
        pygame.draw.rect(TransparentScreenOverlay, (0,0,0,0), (125,0,pygame.display.Info().current_w,pygame.display.Info().current_h))
        def SpawnLevelBox(yoffset, name, id, rating, creator):
            if math.fabs(scroll + yoffset-185) <= 110:
                if len(name) < 6:
                    FalseHelperNameLen = TextFont.size(name + "z"*(6 - len(name)))
                else:
                    FalseHelperNameLen = TextFont.size(name)
            
                pygame.draw.rect(TransparentScreenOverlay, (0,0,0,50), (125,yoffset+scroll,350,100))
                pygame.draw.polygon(TransparentScreenOverlay, (0,0,0),((125,yoffset+scroll),(FalseHelperNameLen[0]+135,yoffset+scroll),(FalseHelperNameLen[0]+135,yoffset+scroll+25),(FalseHelperNameLen[0]+110,yoffset+scroll+25),(FalseHelperNameLen[0]+110,yoffset+scroll+25),(FalseHelperNameLen[0]+110,yoffset+scroll+50),(125,yoffset+scroll+50)))
                pygame.draw.circle(TransparentScreenOverlay, (0,0,0), (FalseHelperNameLen[0]+110,yoffset+scroll+25), 25)
                TransparentScreenOverlay.blit(LevelPlayBtnImg,(412.5,yoffset+scroll+25))
                TransparentScreenOverlay.blit(TextFont.render(name,True,(255,255,255)),(130,yoffset+scroll))    
                TransparentScreenOverlay.blit(TextFont.render(str(id),True,(0,0,0)),(130,yoffset+scroll+75))
                if len(str(creator) )>= 1:TransparentScreenOverlay.blit(TextFont.render("by " +str(creator),True,(0,0,0)),(130,yoffset+scroll+50))
                #pygame.draw.rect(TransparentScreenOverlay, (0,0,0,255), (410,yoffset+scroll,65,100))
                #if x > 410 and x < 475 and y > yoffset+scroll and y < yoffset+scroll+100 and MouseDown and Held:
                    ##scroll += 1
                    #print("hhee")
                    
        for i in range(len(managerJson["levelsFileName"])):
            ReusableLevelJsonDir = THISFILE / "JData" / (str(managerJson["levelsFileName"][i]))
            with open(ReusableLevelJsonDir) as file:
                ReusableLevelJson = json.load(file)
            SpawnLevelBox((i*110)+100,ReusableLevelJson["name"], ReusableLevelJson["id"], "1e",ReusableLevelJson["creator"])
            #if MouseDown: print(y*110+ scroll)
        #for i in range(len(managerJson["levelsFileName"])):
            #if x > 410 and x < 475 and y > (i*110)+100+scroll and y < (i*110)+100+scroll+100 and not MouseUp and Held:
                ##scroll += 1
                #print(i)

        #SpawnLevelBox(320, "level123123123")
        screen.blit(TransparentScreenOverlay, (0, 0))
    screen.blit(TextFont.render(str(Held),True,(255,255,255)),(0,0))
    screen.blit(TextFont.render(str(MouseDown),True,(255,255,255)),(0,20))
    screen.blit(TextFont.render(str(MouseUp),True,(255,255,255)),(0,40))
    screen.blit(TextFont.render(str(MouseY),True,(255,255,255)),(0,60))
    screen.blit(TextFont.render(str(scroll),True,(255,255,255)),(0,80))
    screen.blit(TextFont.render(str(AbleToEditSettings),True,(255,255,255)),(0,100))
    screen.blit(TextFont.render(str(unfocusSetting),True,(255,255,255)),(0,120))
    screen.blit(TextFont.render(str(MouseX),True,(255,255,255)),(0,140))