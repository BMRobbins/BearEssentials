import pygame, sys, time, random
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 1300
WINDOWHEIGHT = 650
CHOICE = 'mainmenu'

#Color
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
GREEN = (0, 255,0)



def load_main_menu_images():
    global LOGO
    #Mainmenu
    LOGO = pygame.image.load('logo.png')

def load_end_game_images():
    global YOUWIN, YOULOSE
    #End Game
    YOUWIN = pygame.image.load('youwin.png')
    YOULOSE = pygame.image.load('youlose.png')

def load_background_images():
    global BACKROUND
    #BACKROUND
    BACKROUND = pygame.image.load('backround.png')

def load_bear_animation_images():
    global BEARRESTRIGHT, BEARRESTRIGHTHALFBLINK, BEARRESTRIGHTFULLBLINK, BEARRESTLEFT, BEARRESTLEFTHALFBLINK, BEARRESTLEFTFULLBLINK, BEARMOVERIGHT1, BEARMOVERIGHT2, BEARMOVERIGHT3, BEARMOVELEFT1 ,\
        BEARMOVELEFT2,BEARMOVELEFT3               
    #bear resting right position and blink
    BEARRESTRIGHT = pygame.image.load('bearRestRight.png')
    BEARRESTRIGHTHALFBLINK = pygame.image.load('bearRestRightHalfBlink.png')
    BEARRESTRIGHTFULLBLINK = pygame.image.load('bearRestRightFullBlink.png')

    #bear resting left position and blink
    BEARRESTLEFT = pygame.image.load('bearRestLeft.png')
    BEARRESTLEFTHALFBLINK = pygame.image.load('bearRestLeftHalfBlink.png')
    BEARRESTLEFTFULLBLINK = pygame.image.load('bearRestLeftFullBlink.png')

    #bear moving right images
    BEARMOVERIGHT1 = pygame.image.load('bearMoveRight1.png')
    BEARMOVERIGHT2 = pygame.image.load('bearMoveRight2.png')
    BEARMOVERIGHT3 = pygame.image.load('bearMoveRight3.png')

    #bear moving right images
    BEARMOVELEFT1 = pygame.image.load('bearMoveLeft1.png')
    BEARMOVELEFT2 = pygame.image.load('bearMoveLeft2.png')
    BEARMOVELEFT3 = pygame.image.load('bearMoveLeft3.png')

#this is where the pygame init was earlier
def add_fruit_and_rock_images():
    global APPLE, BANANA, ORANGE, CHERRY, ROCK, LIFE
    #fruit images
    APPLE = pygame.image.load('apple.png')
    BANANA = pygame.image.load('banana.png')
    ORANGE = pygame.image.load('orange.png')
    CHERRY = pygame.image.load('cherry.png')

    #Rock image
    ROCK = pygame.image.load('rock.png')

    #Life image
    LIFE = pygame.image.load('life.png')

def add_music_and_sound():
    global FAILURE, CHOMP, WALK, WALK2
    #Music
    pygame.mixer.music.load('gamemusic.ogg')
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(loops = 1000)

    #Sound
    FAILURE= pygame.mixer.Sound('failure.wav')
    CHOMP = pygame.mixer.Sound('chomp.ogg')
    WALK = pygame.mixer.Sound('walk.wav')
    WALK2 = pygame.mixer.Sound('walk2.wav')

def load_buttons():
    global fontObj, PLAY, QUITBUTTON, PLAY2, QUITBUTTON2
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    PLAY = button(pygame.image.load('play.png'), pygame.image.load('play1.png'), 550, 400, 180, 64)
    QUITBUTTON = button(pygame.image.load('quit.png'), pygame.image.load('quit1.png'), 550, 475, 180, 64)
    PLAY2 = button(pygame.image.load('playagain.png'), pygame.image.load('playagain1.png'), 550, 350, 180, 64)
    QUITBUTTON2 = button(pygame.image.load('quit.png'), pygame.image.load('quit1.png'), 550, 425, 180, 64)
    
