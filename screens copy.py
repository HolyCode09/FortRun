
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

    matsStack = load_img("pics/miniStacks/matsStack.png", (20, 20))
    foodStack = load_img("pics/miniStacks/foodStack.png", (20, 20))
    toysStack = load_img("pics/miniStacks/toysStack.png", (20, 20))
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
        matsCollectedStack = [matsStack] * matsCount + [grayMatsStack] * (
            10 - matsCount
        )
        foodCollectedStack = [foodStack] * foodCount + [grayFoodStack] * (
            10 - foodCount
        )
        toysCollectedStack = [toysStack] * toysCollected + [grayToysStack] * (
            3 - toysCollected
        )
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
            return
        if x_player == 285:
            colideHappen(285)
        elif x_player == 485:
            colideHappen(485)
        else:
            colideHappen(680)
        pygame.display.flip()


