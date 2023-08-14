# Program Name: Fast Fishing
# Purpose: Purpose of program is for user to play a fishing game on desired difficulty
# Inputs: Difficulty, and speed of targets being clicked
# Outputs: Change in time gap based on difficulty, and checking whether or not fish caught



import random, pygame, time
from pygame import *
from pygame import time

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

# Background
gamebackground = pygame.image.load('lake.jpeg')
insbackground = pygame.image.load('black.jpeg')

# Sound
mixer.music.load("peace.mp3")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Fishing")
icon = pygame.image.load('salmon.png')
pygame.display.set_icon(icon)

# Ripples
playerX = random.randint(400, 600) # x coordinate
playerY = random.randint(250, 400) # y coordinate
playerImg = pygame.image.load('ripple.png') # loads image of ripple
playerImg_rect = pygame.Rect(playerX, playerY, 64, 64)  # defines rectangle for clicking


playerX2 = random.randint(400, 850)
playerY2 = random.randint(250, 400)
playerImg2 = pygame.image.load('ripple.png')
playerImg2_rect = pygame.Rect(playerX2, playerY2, 64, 64)


playerX3 = random.randint(400, 850)
playerY3 = random.randint(250, 400)
playerImg3 = pygame.image.load('ripple.png')
playerImg3_rect = pygame.Rect(playerX3, playerY3, 64, 64)


playerX4 = random.randint(400, 850)
playerY4 = random.randint(250, 400)
playerImg4 = pygame.image.load('ripple.png')
playerImg4_rect = pygame.Rect(playerX4, playerY4, 64, 64)


playerX5 = random.randint(400, 850)
playerY5 = random.randint(250, 400)
playerImg5 = pygame.image.load('ripple.png')
playerImg5_rect = pygame.Rect(playerX5, playerY5, 64, 64)

# Puts ripples onto screen:
def ripple():
    playerImg = pygame.image.load('ripple.png') # loads ripple image
    playerImg = pygame.transform.scale(playerImg, (64, 64)) # scales down image to 64x64px
    screen.blit(playerImg, (playerX, playerY)) # puts ripple on screen with x and y coordinate


def ripple2():
    playerImg2 = pygame.image.load('ripple.png')
    playerImg2 = pygame.transform.scale(playerImg2, (64, 64))
    screen.blit(playerImg2, (playerX2, playerY2))


def ripple3():
    playerImg3 = pygame.image.load('ripple.png')
    playerImg3 = pygame.transform.scale(playerImg3, (64, 64))
    screen.blit(playerImg3, (playerX3, playerY3))


def ripple4():
    playerImg4 = pygame.image.load('ripple.png')
    playerImg4 = pygame.transform.scale(playerImg4, (64, 64))
    screen.blit(playerImg4, (playerX4, playerY4))


def ripple5():
    playerImg5 = pygame.image.load('ripple.png')
    playerImg5 = pygame.transform.scale(playerImg5, (64, 64))
    screen.blit(playerImg5, (playerX5, playerY5))

# Targets
target1 = pygame.image.load('target.png')  # loads target image
target2 = pygame.image.load('target.png')
target3 = pygame.image.load('target.png')


target4 = pygame.image.load('target.png')
target5 = pygame.image.load('target.png')
target6 = pygame.image.load('target.png')

target7 = pygame.image.load('target.png')
target8 = pygame.image.load('target.png')
target9 = pygame.image.load('target.png')

# X and Y coordinates of each target
target1X = playerX + random.randint(50, 100)  # x coordinate of target
target1Y = playerY + random.randint(50, 100)  # y coordinate of target
target2X = target1X + random.randint(50, 100)
target2Y = target1Y + random.randint(50, 100)
target3X = target2X + random.randint(50, 100)
target3Y = target2Y + random.randint(50, 100)

target4X = playerX2 - random.randint(50, 100)
target4Y = playerY2 - random.randint(50, 100)
target5X = target4X - random.randint(50, 100)
target5Y = target4Y - random.randint(50, 100)
target6X = target5X - random.randint(50, 100)
target6Y = target5Y - random.randint(50, 100)

target7X = playerX3 - random.randint(100, 150)
target7Y = playerY3
target8X = playerX3 + random.randint(100, 150)
target8Y = playerY3
target9X = playerX3 + random.randint(100, 150)
target9Y = playerY3 + random.randint(100, 150)