def load_all_images_and_sound():
    global LOGO, YOUWIN, YOULOSE, BACKROUND,BEARRESTRIGHT, BEARRESTRIGHTHALFBLINK, BEARRESTRIGHTFULLBLINK, BEARRESTLEFT, BEARRESTLEFTHALFBLINK, BEARRESTLEFTFULLBLINK, BEARMOVERIGHT1, BEARMOVERIGHT2, BEARMOVERIGHT3, BEARMOVELEFT1 ,\
        BEARMOVELEFT2,BEARMOVELEFT3, APPLE, BANANA, ORANGE, CHERRY, ROCK, LIFE, FAILURE, CHOMP, WALK, WALK2,fontObj
    load_main_menu_images()
    load_end_game_images()
    load_background_images()
    load_bear_animation_images()
    add_fruit_and_rock_images()
    add_music_and_sound()
    load_buttons() 
    
def set_game_display_up():
    global TIME, FPSCLOCK, DISPLAYSURF, MrBear, FRUITLIST, ROCKLIST, GAMESTATE
    TIME = Timer()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Silly Bear')
    DISPLAYSURF.fill(WHITE)
    MrBear = bear(30, WINDOWHEIGHT - 160)
    FRUITLIST = [fruit()]
    ROCKLIST = [rock(),rock(),rock()]
    GAMESTATE = gamestate()

