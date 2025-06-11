# screens.py
from assets import (
    screen,
    clock,
    run_bg,
    player1_img,
    player2_img,
    before_run_window,
    go_sound,
    bg_run_music,
    lose_sound,
    collect_sound,
    hit_sound,
    drama_sound,
    win_sound,
    build_sound,
    start_bg,
    fortress_bg,
    dust_img,
    start_music,
    select_sound,
    goBack,
    desertMap,
    seaMap,
    moonMap,
    forestMap,
    galaxyMap,
    candyWorldMap,
    candyWorldrunMap,
    desertrunMap,
    forestrunMap,
    moonrunMap,
    searunMap,
    spacerunMap,
    candyWorldRunPath,
    desertRunPath,
    forestRunPath,
    spaceRunPath,
    moonRunPath,
    seaRunPath,
    woodSurface,
    get_font,
    load_img,
    soundsVol,
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


soundsVolume = musicVolume = 100
gen = "boy"
place = 0
chosen_toys = [
    0,
    1,
    2,
]  # Indices of the 3 chosen toys, persists outside settings_screen
maps = [desertMap, forestMap, seaMap, candyWorldMap, moonMap, galaxyMap]
chosen_map = maps[place]


def settings_screen():
    global soundsVolume, musicVolume, gen, place, chosen_toys, maps, chosen_map

    screen.fill((255, 191, 0))
    brickWall_img = load_img("pics/BrickWall.png", (1130, 600))
    screen.blit(brickWall_img, (-20, -50))

    screen.blit(goBack, (20, 20))

    woodSign = load_img("pics/titleWoodenSign.png", (300, 100))
    screen.blit(woodSign, (390, 37))


    font1 = get_font(50)
    settingsText = font1.render("תורדגה", True, "white")
    screen.blit(settingsText, (440, 60))

    pygame.draw.rect(screen, (255, 255, 255), (225, 140, 200, 65), 4, 5)

    soundSlider = Slider(
        screen,
        310,
        150,
        100,
        10,
        min=0,
        max=100,
        step=1,
        initial=soundsVolume,
        colour=(255, 80, 0),
        handleColour=(255, 255, 255),
        valueColour=(255, 165, 0),
    )
    font2 = get_font(20)
    soundsText = font2.render("םילילצ", True, "white")
    screen.blit(soundsText, (230, 145))

    musicSlider = Slider(
        screen,
        310,
        180,
        100,
        10,
        min=0,
        max=100,
        step=1,
        initial=musicVolume,
        colour=(255, 80, 0),
        handleColour=(255, 255, 255),
        valueColour=(255, 165, 0),
    )
    soundsText = font2.render("הקיסומ", True, "white")
    screen.blit(soundsText, (230, 175))

    pygame.draw.rect(screen, (255, 255, 255), (430, 140, 440, 170), 4, 5)

    boy = load_img("pics/Runner1.png", (105, 145))
    girl = load_img("pics/Runner2.png", (110, 150))
    screen.blit(boy, (500, 150))
    screen.blit(girl, (670, 150))

    boyRect = pygame.draw.rect(screen, (255, 191, 0), (500, 150, 110, 150), 4, 5)
    girlRect = pygame.draw.rect(screen, (255, 255, 255), (670, 150, 110, 150), 4, 5)

    pygame.draw.rect(screen, (255, 255, 255), (225, 210, 200, 100), 4, 5)
    pygame.draw.rect(screen, "black", (260, 215, 130, 90), 4, 5)

    screen.blit(maps[place], (264, 219))
    arrowLeft = font1.render("<", True, (255, 255, 255))
    arrowRight = font1.render(">", True, (255, 255, 255))
    screen.blit(arrowLeft, (229, 235))
    screen.blit(arrowRight, (395, 235))

    pygame.draw.rect(screen, (255, 255, 255), (225, 315, 645, 110), 4, 5)
    # five squares inside the rectangle to contain 5 toys
    bearToy = load_img("pics/toys/bear.png", (70, 70))
    legoToye = load_img("pics/toys/lego.png", (70, 70))
    puzzleToy = load_img("pics/toys/puzzle.png", (70, 70))
    nintendoToy = load_img("pics/toys/nintendo.png", (70, 70))
    barbieToy = load_img("pics/toys/barbie.png", (70, 70))

    toys = [bearToy, legoToye, puzzleToy, nintendoToy, barbieToy]

    # --- Toys squares logic ---
    toy_rects = []
    toy_frame_colors = [(255, 191, 0)] * 3 + [
        (255, 255, 255)
    ] * 2  # First 3 yellow, last 2 white
    toy_selected = [i in chosen_toys for i in range(5)]
    toy_order = (
        chosen_toys.copy()
    )  # Indices of currently selected toys, in order of selection

    rightX = 267
    for i in range(5):
        toy_rect = pygame.Rect(rightX, 330, 80, 80)
        toy_rects.append(toy_rect)
        frame_color = (255, 191, 0) if toy_selected[i] else (255, 255, 255)
        pygame.draw.rect(screen, frame_color, toy_rect, 4, 5)
        screen.blit(toys[i], (rightX + 4, 335))
        rightX += 120

    # ...existing code...

    while True:
        soundsVol(soundSlider.getValue() / 100, "sound")
        soundsVol(musicSlider.getValue() / 100, "music")
        soundsVolume = soundSlider.getValue()
        musicVolume = musicSlider.getValue()
        # Handle events
        if gen == "boy":
            pygame.draw.rect(screen, (255, 191, 0), (500, 150, 110, 150), 4, 5)
            pygame.draw.rect(screen, (255, 255, 255), (670, 150, 110, 150), 4, 5)
        else:
            pygame.draw.rect(screen, (255, 255, 255), (500, 150, 110, 150), 4, 5)
            pygame.draw.rect(screen, (255, 191, 0), (670, 150, 110, 150), 4, 5)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit_game()
            mouse_pos = pygame.mouse.get_pos()
            # --- Toys squares hover cursor ---
            toys_cursor = False
            for rect in toy_rects:
                if rect.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    toys_cursor = True
                    break
            if not toys_cursor:
                if goBack.get_rect(topleft=(20, 20)).collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            # --- Toys squares click logic ---
            if event.type == pygame.MOUSEBUTTONDOWN:
                if goBack.get_rect(topleft=(20, 20)).collidepoint(mouse_pos):
                    select_sound.play()
                    startScreen()
                    return
                for idx, rect in enumerate(toy_rects):
                    if rect.collidepoint(mouse_pos):
                        if not toy_selected[idx]:
                            # If already 3 selected, unselect the earliest one
                            if sum(toy_selected) == 3:
                                first_idx = toy_order.pop(0)
                                toy_selected[first_idx] = False
                                pygame.draw.rect(
                                    screen, (255, 255, 255), toy_rects[first_idx], 4, 5
                                )
                                screen.blit(
                                    toys[first_idx],
                                    (
                                        toy_rects[first_idx].x + 4,
                                        toy_rects[first_idx].y + 5,
                                    ),
                                )
                            # Select new toy
                            toy_selected[idx] = True
                            toy_order.append(idx)
                            pygame.draw.rect(screen, (255, 191, 0), rect, 4, 5)
                            screen.blit(toys[idx], (rect.x + 4, rect.y + 5))
                            # Update global chosen_toys
                            chosen_toys = toy_order.copy()
                            select_sound.play()
                            pygame.display.update([rect])
                        break
                # ...existing code...
                if boyRect.collidepoint(mouse_pos):
                    select_sound.play()
                    gen = "boy"
                elif girlRect.collidepoint(mouse_pos):
                    select_sound.play()
                    gen = "girl"
                elif arrowLeft.get_rect(topleft=(229, 235)).collidepoint(mouse_pos):
                    select_sound.play()
                    screen.blit(font1.render("<", True, (255, 191, 0)), (229, 235))
                    place -= 1
                    if place < 0:
                        place = len(maps) - 1
                    screen.blit(maps[place], (264, 219))
                elif arrowRight.get_rect(topleft=(395, 235)).collidepoint(mouse_pos):
                    select_sound.play()
                    screen.blit(font1.render(">", True, (255, 191, 0)), (395, 235))
                    place += 1
                    if place >= len(maps):
                        place = 0
                    screen.blit(maps[place], (264, 219))
            if event.type == pygame.MOUSEBUTTONUP:
                screen.blit(font1.render("<", True, (255, 255, 255)), (229, 235))
                screen.blit(font1.render(">", True, (255, 255, 255)), (395, 235))

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


def apply_grayscale(surface):
    grayscale = pygame.Surface(surface.get_size()).convert_alpha()
    for y in range(surface.get_height()):
        for x in range(surface.get_width()):
            pixel = surface.get_at((x, y))
            avg = (pixel.r + pixel.g + pixel.b) // 3
            grayscale.set_at((x, y), (avg, avg, avg, pixel.a))
    return grayscale


def runScreen(gen):
    global y_1, y_2, lives, matsSpawned, matsCount, place, candyWorldrunMap, desertrunMap, forestrunMap, moonrunMap, searunMap, spacerunMap, candyWorldRunPath, desertRunPath, forestRunPath, moonRunPath, seaRunPath, spaceRunPath, woodSurface
    runMaps = [
        desertrunMap,
        forestrunMap,
        searunMap,
        candyWorldrunMap,
        moonrunMap,
        spacerunMap,
    ]
    runPaths = [
        desertRunPath,
        forestRunPath,
        seaRunPath,
        candyWorldRunPath,
        moonRunPath,
        spaceRunPath,
    ]

    foodCount = 0  # Add this line at the start of runScreen
    toysCollected = 0  # Track collected toys
    summoned_toys = set()  # Track which toys have been summoned
    go_sound.play()
    bgMusic = bg_run_music
    bgMusic.play(-1)
    lose = lose_sound
    collectSound = collect_sound
    hitSound = hit_sound
    font = get_font(20)
    item_images = [
        (load_img("pics/needs/life/heart.png", (120, 120)), "life"),
        (load_img("pics/needs/life/heart.png", (120, 120)), "life"),
        (load_img("pics/needs/life/heart.png", (120, 120)), "life"),
        (load_img("pics/needs/life/heart.png", (120, 120)), "life"),
        (load_img("pics/needs/life/heart.png", (120, 120)), "life"),
        (load_img("pics/needs/life/food1.png", (120, 120)), "food"),
        (load_img("pics/needs/life/food2.png", (120, 120)), "food"),
        (load_img("pics/needs/life/food3.png", (120, 120)), "food"),
        (load_img("pics/needs/life/food4.png", (120, 120)), "food"),
        (load_img("pics/needs/life/food5.png", (120, 120)), "food"),
        (load_img("pics/needs/life/food6.png", (120, 120)), "food"),
        (load_img("pics/needs/life/food7.png", (120, 120)), "food"),
        (load_img("pics/needs/life/water.png", (120, 120)), "food"),
        (load_img("pics/needs/mats/bricks.png", (120, 120)), "mats"),
        (load_img("pics/needs/mats/metal.png", (120, 120)), "mats"),
        (load_img("pics/needs/mats/wood.png", (120, 120)), "mats"),
        (load_img("pics/needs/mats/bricks.png", (120, 120)), "mats"),
        (load_img("pics/needs/mats/metal.png", (120, 120)), "mats"),
        (load_img("pics/needs/mats/wood.png", (120, 120)), "mats"),
        (load_img("pics/obstacles/clothes_obsticle.png", (120, 120)), "obs"),
        (load_img("pics/obstacles/sand_obsticle.png", (120, 120)), "obs"),
        (load_img("pics/obstacles/stone_obsticle.png", (120, 120)), "obs"),
        (load_img("pics/obstacles/clothes_obsticle.png", (120, 120)), "obs"),
        (load_img("pics/obstacles/sand_obsticle.png", (120, 120)), "obs"),
        (load_img("pics/obstacles/stone_obsticle.png", (120, 120)), "obs"),
    ]
    # Add chosen toys to the list of possible items to summon, but only once each
    toy_imgs = [
        load_img("pics/toys/bear.png", (120, 120)),
        load_img("pics/toys/lego.png", (120, 120)),
        load_img("pics/toys/puzzle.png", (120, 120)),
        load_img("pics/toys/nintendo.png", (120, 120)),
        load_img("pics/toys/barbie.png", (120, 120)),
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
        item_x = random.choice(
            [285, 485, 680]
        )  # Adjusted x positions more to the right
        item_y = -100

        # Summon a toy if not all have been summoned yet
        if len(summoned_toys) < 3:
            available_toys = [i for i in chosen_toys if i not in summoned_toys]
            if available_toys and random.random() < 0.15:  # 15% chance to summon a toy
                toy_idx = random.choice(available_toys)
                items_pos.append((item_x, item_y, (toy_imgs[toy_idx], "toy", toy_idx)))
                summoned_toys.add(toy_idx)
                return

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

    x_player = 485  # Middle lane position, adjusted more to the right
    path = "Mid"
    runBackground1 = runMaps[place]
    paths1 = runPaths[place]
    paths2 = runPaths[place]
    player1 = player1_img
    player2 = player2_img
    players = [player1, player2]
    time = 0

    def colideHappen(rightX):
        global lives, matsCount
        nonlocal foodCount
        nonlocal toysCollected
        for item in items_pos:
            if item[0] == rightX and item[1] < 480 and item[1] > 520 - 250:
                items_pos.remove(item)
                if item[2][1] == "mats":
                    collectSound.play()
                    matsCount += 1
                if item[2][1] == "obs":
                    hitSound.play()
                    lives -= 1
                if item[2][1] == "life":
                    collectSound.play()
                    lives += 1
                if item[2][1] == "food":
                    collectSound.play()
                    foodCount += 1
                if item[2][1] == "toy":
                    collectSound.play()
                    toysCollected = min(toysCollected + 1, 3)

    matsStack = load_img("pics/miniStacks/matsStack.png", (20,20))
    foodStack = load_img("pics/miniStacks/foodStack.png", (20,20))
    toysStack = load_img("pics/miniStacks/toysStack.png", (20,20))
    while True:
        time += 1
        screen.blit(runBackground1, (0, 0))
        screen.blit(paths1, (240, y_1))  # Adjusted from 220 to 240
        screen.blit(paths2, (237, y_2))  # Adjusted from 217 to 237
        screen.blit(woodSurface, (820, -35))

        heartImg = load_img("pics/needs/life/heart.png", (50, 50))
        grayHeartImg = apply_grayscale(heartImg)
        hearts = [heartImg] * lives + [grayHeartImg] * (3 - lives)
        spaceBetwweenHearts = 50
        for i in range(3):
            screen.blit(hearts[i], (20 + i * spaceBetwweenHearts, 20))

        needs = font.render(f":םירמוח", True, "white")
        foodCheck = font.render(":ןוזמ", True, "white")
        toysCheck = font.render(":םיעוצעצ", True, "white")
        screen.blit(needs, (1000, 10))
        screen.blit(foodCheck, (1030, 55))
        screen.blit(toysCheck, (985, 100))
        grayMatsStack = apply_grayscale(matsStack)
        grayFoodStack = apply_grayscale(foodStack)
        grayToysStack = apply_grayscale(toysStack)
        matsCollectedStack = [matsStack] * matsCount + [grayMatsStack] * (10 - matsCount)
        foodCollectedStack = [foodStack] * foodCount + [grayFoodStack] * (10 - foodCount)
        toysCollectedStack = [toysStack] * toysCollected + [grayToysStack] * (3 - toysCollected)
        spaceBetweenStacks = 20
        for i in range(10):
            screen.blit(matsCollectedStack[i], (1050 - i * spaceBetweenStacks, 30))
            screen.blit(foodCollectedStack[i], (1050 - i * spaceBetweenStacks, 75))
        for i in range(3):
            screen.blit(toysCollectedStack[i], (1050 - i * spaceBetweenStacks, 120))
        y_1 += 2
        y_2 += 2
        if y_1 >= 520:
            y_1 = -520
        if y_2 >= 520:
            y_2 = -520
        if path == "Mid":
            x_player = 485  # Adjusted middle position
        elif path == "Left":
            x_player = 285  # Adjusted left position
        else:
            x_player = 680  # Adjusted right position
        screen.blit(players[gen], (x_player, 320))
        if time % 35 == 0:
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
        if matsSpawned < 11:
            for pos in items_pos:
                screen.blit(pos[2][0], (pos[0], pos[1]))
        else:
            bgMusic.stop()
            baseScreen()
        if lives == 0:
            bgMusic.stop()
            lose.play()
            game_over_screen()
        if x_player == 285:
            colideHappen(285)
        elif x_player == 485:
            colideHappen(485)
        else:
            colideHappen(680)
        pygame.display.flip()


def build(persentage):
    base = load_img(f"pics/Building_{persentage}%.png", (450, 450))
    return base


def baseScreen():
    global matsCount
    drama = drama_sound
    drama.play()
    Win = win_sound
    lose = lose_sound
    p = (
        25
        if 0 <= matsCount < 3
        else 50 if 2 < matsCount < 6 else 75 if 5 < matsCount < 10 else 100
    )
    font = get_font(20)
    text1 = font.render(f"םלש {p}% אוה ךלש רצבמה", True, "darkred")
    ans = "תחצינ!" if p >= 75 else "...תדספה"
    text2 = font.render(ans, True, "darkred")
    pygame.time.delay(1000)
    bgPic = fortress_bg
    current_base = build(p)
    dust = dust_img
    buildSound = build_sound
    buildSound.play()
    for i in range(11):
        screen.blit(bgPic, (0, 0))
        dust = pygame.transform.scale(dust, (600, 600))
        screen.blit(dust, (220, -20))
        pygame.time.delay(300)
        pygame.display.flip()
        screen.blit(bgPic, (0, 0))
        dust = pygame.transform.scale(dust, (650, 650))
        screen.blit(dust, (200, -35))
        pygame.time.delay(300)
        pygame.display.flip()
    if p >= 75:
        Win.play()
    else:
        lose.play()
    while True:
        screen.blit(bgPic, (0, 0))
        screen.blit(current_base, (325, 30))
        screen.blit(text1, (750, 40))
        screen.blit(text2, (250, 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.flip()


def startScreen():
    global gen
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    startBackground = start_bg
    screen.blit(startBackground, (0, 0))
    # font1 = get_font(50)
    # font2Border = get_font(155)
    # font2 = get_font(150)
    # font3Border = get_font(205)
    # font3 = get_font(200)
    # titleText1Border = font2Border.render("ץורימה", True, "white")
    # titleText1 = font2.render("ץורימה", True, "orange")
    # titleText2Border = font3Border.render("רצבמל", True, "brown")
    # titleText2 = font3.render("רצבמל", True, "orange")
    # startBtnText = font1.render("לחתה", True, "brown")
    # startBtnTextShadow = font1.render("לחתה", True, "black")
    # pygame.draw.rect(screen,"orange", btnRect,0,100)
    # pygame.draw.rect(screen,"brown", (400,350, 300,100),5,100)
    # screen.blit(titleText1Border, (275,0))
    # screen.blit(titleText1, (285,3))
    # screen.blit(titleText2Border, (200,100))
    # screen.blit(titleText2, (207,103))
    # screen.blit(startBtnTextShadow,(479,375))
    # screen.blit(startBtnText,(477,372))

    icon = load_img("pics/game_Icon.png", (750, 300))
    screen.blit(icon, (-10, 60))

    lines = ["םיבושח םירבד ופסאת ,וצורת ,הקתפרהל ואצ", "ףוסב םכלש ידוסה רצבמה תא ונבו"]

    sticker = load_img("pics/goSettingsSticker.png", (185, 185))
    # sticker = pygame.transform.rotate(sticker, -3)
    screen.blit(sticker, (800, 0))

    for i in range(2):
        text = get_font(30).render(lines[i], True, "black")
        if i == 0:
            screen.blit(text, (51, 401))
        else:
            screen.blit(text, (121, 431))

    for i in range(2):
        text = get_font(30).render(lines[i], True, "white")
        if i == 0:
            screen.blit(text, (50, 400))
        else:
            screen.blit(text, (120, 430))
    # הגדרות העמוד - הזזה ימינה
    pillar_width = 80  # צר יותר מהכפתורים
    button_start_y = 180  # התחלת אזור הכפתורים
    button_spacing = 20  # רווח בין הכפתורים
    right_margin = 150  # מרווח מהצד הימני של המסך

    # הגדרות הכפתורים
    button_heights = {"לחתה": 80, "תוארוה": 70, "תורדגה": 60, "האיצי": 50}

    # חישוב גובה העמוד בהתאם לכפתורים
    total_buttons_height = (
        sum(button_heights.values()) + (len(button_heights) - 1) * button_spacing
    )
    pillar_height = total_buttons_height + 40  # תוספת שוליים

    # מיקום חדש לעמוד - מימין
    pillar_x = 1080 - pillar_width - right_margin
    pillar_y = button_start_y - 20

    # ציור הצל של העמוד
    shadow_surface = pygame.Surface((pillar_width, pillar_height))
    shadow_surface.fill((30, 30, 30))
    shadow_surface.set_alpha(80)
    screen.blit(shadow_surface, (pillar_x + 8, pillar_y + 8))

    # ציור העמוד העץ
    pillar_surface = pygame.Surface((pillar_width, pillar_height))
    wood_color = (139, 90, 30)
    pillar_surface.fill(wood_color)

    # הוספת טקסטורת עץ
    for i in range(0, pillar_height, 15):
        wood_line_color = (101, 67, 33)
        pygame.draw.line(pillar_surface, wood_line_color, (0, i), (pillar_width, i), 2)
        for j in range(5):
            x = random.randint(0, pillar_width)
            pygame.draw.circle(pillar_surface, wood_line_color, (x, i), 2)

    pygame.draw.rect(
        pillar_surface, (101, 67, 33), (0, 0, pillar_width, pillar_height), 5
    )
    screen.blit(pillar_surface, (pillar_x, pillar_y))

    font_buttons = get_font(50)

    # סידור הכפתורים
    button_width_base = 300
    current_y = button_start_y
    buttons = {}

    for text, height in button_heights.items():
        width = button_width_base - (80 - height)
        # מיקום חדש לכפתורים - מימין
        x = pillar_x - (width - pillar_width) // 2
        buttons[text] = (x, current_y, width, height)
        current_y += height + button_spacing

    button_rects = {}

    # יצירת הכפתורים
    for text, (x, y, width, height) in buttons.items():
        btn_rect = pygame.Rect(x, y, width, height)

        # צל לכפתור
        shadow_rect = btn_rect.copy()
        shadow_rect.x += 4
        shadow_rect.y += 4
        pygame.draw.rect(screen, (60, 30, 0), shadow_rect, 0, 15)  # border_radius=15

        # רקע עץ לכפתור עם קצוות מעוגלים
        button_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        wood_button_color = (205, 133, 63)
        button_surface.fill((0, 0, 0, 0))
        pygame.draw.rect(
            button_surface, wood_button_color, (0, 0, width, height), border_radius=15
        )

        # מסכה עבור קצוות מעוגלים
        mask_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        mask_surface.fill((0, 0, 0, 0))
        pygame.draw.rect(
            mask_surface, (255, 255, 255, 255), (0, 0, width, height), border_radius=15
        )

        # טקסטורת עץ לכפתור (רק בתוך המסכה)
        texture_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        for i in range(0, height, 5):
            wood_line_color = (139, 69, 19)
            pygame.draw.line(texture_surface, wood_line_color, (0, i), (width, i), 1)
            for j in range(1):  # פחות עיגולים, שיהיה עדין
                xk = random.randint(10, width - 10)
                pygame.draw.circle(texture_surface, wood_line_color, (xk, i), 2)
        # החלת המסכה
        texture_surface.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        button_surface.blit(
            texture_surface, (0, 0), special_flags=pygame.BLEND_RGBA_ADD
        )

        screen.blit(button_surface, btn_rect)
        pygame.draw.rect(screen, (101, 67, 33), btn_rect, 3, 15)  # border_radius=15

        # הטקסט על הכפתור
        text_surface = font_buttons.render(text, True, "white")
        text_rect = text_surface.get_rect(center=btn_rect.center)
        screen.blit(text_surface, text_rect)

        button_rects[text] = btn_rect

    pygame.display.flip()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        cursor_set = False
        for btn_rect in button_rects.values():
            if btn_rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                cursor_set = True
                break
        if not cursor_set:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for text, btn_rect in button_rects.items():
                    if btn_rect.collidepoint(event.pos):
                        select_sound.play()
                        # Handle button actions here if needed
                        if text == "לחתה":
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                            start_music.stop()
                            if gen == "boy":
                                runScreen(0)
                            else:
                                runScreen(1)
                        elif text == "תוארוה":
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                            # tutorialScreen()
                        elif text == "תורדגה":
                            settings_screen()
                            return
                        elif text == "האיצי":
                            pygame.quit()

                        # ...add more actions for other buttons if needed...
        pygame.display.flip()
