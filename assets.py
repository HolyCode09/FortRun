# assets.py
import pygame
import os
pygame.init()

screen = pygame.display.set_mode((1080,520))
clock = pygame.time.Clock()

pygame.display.set_caption("המירוץ למבצר")
pygame.display.set_icon(pygame.image.load("pics/game_Icon.png"))

def soundsVol(volume, check):
    for mixer in sounds:
        if mixer[1] == "sound" and check == "sound":
            mixer[0].set_volume(volume)
        elif mixer[1] == "music" and check == "music":
            mixer[0].set_volume(volume)




# Asset loading helpers
def load_img(path, size=None):
    img = pygame.image.load(path)
    if size:
        img = pygame.transform.scale(img, size)
    return img

def load_sound(path):
    return pygame.mixer.Sound(path)

def load_font(path, size):
    return pygame.font.Font(path, size)

# Images
run_bg = load_img("pics/Run_Screen_Background.jpg", (1080,520))
paths_img = load_img("pics/paths1.png", (595,520))
paths_img2 = load_img("pics/paths2.png", (600,520))
player1_img = load_img("pics/Runner1.png", (130,170))
player2_img = load_img("pics/Runner2.png", (130,170))
before_run_window = load_img("pics/beforeRunPage.png", (1080,500))
start_bg = load_img("pics/Start_Screen_Background.jpg", (1080,520))
fortress_bg = load_img("pics/Fortres_Background.jpg", (1080,520))
dust_img = load_img("pics/Bluilding_Dust.png", (600,600))
forNow = load_img("pics/maps/forNow.png", (300,300))
goBack = load_img("pics/goBackIcon.png", (50,50))

# Sounds

go_sound = load_sound("sounds/GO.mp3")
bg_run_music = load_sound("sounds/Running_Background_Music.mp3")
lose_sound = load_sound("sounds/Lose_Sound.mp3")
collect_sound = load_sound("sounds/Collect.mp3")
hit_sound = load_sound("sounds/Hit_Sound.mp3")
drama_sound = load_sound("sounds/Enough_Mats_Check.mp3")
win_sound = load_sound("sounds/Win_Sound.mp3")
build_sound = load_sound("sounds/Building_Sound.mp3")
start_music = load_sound("sounds/Start_Screen_Background_Muisc.mp3")
select_sound = load_sound("sounds/select.mp3")

sounds = [
    (go_sound, "sound"),
    (bg_run_music, "music"),
    (lose_sound, "sound"),
    (collect_sound, "sound"),
    (hit_sound, "sound"),
    (drama_sound, "sound"),
    (win_sound, "sound"),
    (build_sound, "sound"),
    (start_music, "music"),
    (select_sound, "sound")
]

# Fonts
def get_font(size):
    return load_font("ganclm_bold-webfont.woff", size)