def handle_command_mainmenu():
    global CHOICE, QUIT, PLAY, QUITBUTTON, GAMESTATE, FPSCLOCK
    while CHOICE == 'mainmenu':
        for event in pygame.event.get():
            if event.type == QUIT or (event.type== KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse = event.pos
                if PLAY.mouse_click_on_button(mouse):
                    PLAY.highlight_button_color()
                else:
                    PLAY.orig_button_color()
                if QUITBUTTON.mouse_click_on_button(mouse):
                    QUITBUTTON.highlight_button_color()
                else:
                    QUITBUTTON.orig_button_color()
            elif event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                if PLAY.mouse_click_on_button(mouse):
                    PLAY.update_keydown()
                elif QUITBUTTON.mouse_click_on_button(mouse):
                    QUITBUTTON.update_keydown()
            elif event.type ==  MOUSEBUTTONUP:
                mouse = event.pos
                if PLAY.mouse_click_on_button(mouse):
                    PLAY.update_keyup()
                    CHOICE = 'game'
                elif QUITBUTTON.mouse_click_on_button(mouse):
                    QUITBUTTON.update_keyup()
                    pygame.quit()
                    sys.exit()
            elif event.type == KEYUP:
                if event.key == K_m:
                    GAMESTATE.toggle_music()
                    if GAMESTATE.is_music_on():
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                    
        drawmainmenu()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def handle_command_game():
    global CHOICE, MrBear, BEARRESTRIGHT, BEARRESTLEFT, GAMESTATE, FPSCLOCK, FRUITLIST, ROCKLIST
    while CHOICE == 'game':
        for event in pygame.event.get():
            if event.type == QUIT or (event.type== KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    MrBear.change_move('RIGHT')
                elif event.key == K_LEFT:
                    MrBear.change_move('LEFT')

            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    MrBear.change_image(BEARRESTRIGHT)
                    MrBear.change_move(None)
                elif event.key == K_LEFT:
                    MrBear.change_image(BEARRESTLEFT)
                    MrBear.change_move(None)
                elif event.key == K_m:
                    GAMESTATE.toggle_music()
                    if GAMESTATE.is_music_on():
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                elif event.key == K_p:
                    GAMESTATE.toggle_pause()

                    while GAMESTATE.is_paused():
                        for event in pygame.event.get():
                            if event.type == KEYUP:
                                if event.key == K_p:
                                    GAMESTATE.toggle_pause()
                                

                
        drawboard()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        if GAMESTATE.time_for_fruit():
            FRUITLIST.append(fruit())
        if GAMESTATE.time_for_rock():
            ROCKLIST.append(rock())

def handle_command_endgame():
    global CHOICE, PLAY2, QUITBUTTON2, GAMESTATE, FPSCLOCK
    while CHOICE == 'endgame':
        for event in pygame.event.get():
            if event.type == QUIT or (event.type== KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse = event.pos
                if PLAY2.mouse_click_on_button(mouse):
                    PLAY2.highlight_button_color()
                else:
                    PLAY2.orig_button_color()
                if QUITBUTTON2.mouse_click_on_button(mouse):
                    QUITBUTTON2.highlight_button_color()
                else:
                    QUITBUTTON2.orig_button_color()
            elif event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                if PLAY2.mouse_click_on_button(mouse):
                    PLAY2.update_keydown()
                elif QUITBUTTON2.mouse_click_on_button(mouse):
                    QUITBUTTON2.update_keydown()
            elif event.type ==  MOUSEBUTTONUP:
                mouse = event.pos
                if PLAY2.mouse_click_on_button(mouse):
                    PLAY2.update_keyup()
                    CHOICE = 'game'
                    main()
                elif QUITBUTTON2.mouse_click_on_button(mouse):
                    QUITBUTTON2.update_keyup()
                    pygame.quit()
                    sys.exit()

            elif event.type == KEYUP:
                if event.key == K_m:
                    GAMESTATE.toggle_music()
                    if GAMESTATE.is_music_on():
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                

                    
        drawendmenu()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def main():
    global FPSCLOCK, DISPLAYSURF, MrBear, FRUITLIST, GAMESTATE, ROCKLIST, TIME, CHOICE, PLAY, QUITBUTTON, PLAY2, QUITBUTTON2, LOGO, YOUWIN, YOULOSE, BACKROUND,BEARRESTRIGHT, BEARRESTRIGHTHALFBLINK, BEARRESTRIGHTFULLBLINK, BEARRESTLEFT, BEARRESTLEFTHALFBLINK, BEARRESTLEFTFULLBLINK, BEARMOVERIGHT1, BEARMOVERIGHT2, BEARMOVERIGHT3, BEARMOVELEFT1 ,\
        BEARMOVELEFT2,BEARMOVELEFT3, APPLE, BANANA, ORANGE, CHERRY, ROCK, LIFE, FAILURE, CHOMP, WALK, WALK2, fontObj
    pygame.init()
    load_all_images_and_sound()
    set_game_display_up()

    if CHOICE == 'mainmenu':
        handle_command_mainmenu()
    if CHOICE == 'game':
        handle_command_game()
    if CHOICE == 'endgame':
        handle_command_endgame()

        
    
        



def drawendmenu():
    global fontObj
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(BACKROUND, (0,0))
    result = GAMESTATE.get_win_or_lose()
    if result == 'lose':
        DISPLAYSURF.blit(YOULOSE, (380, 200))
    else:
        DISPLAYSURF.blit(YOUWIN, (400, 200))

    ScoreSurfaceObj = fontObj.render('Score = ' + str(GAMESTATE.get_score()), True, BLACK, BLUE)
    ScoreRectObj = ScoreSurfaceObj.get_rect()
    ScoreRectObj.center = (WINDOWWIDTH - 200, 40)
    DISPLAYSURF.blit(ScoreSurfaceObj, ScoreRectObj)
        
    PLAY2.draw()
    QUITBUTTON2.draw()
    
def drawmainmenu():
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(BACKROUND, (0,0))
    DISPLAYSURF.blit(LOGO, (300, 200))
    PLAY.draw()
    QUITBUTTON.draw()
    
    
    
def drawboard_background_and_bear():
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(BACKROUND, (0,0))
    MrBear.draw()

def drawboard_time():
    global fontObj, TimeSurfaceObj, TimeRectObj
    TIME.update()
    TimeSurfaceObj = fontObj.render('Time = '+ TIME.get_time(), True, BLACK, BLUE)
    TimeRectObj = TimeSurfaceObj.get_rect()
    TimeRectObj.center = (WINDOWWIDTH - 200, 80)
    DISPLAYSURF.blit(TimeSurfaceObj, TimeRectObj)

def drawboard_level():
    global LevelSurfaceObj, LevelRectObj
    LevelSurfaceObj = fontObj.render('Level = '+ str(GAMESTATE.get_level()), True, BLACK, BLUE)
    LevelRectObj = TimeSurfaceObj.get_rect()
    LevelRectObj.center = (WINDOWWIDTH - 160, 120)
    DISPLAYSURF.blit(LevelSurfaceObj, LevelRectObj)

def drawboard_score():
    global ScoreSurfaceObj, ScoreRectObj, ScoreRectObj
    ScoreSurfaceObj = fontObj.render('Score = ' + str(GAMESTATE.get_score()), True, BLACK, BLUE)
    ScoreRectObj = ScoreSurfaceObj.get_rect()
    ScoreRectObj.center = (WINDOWWIDTH - 200, 40)
    DISPLAYSURF.blit(ScoreSurfaceObj, ScoreRectObj)

def drawboard_fruit():
    for item in FRUITLIST:
        item.draw()
        item.update()
        if item.check_to_delete():
            FRUITLIST.remove(item)
        ItemRect = item.determine_rect_dimensions()
        if BearRect.colliderect(ItemRect):
            CHOMP.play()
            FRUITLIST.remove(item)
            GAMESTATE.update_score(10)

def drawboard_rock():
    global CHOICE
    for item in ROCKLIST:
        item.draw()
        item.update()
        if item.check_to_delete():
            ROCKLIST.remove(item)
        ItemRect = item.determine_rect_dimensions()
        if BearRect.colliderect(ItemRect):
            FAILURE.play()
            time.sleep(1)
            GAMESTATE.update_lives()
            ROCKLIST.remove(item)
        if  GAMESTATE.get_lives() <= 0:
            GAMESTATE.set_win_or_lose('lose')
            CHOICE = 'endgame'

def drawboard():
    global CHOICE, fontObj, BearRect
    drawboard_background_and_bear()
    drawboard_time()
    drawboard_level()
    drawboard_score() 
    GAMESTATE.draw_lives()
    BearRect = MrBear.determine_rect_dimensions()
    drawboard_fruit()
    drawboard_rock() 

class bear():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.speed = 10
        self.image = BEARRESTRIGHT
        self.blinktime = 5
        self.time = time.time()
        self.blinkingRight = [BEARRESTRIGHTHALFBLINK, BEARRESTRIGHTFULLBLINK, BEARRESTRIGHTHALFBLINK, BEARRESTRIGHT]
        self.blinkingLeft = [BEARRESTLEFTHALFBLINK, BEARRESTLEFTFULLBLINK, BEARRESTLEFTHALFBLINK, BEARRESTLEFT]
        self.movingRight = [BEARMOVERIGHT2,BEARMOVERIGHT3,BEARMOVERIGHT2,BEARMOVERIGHT1,BEARMOVERIGHT2]
        self.moveRightIndex = 0
        self.movingLeft = [BEARMOVELEFT2,BEARMOVELEFT3,BEARMOVELEFT2,BEARMOVELEFT1,BEARMOVELEFT2]
        self.moveLeftIndex = 0
        self.blinkindex = 0
        self.move = None
        self.direction = 'RIGHT'

    def draw(self):
        if self.move == 'RIGHT':
            self.move_right_animation()
            self.direction ='RIGHT'

        elif self.move == 'LEFT':
            self.move_left_animation()
            self.direction = 'LEFT'
            
        elif time.time() - self.time > self.blinktime:
            self.blinkanimation()
            
        else:
            DISPLAYSURF.blit(self.image, (self.x, self.y))

    def change_image(self,image):
        self.image = image

    def blinkanimation(self):
        if self.blinkindex == 0:
            if self.direction == 'RIGHT':
                self.change_image(self.blinkingRight[self.blinkindex])
            else:
                self.change_image(self.blinkingLeft[self.blinkindex])
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.blinkindex +=1

        elif self.blinkindex == 1:
            if self.direction == 'RIGHT':
                self.change_image(self.blinkingRight[self.blinkindex])
            else:
                self.change_image(self.blinkingLeft[self.blinkindex])
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.blinkindex +=1

        elif self.blinkindex == 2:
            if self.direction == 'RIGHT':
                self.change_image(self.blinkingRight[self.blinkindex])
            else:
                self.change_image(self.blinkingLeft[self.blinkindex])
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.blinkindex +=1

        else:
            if self.direction == 'RIGHT':
                self.change_image(self.blinkingRight[self.blinkindex])
            else:
                self.change_image(self.blinkingLeft[self.blinkindex])
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.blinkindex = 0
            self.time = time.time()

    def move_right_animation(self):
        if self.moveRightIndex == 0:
            self.change_image(self.movingRight[self.moveRightIndex])
            self.change_x()
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.moveRightIndex +=1

        elif self.moveRightIndex == 1:
            WALK.play()
            self.change_image(self.movingRight[self.moveRightIndex])
            self.change_x()
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.moveRightIndex +=1

        elif self.moveRightIndex == 2:
            self.change_image(self.movingRight[self.moveRightIndex])
            self.change_x()
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.moveRightIndex +=1

        elif self.moveRightIndex == 3:
            self.change_image(self.movingRight[self.moveRightIndex])
            self.change_x()
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.moveRightIndex +=1

        else:
            WALK2.play()
            self.change_image(self.movingRight[self.moveRightIndex])
            self.change_x()
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.moveRightIndex = 1

    def move_left_animation(self):
        if self.moveLeftIndex == 0:
            self.change_image(self.movingLeft[self.moveLeftIndex])
            self.change_x()
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.moveLeftIndex +=1

        elif self.moveLeftIndex == 1:
            WALK.play()
            self.change_image(self.movingLeft[self.moveLeftIndex])
            self.change_x()
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.moveLeftIndex +=1

        elif self.moveLeftIndex == 2:
            self.change_image(self.movingLeft[self.moveLeftIndex])
            self.change_x()
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.moveLeftIndex +=1

        elif self.moveLeftIndex == 3:
            self.change_image(self.movingLeft[self.moveLeftIndex])
            self.change_x()
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.moveLeftIndex +=1

        else:
            WALK2.play()
            self.change_image(self.movingLeft[self.moveLeftIndex])
            self.change_x()
            DISPLAYSURF.blit(self.image, (self.x, self.y))
            self.moveLeftIndex = 1

    def determine_rect_dimensions(self):
        return pygame.Rect(self.x,self.y, 87, 149)

    def change_x(self):
        if self.move == 'RIGHT':
            if self.x < WINDOWWIDTH - 87:
                self.x += self.speed

        elif self.move == 'LEFT':
            if self.x > 0:
                self.x -= self.speed
            


    def change_move(self, move):
        self.move = move
        
            
            
class fruit():
    def __init__(self):
        self.possible = [APPLE,BANANA,ORANGE,CHERRY]
        self.fruit = random.choice(self.possible)
        self.y = 0
        self.x = random.randint(50, WINDOWWIDTH - 50)
        self.time = time.time()
        self.timeout = .2
        self.speed = 10
        self.delete = False
    def determine_rect_dimensions(self):
        if self.fruit == APPLE:
            rect = pygame.Rect(self.x,self.y, 50, 53)
        elif self.fruit == BANANA:
            rect = pygame.Rect(self.x,self.y, 50, 85)
        elif self.fruit == CHERRY:
            rect = pygame.Rect(self.x,self.y,50, 50)
        else:
            rect = pygame.Rect(self.x,self.y, 50, 60)
        return rect
            
    def draw(self):
        DISPLAYSURF.blit(self.fruit, (self.x, self.y))

    def update(self):
        if time.time() - self.time > self.timeout:
            self.y += self.speed
            self.time = time.time()
            if self.y > WINDOWHEIGHT:
                self.delete = True
            
    def check_to_delete(self):
        return self.delete

class rock():
    def __init__(self):
        self.image = ROCK
        self.y = 0
        self.x = random.randint(50, WINDOWWIDTH - 50)
        self.time = time.time()
        self.timeout = .1
        self.speed = 20
        self.delete = False

    def draw(self):
        DISPLAYSURF.blit(self.image, (self.x, self.y))
    def determine_rect_dimensions(self):
        return pygame.Rect(self.x,self.y, 50,41)

    def update(self):
        if time.time() - self.time > self.timeout:
            self.y += self.speed
            self.time = time.time()
            if self.y > WINDOWHEIGHT:
                self.delete = True
            
    def check_to_delete(self):
        return self.delete
    

class gamestate():
    def __init__(self):
        self.score = 0
        self.starttime = time.time()
        self.lastfruit = time.time()
        self.lastrock = time.time()
        self.fruitTimeOut = 10
        self.rockTimeOut = 5
        self.lives = 5
        self.level = 1
        self.WinOrLose = 'win'
        self.MusicOn = True
        self.Pause = False
    def toggle_pause(self):
        if self.Pause == True:
            self.Pause = False
        else:
            self.Pause = True

    def is_paused(self):
        return self.Pause
                
    def toggle_music(self):
        if self.MusicOn == True:
            self.MusicOn = False
        else:
            self.MusicOn = True
            
    def is_music_on(self):
        return self.MusicOn

    def time_for_fruit(self):
        global CHOICE
        if time.time() - self.starttime > 60:
            self.starttime = time.time()
            self.fruitTimeOut -= 1
            self.rockTimeOut -= .5
            self.level += 1
            if self.fruitTimeOut <= 0:
                CHOICE = 'endgame'
        if time.time() - self.lastfruit > self.fruitTimeOut:
            self.lastfruit = time.time()
            return True
        return False

    def time_for_rock(self):
        if time.time() - self.lastrock > self.rockTimeOut:
            self.lastrock = time.time()
            return True
        return False

    def get_score(self):
        return self.score

    def update_score(self, points):
        self.score += points

    def update_lives(self):
        self.lives -= 1


    def get_level(self):
        return self.level

    def draw_lives(self):
        if self.lives == 5:
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 300, 140))
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 260, 140))
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 220, 140))
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 180, 140))
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 140, 140))
        elif self.lives == 4:
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 300, 140))
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 260, 140))
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 220, 140))
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 180, 140))
      
        elif self.lives == 3:
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 300, 140))
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 260, 140))
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 220, 140))

        elif self.lives == 2:
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 300, 140))
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 260, 140))

        elif self.lives == 1:
            DISPLAYSURF.blit(LIFE,(WINDOWWIDTH - 300, 140))

    def get_lives(self):
        return self.lives

    def set_win_or_lose(self, result):
        self.WinOrLose = result

    def get_win_or_lose(self):
        return self.WinOrLose
        