target10X = playerX4 - random.randint(100, 150)
target10Y = playerY4 - random.randint(100, 150)
target11X = playerX4 + random.randint(100, 150)
target11Y = playerY4 + random.randint(100, 150)
target12X = playerX4 - random.randint(100, 150)
target12Y = playerY4

target13X = playerX5 + random.randint(100, 150)
target13Y = playerY5 + random.randint(100, 150)
target14X = playerX5
target14Y = playerY5 - random.randint(100, 150)
target15X = playerX5 + random.randint(100, 150)
target15Y = playerY5

# Puts targets onto screen:
def target1():
    target1 = pygame.image.load('target.png')  # loads image of target
    target1 = pygame.transform.scale(target1, (80, 80))  # scales down target to 80x80px size
    screen.blit(target1, (target1X, target1Y))  # puts target onto screen with x and y coordinate


target1_rect = pygame.Rect(target1X, target1Y, 80, 80) # puts rectangle of target on screen for clicking


def target2():
   target2 = pygame.image.load('target.png')
   target2 = pygame.transform.scale(target2, (80, 80))
   screen.blit(target2, (target2X, target2Y))


target2_rect = pygame.Rect(target2X, target2Y, 80, 80)




def target3():
   target3 = pygame.image.load('target.png')
   target3 = pygame.transform.scale(target3, (80, 80))
   screen.blit(target3, (target3X, target3Y))


target3_rect = pygame.Rect(target3X, target3Y, 80, 80)

def target4():
   target4 = pygame.image.load('target.png')
   target4 = pygame.transform.scale(target4, (80, 80))
   screen.blit(target4, (target4X, target4Y))


target4_rect = pygame.Rect(target4X, target4Y, 80, 80)


def target5():
   target5 = pygame.image.load('target.png')
   target5 = pygame.transform.scale(target5, (80, 80))
   screen.blit(target5, (target5X, target5Y))


target5_rect = pygame.Rect(target5X, target5Y, 80, 80)


def target6():
   target6 = pygame.image.load('target.png')
   target6 = pygame.transform.scale(target6, (80, 80))
   screen.blit(target6, (target6X, target6Y))


target6_rect = pygame.Rect(target6X, target6Y, 80, 80)


def target7():
   target7 = pygame.image.load('target.png')
   target7 = pygame.transform.scale(target7, (80, 80))
   screen.blit(target7, (target7X, target7Y))


target7_rect = pygame.Rect(target7X, target7Y, 80, 80)

def target8():
   target8 = pygame.image.load('target.png')
   target8 = pygame.transform.scale(target8, (80, 80))
   screen.blit(target8, (target8X, target8Y))


target8_rect = pygame.Rect(target8X, target8Y, 80, 80)

def target9():
   target9 = pygame.image.load('target.png')
   target9 = pygame.transform.scale(target9, (80, 80))
   screen.blit(target9, (target9X, target9Y))


target9_rect = pygame.Rect(target9X, target9Y, 80, 80)

def target10():
   target10 = pygame.image.load('target.png')
   target10 = pygame.transform.scale(target10, (80, 80))
   screen.blit(target10, (target10X, target10Y))


target10_rect = pygame.Rect(target10X, target10Y, 80, 80)

def target11():
   target11 = pygame.image.load('target.png')
   target11 = pygame.transform.scale(target11, (80, 80))
   screen.blit(target11, (target11X, target11Y))


target11_rect = pygame.Rect(target11X, target11Y, 80, 80)

def target12():
   target12 = pygame.image.load('target.png')
   target12 = pygame.transform.scale(target12, (80, 80))
   screen.blit(target12, (target12X, target12Y))


target12_rect = pygame.Rect(target12X, target12Y, 80, 80)

def target13():
   target13 = pygame.image.load('target.png')
   target13 = pygame.transform.scale(target13, (80, 80))
   screen.blit(target13, (target13X, target13Y))


target13_rect = pygame.Rect(target13X, target13Y, 80, 80)

def target14():
   target14 = pygame.image.load('target.png')
   target14 = pygame.transform.scale(target14, (80, 80))
   screen.blit(target14, (target14X, target14Y))


target14_rect = pygame.Rect(target14X, target14Y, 80, 80)

def target15():
   target15 = pygame.image.load('target.png')
   target15 = pygame.transform.scale(target15, (80, 80))
   screen.blit(target15, (target15X, target15Y))

