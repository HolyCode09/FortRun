# screens.py
from assets import (
    screen, clock, run_bg, paths_img, paths_img2, player1_img, player2_img, before_run_window,
    go_sound, bg_run_music, lose_sound, collect_sound, hit_sound, drama_sound, win_sound, build_sound,
    start_bg, fortress_bg, dust_img, start_music, get_font, load_img, soundsVol
)
from state import y_1, y_2, lives, matsCount, matsSpawned
from utils import exit_game
import pygame_widgets
from pygame_widgets.slider import Slider
import pygame
import random



def game_over_screen():
    font = get_font(300)
    gameOverText = font.render("תלספנ", True, "darkred")
    screen.blit(gameOverText, (50, 120))
    pygame.display.flip()
    pygame.time.delay(4000)
    exit_game()

def settings_screen():

    screen.fill((255, 191, 0))
    brickWall_img = load_img("pics/BrickWall.png", (1130,600))
    screen.blit(brickWall_img, (-20, -50))
    
    woodSign = load_img("pics/WoodSign.png", (300, 100))
    screen.blit(woodSign, (380, 20))

    
    font1 = get_font(50)
    settingsText = font1.render("תורדגה", True, "brown")
    screen.blit(settingsText, (440, 60))
    
    soundSlider = Slider(
        screen,
        250, 200, 100, 10,
        min=0, max=100,
        step=1, initial=100,
        colour=(255, 80, 0), handleColour=(255,0,0), valueColour=(255, 165, 0)
    )
    font2 = get_font(20)    
    soundsText = font2.render("םילילצ", True, (255, 191, 0))
    screen.blit(soundsText, (250, 100))

    musicSlider = Slider(
        screen,
        1080-450, 200, 100, 10,
        min=0, max=100,
        step=1, initial=100,
        colour=(255, 80, 0), handleColour=(255,0,0), valueColour=(255, 165, 0)
    )
    while True:
        soundsVol(soundSlider.getValue() / 100, "sound")
        soundsVol(musicSlider.getValue() / 100, "music")
        # Handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit_game()
        

        pygame_widgets.update(events)
        pygame.display.flip()


# def beforeRun():
    # font = get_font(50)
    # runBackground1 = run_bg
    # paths1 = paths_img
    # screen.blit(runBackground1,(0,0))
    # screen.blit(paths1,(260,0))
    # window = before_run_window
    # screen.blit(window, (0,0))
    # btn0 = pygame.draw.rect(screen, "orange", (300,380, 200,50),0,100)
    # btn1 = pygame.draw.rect(screen, "orange", (580,380, 200,50),0,100)
    # textBoy = font.render("ןב", True, "white")
    # textGirl = font.render("תב", True, "white")
    # screen.blit(textBoy, (370,380))
    # screen.blit(textGirl, (650,380))
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             mouse_pos = pygame.mouse.get_pos()
    #             if btn0.collidepoint(mouse_pos):
    #                 runScreen(0)
    #             if btn1.collidepoint(mouse_pos):
    #                 runScreen(1)
    #     pygame.display.flip()