class Timer():
    def __init__(self):
        self.sec = 0
        self.min = 0
        self.origtime = time.time()

    def update(self):
        self.min = (time.time() - self.origtime) // 60
        self.sec = (time.time() - self.origtime) % 60

    def get_time(self):
        if self.min < 10:
            minute = '0' + str(int(self.min))
        else:
            minute = str(int(self.min))

        if self.sec < 10:
            second = '0' + str(int(self.sec))

        else:
            second = str(int(self.sec))

        return minute + ' : ' + second

class button():
    def __init__(self, buttonimage, highlightimage, x, y, width, height, sound = None):
        self.buttonimage = buttonimage
        self.highlightimage = highlightimage
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.image = buttonimage
        self.yd = 5
        self.sound = sound
        

    def draw(self):
        if self.sound:
            self.sound.play()
        DISPLAYSURF.blit(self.image, (self.x, self.y))

    def update_keydown(self):
        self.y += self.yd

    def update_keyup(self):
        self.y -= self.yd

    def highlight_button_color(self):
        self.image = self.highlightimage

    def orig_button_color(self):
        self.image = self.buttonimage

    def mouse_click_on_button(self, mouseclick):
        return mouseclick[0] >= self.x and mouseclick[0] <= self.x + self.width and mouseclick[1] >=  self.y and mouseclick[1] <= self.y  + self.height
    
    
    

    
        
            
if __name__ == '__main__':
    main()