target15_rect = pygame.Rect(target15X, target15Y, 80, 80)

targ1 = target1_rect  # filler, just defining variable outside function
targ2 = target2_rect  # filler, just defining variable outside function
targ3 = target3_rect  # filler, just defining variable outside function
rip = playerImg_rect  # filler, just defining variable outside function

# Function for game with parameter difficulty
def game(difficult):
    # global variables that can be accessed throughout the program
    global game_state, time1, time2, time3, caughtfish, numcaughtfish, currentfish, event, targ2, targ1, targ3, rip
    screen.blit(gamebackground, (-700, -600))  # puts background onto screen
    start_ticks = pygame.time.get_ticks()  # starts timer
    while game_state == 'Game':
        for event in pygame.event.get():  # to constantly scan for events such as mouse clicks
            if fish == 1:  # different ripple position for each fish
                rip = playerImg_rect
                ripple()
            if fish == 2:
                rip = playerImg2_rect
                ripple2()
            if fish == 3:
                rip = playerImg3_rect
                ripple3()
            if fish == 4:
                rip = playerImg4_rect
                ripple4()
            if fish == 5:
                rip = playerImg5_rect
                ripple5()
            if difficult == 'Easy':  # the easier the game mode, the more time given to click the targets
                time1 = 5
                time2 = 10
                time3 = 15
            else:
                if difficult == 'Medium':
                    time1 = 4
                    time2 = 8
                    time3 = 12
                else:
                    if difficult == 'Hard':
                        time1 = 3
                        time2 = 6
                        time3 = 9
            if event.type == pygame.MOUSEBUTTONDOWN:  # if mouse clicked
                mouse_position = pygame.mouse.get_pos()  # get mouse position
                if rip.collidepoint(mouse_position):  # if ripple position and mouse position equal
                    if fish == 1:  # different target for each fish
                        target1()
                        ripple()  # this is here to keep the ripple up on the screen
                        targ1 = target1_rect
                    if fish == 2:
                        targ1 = target4_rect
                        target4()
                        ripple2()
                    if fish == 3:
                        targ1 = target7_rect
                        target7()
                        ripple3()
                    if fish == 4:
                        targ1 = target10_rect
                        target10()
                        ripple4()
                    if fish == 5:
                        targ1 = target13_rect
                        target13()
                        ripple5()
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # variable seconds receives the time
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if seconds < time1:  # if clicked within the maximum amount of seconds
                    if targ1.collidepoint(mouse_position):
                        screen.blit(gamebackground, (-700, -600))  # puts background on screen to cover the old target
                        if fish == 1:  # different target for each fish
                            targ2 = target2_rect
                            target2()
                            ripple()
                        if fish == 2:
                            targ2 = target5_rect
                            target5()
                            ripple2()
                        if fish == 3:
                            targ2 = target8_rect
                            target8()
                            ripple3()
                        if fish == 4:
                            targ2 = target11_rect
                            target11()
                            ripple4()
                        if fish == 5:
                            targ2 = target14_rect
                            target14()
                            ripple5()
                else:
                    game_state = 'Fail'  # if not clicked in time, go to fail screen
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if seconds < time2:
                    if targ2.collidepoint(mouse_position):
                        screen.blit(gamebackground, (-700, -600))
                        if fish == 1:
                            targ3 = target3_rect
                            target3()
                            ripple()
                        if fish == 2:
                            targ3 = target6_rect
                            target6()
                            ripple2()
                        if fish == 3:
                            targ3 = target9_rect
                            target9()
                            ripple3()
                        if fish == 4:
                            targ3 = target12_rect
                            target12()
                            ripple4()
                        if fish == 5:
                            targ3 = target15_rect
                            target15()
                            ripple5()
                else:
                    game_state = 'Fail'
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if seconds < time3:
                    if targ3.collidepoint(mouse_position):
                        screen.blit(gamebackground, (-700, -600))
                        if fish == 1:
                            caughtfish = 'tuna'  # puts which fish are caught into huge string variable
                            currentfish = 'tuna'  # puts current fish caught for the congratulations screen
                            numcaughtfish = numcaughtfish + 1  # variable that keeps track of how many total fish caught
                            game_state = 'Caught'  # moves to the caught screen
                        if fish == 2:
                            caughtfish = caughtfish + ',' + ' salmon'
                            currentfish = 'salmon'
                            numcaughtfish = numcaughtfish + 1
                            game_state = 'Caught'
                        if fish == 3:
                            caughtfish = caughtfish + ',' + ' swordfish'
                            currentfish = 'swordfish'
                            numcaughtfish = numcaughtfish + 1
                            game_state = 'Caught'
                        if fish == 4:
                            caughtfish = caughtfish + ',' + ' Great White Shark'
                            currentfish = 'Great White Shark'
                            numcaughtfish = numcaughtfish + 1
                            game_state = 'Caught'
                        if fish == 5:
                            caughtfish = caughtfish + ',' + ' Orca'
                            currentfish = 'Orca'
                            numcaughtfish = numcaughtfish + 1
                            game_state = 'Caught'
                    pygame.display.update()
                pygame.display.update()