def runScreen(gen):
    global y_1, y_2, lives, matsSpawned, matsCount
    foodCount = 0  # Add this line at the start of runScreen
    go_sound.play()
    bgMusic = bg_run_music
    bgMusic.play(-1)
    lose = lose_sound
    collectSound = collect_sound
    hitSound = hit_sound
    font = get_font(50)
    item_images = [
        (load_img("pics/needs/life/heart.png", (120,120)), "life"),
        (load_img("pics/needs/life/heart.png", (120,120)), "life"),
        (load_img("pics/needs/life/heart.png", (120,120)), "life"),
        (load_img("pics/needs/life/heart.png", (120,120)), "life"),
        (load_img("pics/needs/life/heart.png", (120,120)), "life"),
        (load_img("pics/needs/life/food1.png", (120,120)), "food"),
        (load_img("pics/needs/life/food2.png", (120,120)), "food"),
        (load_img("pics/needs/life/food3.png", (120,120)), "food"),
        (load_img("pics/needs/life/food4.png", (120,120)), "food"),
        (load_img("pics/needs/life/food5.png", (120,120)), "food"),
        (load_img("pics/needs/life/food6.png", (120,120)), "food"),
        (load_img("pics/needs/life/food7.png", (120,120)), "food"),
        (load_img("pics/needs/life/water.png", (120,120)), "food"),
        (load_img("pics/needs/mats/bricks.png", (120,120)), "mats"),
        (load_img("pics/needs/mats/metal.png", (120,120)), "mats"),
        (load_img("pics/needs/mats/wood.png", (120,120)), "mats"),
        (load_img("pics/needs/mats/bricks.png", (120,120)), "mats"),
        (load_img("pics/needs/mats/metal.png", (120,120)), "mats"),
        (load_img("pics/needs/mats/wood.png", (120,120)), "mats"),
        (load_img("pics/obstacles/clothes_obsticle.png", (120,120)), "obs"),
        (load_img("pics/obstacles/sand_obsticle.png", (120,120)), "obs"),
        (load_img("pics/obstacles/stone_obsticle.png", (120,120)), "obs"),
        (load_img("pics/obstacles/clothes_obsticle.png", (120,120)), "obs"),
        (load_img("pics/obstacles/sand_obsticle.png", (120,120)), "obs"),
        (load_img("pics/obstacles/stone_obsticle.png", (120,120)), "obs"),
    ]
    items_pos = []
    add_interval = 1000
    last_add_time = 0

    def has_mats_on_screen():
        return any(item[2][1] == "mats" for item in items_pos)

    def has_hearts_on_screen():
        return any(item[2][1] == "life" for item in items_pos)

    def add_new_item():
        global matsSpawned
        item_x = random.choice([300,495,690])
        item_y = -100
        item_image = random.choice(item_images)
        if item_image[1] == "life" and (lives == 3 or has_hearts_on_screen()):
            add_new_item()
            return
        if item_image[1] == "mats" and has_mats_on_screen():
            add_new_item()
            return
        items_pos.append((item_x, item_y, item_image))
        if item_image[1] == "mats":
            matsSpawned += 1

    x_player = 495
    path = "Mid"
    runBackground1 = run_bg
    runBackground2 = run_bg
    paths1 = paths_img
    paths2 = paths_img2
    player1 = player1_img
    player2 = player2_img
    players = [player1,player2]
    time = 0

    def colideHappen(rightX):
        global lives, matsCount
        nonlocal foodCount  # Add this line
        for item in items_pos:
            if item[0] == rightX and item[1] < 480 and item[1] > 520 - 250:
                items_pos.remove(item)
                if item[2][1] == "mats":
                    collectSound.play()
                    matsCount+=1
                if item[2][1] == "obs":
                    hitSound.play()
                    lives-=1
                if item[2][1] == "life":
                    collectSound.play()
                    lives+=1
                if item[2][1] == "food":
                    collectSound.play()
                    foodCount+=1

    while True:
        time+=1
        screen.blit(runBackground1,(0,y_1))
        screen.blit(runBackground2,(0,y_2))
        screen.blit(paths1,(260,y_1))
        screen.blit(paths2,(257,y_2))
        needs = font.render(f"10/{matsCount} םירמוח", True, "white")
        livesCheck = font.render(f"{lives} :םייח רפסמ", True, "white")
        foodCheck = font.render(f"{foodCount} :הייחמ יבאשמ", True, "white")
        food_x = 690 if foodCount < 10 else 670
        screen.blit(needs, (760,0))
        screen.blit(livesCheck, (750,50))
        screen.blit(foodCheck, (food_x,100))
        y_1+=2
        y_2+=2
        if y_1>=520:
            y_1=-520
        if y_2>=520:
            y_2=-520
        if path == "Mid":
            x_player=495
        elif path == "Left":
            x_player = 300
        else:
            x_player = 690
        screen.blit(players[gen],(x_player,320))
        if time%35==0:
            players[gen] = pygame.transform.flip(players[gen], True, False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if path == "Right":
                    path = "Mid"
                elif path == "Mid":
                    path = "Left"
            elif keys[pygame.K_RIGHT]:
                if path == "Left":
                    path = "Mid"
                elif path == "Mid":
                    path = "Right"
        clock.tick(600)
        current_time = pygame.time.get_ticks()
        if current_time - last_add_time > add_interval:
            add_new_item()
            last_add_time = current_time
        for i in range(len(items_pos)):
            items_pos[i] = (items_pos[i][0], items_pos[i][1] + 2, items_pos[i][2])
        items_pos = [item for item in items_pos if item[1] < 520]
        if matsSpawned<11:
            for pos in items_pos:
                screen.blit(pos[2][0], (pos[0], pos[1]))
        else:
            bgMusic.stop()
            baseScreen()
        if lives == 0:
            bgMusic.stop()
            lose.play()
            game_over_screen()
        if x_player == 300:
            colideHappen(300)
        elif x_player == 495:
            colideHappen(495)
        else:
            colideHappen(690)
        pygame.display.flip()

def build(persentage):
    base = load_img(f"pics/Building_{persentage}%.png", (450,450))
    return base

def baseScreen():
    global matsCount
    drama = drama_sound
    drama.play()
    Win = win_sound
    lose = lose_sound
    p = 25 if 0 <= matsCount < 3 else 50 if 2 < matsCount < 6 else 75 if 5 < matsCount < 10 else 100
    font = get_font(20)
    text1 = font.render(f"םלש {p}% אוה ךלש רצבמה", True, "darkred")
    ans = "תחצינ!" if p >=75 else "...תדספה"
    text2 = font.render(ans, True, "darkred")
    pygame.time.delay(1000)
    bgPic = fortress_bg
    current_base = build(p)
    dust = dust_img
    buildSound = build_sound
    buildSound.play()
    for i in range(11):
        screen.blit(bgPic,(0,0))
        dust = pygame.transform.scale(dust, (600,600))
        screen.blit(dust,(220,-20))
        pygame.time.delay(300)
        pygame.display.flip()
        screen.blit(bgPic,(0,0))
        dust = pygame.transform.scale(dust, (650,650))
        screen.blit(dust,(200,-35))
        pygame.time.delay(300)
        pygame.display.flip()
    if p>=75:
        Win.play()
    else:
        lose.play()
    while True:
        screen.blit(bgPic,(0,0))
        screen.blit(current_base, (325, 30))
        screen.blit(text1, (750,40))
        screen.blit(text2, (250,40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.flip()

btnRect = pygame.Rect(400,350, 300,100)
def startScreen():
    startBackground = start_bg
    screen.blit(startBackground,(0,0))
    bgMuisc = start_music
    bgMuisc.play(-1)
    font1 = get_font(50)
    font2Border = get_font(155)
    font2 = get_font(150)
    font3Border = get_font(205)
    font3 = get_font(200)
    titleText1Border = font2Border.render("ץורימה", True, "white")
    titleText1 = font2.render("ץורימה", True, "orange")
    titleText2Border = font3Border.render("רצבמל", True, "brown")
    titleText2 = font3.render("רצבמל", True, "orange")
    startBtnText = font1.render("לחתה", True, "brown")
    startBtnTextShadow = font1.render("לחתה", True, "black")
    pygame.draw.rect(screen,"orange", btnRect,0,100)
    pygame.draw.rect(screen,"brown", (400,350, 300,100),5,100)
    screen.blit(titleText1Border, (275,0))
    screen.blit(titleText1, (285,3))
    screen.blit(titleText2Border, (200,100))
    screen.blit(titleText2, (207,103))
    screen.blit(startBtnTextShadow,(479,375))
    screen.blit(startBtnText,(477,372))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnRect.collidepoint(event.pos):
                    # bgMuisc.stop()
                    settings_screen()
        pygame.display.flip()