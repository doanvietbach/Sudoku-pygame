import pygame
from Game.Scenes.Scene import Scene
from Game.Board.Board import Board
from Game.Shared.GameConstants import GameConstants

import speech_recognition as sr
import time as Time

SPEECH_DIGIT = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bẩy', 'tám', 'chín']


class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

        self.game = game
        self.run = 0
        self.screen = pygame.display.set_mode()
        self.counter = 0
        self.time = ''
        self.mouse = []
        self.key = 0
        self.score = None

        pygame.time.set_timer(pygame.USEREVENT, 1000)

        self.__playSprite2 = pygame.image.load(GameConstants.SPRITE_PLAY)

        # self.__rowLabelSprites = []
        # for i in range(9):
        #     self.__rowLabelSprites.append()
        #
        #
        # self.__colLabelSprites = []

    def render(self):
        super(PlayingGameScene, self).render()

        self.getGame().screen.blit(self.__playSprite2, (650, 350))

        game = self.getGame()

        puzzle = Board.tiles(self)

        if self.key == 0 and len(self.mouse) == 0:
            PlayingGameScene.makeboard(self, game, puzzle)
            self.run += 1
        else:
            key = self.key
            x = self.mouse[0]
            y = self.mouse[1]
            if puzzle[x][y] == 0:
                puzzle[x][y] = key
                self.key = 0
                PlayingGameScene.makeboard(self, game, puzzle, selected=(x, y))
            else:
                PlayingGameScene.makeboard(self, game, puzzle, selected=(x, y))

        self.clearText()

        for i in range(9):
            self.addText(str(i), 85 + GameConstants.TILE_SIZE[0] * i, 0, size=50)

        for i in range(9):
            self.addText(chr(ord('A') + i), 10, 85 + GameConstants.TILE_SIZE[1] * i, size=50)

    def setscore(self):
        puzzle = self.unsolve
        score = Board.checkboard(self, puzzle)
        return score

    def storetime(self, time):
        self.time = time

    def gettime(self):
        return self.time

    def displaybox(self, screen):
        pygame.draw.rect(self.screen, (86, 47, 14), [50, 50, 500, 500], 25)

    def makeboard(self, game, puzzle, selected=None):
        bag = []
        for i in range(0, 9):
            for j in range(0, 9):
                num = puzzle[i][j]
                if num == 0 and selected == (i, j):
                    name = GameConstants.TILE_PATH + '/Selected.jpg'
                else:
                    name = GameConstants.TILE_PATH + '/' + str(num) + '.jpg'
                bag.append(name)

        numbers = []
        for i in range(0, len(bag)):
            board = pygame.image.load(bag[i])
            numbers.append(board)
        n = 0
        for i in range(0, 9):
            for j in range(0, 9):
                game.screen.blit(numbers[n], (75 + GameConstants.TILE_SIZE[0] * i, 75 + GameConstants.TILE_SIZE[1] * j))
                n = n + 1

    def clock(self, text):
        time = ''
        if text >= 60:
            min = int(text / 60)
            sec = int(text - min * 60)
            time = str(min) + str(':') + str(sec)
            return time
        else:
            time = '0' + ':' + str(text)
            return time

    def cursor(self, pos):
        x = int(pos[0])
        y = int(pos[1])
        if (x > 75 and x < 525) and (y > 75 and y < 525):
            i = (x - 75) / 50
            j = (y - 75) / 50
            print(int(i), int(j))
            return (int(i), int(j))
        else:
            return pos

    def keyboard(self, key):
        if key == 256 or key == 48:
            flag = 0
        if key == 257 or key == 49:
            flag = 1
        if key == 258 or key == 50:
            flag = 2
        if key == 259 or key == 51:
            flag = 3
        if key == 260 or key == 52:
            flag = 4
        if key == 261 or key == 53:
            flag = 5
        if key == 262 or key == 54:
            flag = 6
        if key == 263 or key == 55:
            flag = 7
        if key == 264 or key == 56:
            flag = 8
        if key == 265 or key == 57:
            flag = 9
        return flag

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
                Board.newboard()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                if mouse[0] == 1:
                    point = PlayingGameScene.cursor(self, pos)
                    self.getGame().playSound(GameConstants.SOUND_CLICK)
                    self.mouse = point

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.getGame().changeScene(GameConstants.MENU_SCENE)

                if event.key == pygame.K_F1:
                    self.getGame().changeScene(GameConstants.MENU_SCENE)

                if event.key == pygame.K_F2:
                    test = PlayingGameScene.setscore(self)
                    if test == True:
                        self.getGame().changeScene(GameConstants.SAVING_SCENE)
                    else:
                        self.getGame().playSound(GameConstants.SOUND_GAMEOVER)
                        self.getGame().changeScene(GameConstants.GAMEOVER_SCENE)

                if event.key == pygame.K_F4:
                    exit()

                key = event.key

                if (key >= 48 and key <= 57) or (key >= 256 and key <= 265):
                    final = PlayingGameScene.keyboard(self, key)
                else:
                    final = 0

                self.key = final

                if event.key == pygame.K_SPACE:
                    print('start_listening')
                    self.getGame().playSound(GameConstants.SOUND_BELL)

                    r = sr.Recognizer()
                    m = sr.Microphone()
                    with m as source:
                        r.adjust_for_ambient_noise(source)
                    stop_listening = r.listen_in_background(m, self.voice_callback)
                    Time.sleep(4)
                    stop_listening()
                    print('stop_listening')
                    self.getGame().playSound(GameConstants.SOUND_BELL)

            if event.type == pygame.USEREVENT:
                self.counter += 1
                text = str(self.counter)
                text1 = int(text)

                time = PlayingGameScene.clock(self, text1)
                # self.addText(time, x=700, y=175, size=50)
                game = self.getGame()
                game.setTime(time)

    def voice_callback(self, recognizer, audio):
        print(self)
        try:
            s = recognizer.recognize_google(audio, language="vi-VN")
            print("Google Speech Recognition thinks you said " + s)

            self.key, self.mouse = getCommand(s)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def getVal(s):
    val = 0

    print(s)

    if s.lower() in SPEECH_DIGIT:
        val = SPEECH_DIGIT.index(s.lower())
    elif s.lower() == 'bảy':
        val = 7
    elif s.lower().isnumeric():
        val = int(s)

    return val

def findInd(arr):

    if len(arr) == 0:
        return [0, 0]

    if len(arr) == 1:
        s = arr[0]
        col = int(s[1])
        if s[0].lower() == 'y':
            row = ord('i') - ord('a')
        else:
            row = ord(s[0].lower()) - ord('a')

        return [col, row]
    else:
        s = arr[0]

        if s[0].lower() == 'y':
            row = ord('i') - ord('a')
        else:
            row = ord(s[0].lower()) - ord('a')

        col = getVal(arr[1])

        return [col, row]

def getCommand(s):
    split = s.split(' ')

    print(split)

    if split[0].lower() == 'điền' or split[0].lower() == 'đặt':
        val = getVal(split[1])

        if len(split) >= 4:
            pos = findInd(split[3:])
            print(val, pos)
            return val, pos
    elif split[0].lower().isnumeric():
        val = getVal(split[0])

        if len(split) >= 3:
            pos = findInd(split[2:])
            print(val, pos)
            return val, pos
    elif split[0].lower() in SPEECH_DIGIT or split[0].lower() == 'bảy':
        val = getVal(split[0])

        if len(split) >= 3:
            pos = findInd(split[2:])
            print(val, pos)
            return val, pos

    return 0, [0, 0]