# Game Variables
fish = 1  # filler, just defining variable outside function
numcaughtfish = 0  # filler, just defining variable outside function
game_state = 'Menu'  # to make game start off with menu screen
caughtfish = ''  # filler, just defining variable outside function
start_ticks = pygame.time.get_ticks()  # starts timer
# Game
running = True
while running:  # keeps the program running
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
    if game_state == "Menu":  # game starts off with the menu screen
        button_font = pygame.font.Font('freesansbold.ttf', 64)  # font of text
        start_text = button_font.render('START', True, (255, 255, 255))  # declares content of text
        ins_text = button_font.render('INSTRUCTIONS', True, (255, 255, 255))  # declares content of text
        quit_text = button_font.render('QUIT', True, (255, 255, 255))  # declares content of text
        quit_text_rect = quit_text.get_rect()  # declares rectangle of text to be clicked on
        start_text_rect = start_text.get_rect()  # declares rectangle of text to be clicked on
        ins_text_rect = ins_text.get_rect()  # declares rectangle of text to be clicked on
        quit_text_rect.x = 400  # declares x coordinate of rectangle of quit button
        quit_text_rect.y = 400  # declares y coordinate of rectangle of quit button
        start_text_rect.x = 400
        start_text_rect.y = 200
        ins_text_rect.x = 400
        ins_text_rect.y = 300
        # puts everything on screen
        screen.blit(gamebackground, (-700, -600))
        screen.blit(quit_text, (400, 400))
        screen.blit(start_text, (400, 200))
        screen.blit(ins_text, (400, 300))
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if quit_text_rect.collidepoint(mouse_position):
                pygame.quit()  # if quit button clicked, game quit
            if start_text_rect.collidepoint(mouse_position):
                game_state = 'Difficulty'  # if start button clicked, move to difficulty screen to select difficulty
                screen.blit(gamebackground, (-700, -600))
            if ins_text_rect.collidepoint(mouse_position):
                game_state = 'Instruction' # if instruction button clicked, move to instruction screen to read them
    if game_state == "Instruction":
        screen.fill((255, 255, 255))
        button_font = pygame.font.Font('TitilliumWeb-Regular.ttf', 64)
        start_text = button_font.render('START', True, (0, 150, 255))
        start_text_rect = start_text.get_rect()
        start_text_rect.x = 400
        start_text_rect.y = 400
        ins_font = pygame.font.Font('TitilliumWeb-Regular.ttf', 24)
        ins_text1 = ins_font.render('Click the ripples in the pond to cast your fishing rod.', True, (0, 150, 255))
        ins_text2 = ins_font.render('Click on the targets in the correct order to successfully catch the fish!',
                                    True, (0, 150, 255))
        ins_text3 = ins_font.render('Good Luck! Have Fun!', True, (0, 150, 255))
        # puts everything on screen
        screen.blit(ins_text1, (100, 200))
        screen.blit(ins_text2, (100, 250))
        screen.blit(ins_text3, (100, 300))
        screen.blit(start_text, (400, 400))
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if start_text_rect.collidepoint(mouse_position):
                # once the start button is clicked, the game moves to a difficulty screen to select difficulty
                game_state = 'Difficulty'
    if game_state == 'Caught':
        global difficulty
        screen.fill((255, 255, 255))
        goo_font = pygame.font.Font('TitilliumWeb-Regular.ttf', 36)
        goo_text1 = goo_font.render('Congrats! You have caught a ' + currentfish + '!', True, (0, 150, 255))
        cont_text = goo_font.render('CONTINUE', True, (0, 150, 255))
        cont_text_rect = cont_text.get_rect()
        cont_text_rect.x = 400
        cont_text_rect.y = 500
        screen.blit(cont_text, (400, 500))
        screen.blit(goo_text1, (100, 300))
        if event.type == MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if cont_text_rect.collidepoint(mouse_position):
                if fish == 5:
                    game_state = 'Done'
                else:
                    fish = fish + 1
                    screen.blit(gamebackground, (-700, -600))
                    game_state = 'Game'
                    game(difficulty)
                    start_ticks = pygame.time.get_ticks()  # starter tick
        pygame.display.update()
    if game_state == 'Fail':
        screen.fill((255, 255, 255))
        sor_font = pygame.font.Font('TitilliumWeb-Regular.ttf', 24)
        sor_text = sor_font.render('You did not click the targets in time! The fish swam away!', True, (0, 150, 255))
        cont_text = sor_font.render('CONTINUE', True, (0, 150, 255))
        cont_text_rect = cont_text.get_rect()
        cont_text_rect.x = 400
        cont_text_rect.y = 500
        screen.blit(cont_text, (400, 500))
        screen.blit(sor_text, (100, 300))
        if event.type == MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if cont_text_rect.collidepoint(mouse_position):
                if fish > 4:
                    game_state = 'Done'
                else:
                    game_state = 'Game'
                    screen.blit(gamebackground, (-700, -600))
                    fish = fish + 1
                    game(difficulty)
                    start_ticks = pygame.time.get_ticks()  # starter tick
        pygame.display.update()
    if game_state == 'Done':
        screen.fill((255, 255, 255))
        button_font = pygame.font.Font('TitilliumWeb-Regular.ttf', 64)
        quit_text = button_font.render('QUIT', True, (0, 0, 255))
        quit_text_rect = quit_text.get_rect()
        quit_text_rect.x = 400
        quit_text_rect.y = 400
        don_font = pygame.font.Font('TitilliumWeb-Regular.ttf', 20)
        don_text1 = don_font.render('Congratulations! You successfully caught: ' + caughtfish + '.', True, (0, 0, 255))
        if numcaughtfish < 5:
            don_text2 = don_font.render('Unfortunately, you did not catch ' + str(5 - numcaughtfish) + ' fish.', True,
                                        (0, 0, 255))
            screen.blit(don_text2, (100, 300))
        screen.blit(don_text1, (100, 200))
        screen.blit(quit_text, (400, 400))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if quit_text_rect.collidepoint(mouse_position):
                pygame.quit()
        pygame.display.update()
    if game_state == 'Difficulty':
        screen.fill((255, 255, 255))
        button_font = pygame.font.Font('TitilliumWeb-Regular.ttf', 64)
        ins_font = pygame.font.Font('freesansbold.ttf', 24)
        ins_text1 = ins_font.render('Easy', True, (0, 150, 255))
        ins_text2 = ins_font.render('Medium',
                                    True, (0, 150, 255))
        ins_text3 = ins_font.render('Hard', True, (0, 150, 255))
        ins_text1_rect = ins_text1.get_rect()
        ins_text1_rect.x = 450
        ins_text1_rect.y = 250
        ins_text2_rect = ins_text2.get_rect()
        ins_text2_rect.x = 450
        ins_text2_rect.y = 300
        ins_text3_rect = ins_text3.get_rect()
        ins_text3_rect.x = 450
        ins_text3_rect.y = 350
        screen.blit(ins_text1, (450, 250))
        screen.blit(ins_text2, (450, 300))
        screen.blit(ins_text3, (450, 350))
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if ins_text1_rect.collidepoint(mouse_position):
                difficulty = 'Easy'
                game_state = 'Game'
                game(difficulty)
                start_ticks = pygame.time.get_ticks()
                screen.blit(gamebackground, (-700, -600))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if ins_text2_rect.collidepoint(mouse_position):
                difficulty = 'Medium'
                game_state = 'Game'
                game(difficulty)
                start_ticks = pygame.time.get_ticks()
                screen.blit(gamebackground, (-700, -600))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if ins_text3_rect.collidepoint(mouse_position):
                game_state = 'Game'
                difficulty = 'Hard'
                game(difficulty)
                start_ticks = pygame.time.get_ticks()
                screen.blit(gamebackground, (-700, -600))

