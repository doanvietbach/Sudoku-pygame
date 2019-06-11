import os


class GameConstants:
    SCREEN_SIZE = (900, 600)
    CURSOR_SIZE = (50, 50)
    TILE_SIZE = (50, 50)

    TILE_PATH = os.path.join("Game/Assets", "Digits")

    SPRITE_MENU = os.path.join("Game/Assets", "Menu.jpg")
    SPRITE_MAINMENU = os.path.join("Game/Assets", "MainMenu.png")
    SPRITE_PLAY = os.path.join("Game/Assets", "Play.png")
    SPRITE_CLOCK = os.path.join("Game/Assets", "Clock.png")
    SPRITE_PRIZE = os.path.join("Game/Assets", "Prize.png")
    SPRITE_STAND = os.path.join("Game/Assets", "Stand.png")
    SPRITE_INSTRUCTION = os.path.join("Game/Assets", "Instruction.png")
    SPRITE_GAMEOVER = os.path.join("Game/Assets", "Gameover.png")
    SPRITE_HIGHSCORE = os.path.join("Game/Assets", "Highscore.png")
    SPRITE_CONGRATS = os.path.join("Game/Assets", "Congrats.png")
    SPRITE_SAD_1 = os.path.join("Game/Assets", "Sad_1.png")
    SPRITE_SAD_2 = os.path.join("Game/Assets", "Sad_2.png")
    SPRITE_WON = os.path.join("Game/Assets", "Won.png")


    SOUND_FILE_CLICK = os.path.join("Game/Assets", "Click.wav")
    SOUND_FILE_GAMEOVER = os.path.join("Game/Assets", "Gameover.wav")
    SOUND_FILE_SCREEN = os.path.join("Game/Assets", "Screen.wav")
    SOUND_FILE_BELL = os.path.join("Game/Assets", "Bell.wav")

    SOUND_CLICK = 0
    SOUND_GAMEOVER = 1
    SOUND_SCREEN = 2
    SOUND_BELL = 3

    PLAYING_SCENE = 0
    HIGHSCORE_SCENE = 1
    MENU_SCENE = 2
    INSTRUCTION = 3
    GAMEOVER_SCENE = 4
    SAVING_SCENE = 5
