import pygame
import random
import math
from pygame import mixer

# Initialise the pygame
pygame.init()

# Start Screen

WHITE = (255, 255, 255)

# Set the height and width of the screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("GALAGA v2.0.19")
icon1 = pygame.image.load('icon.png')
pygame.display.set_icon(icon1)

# This is a font we use to draw text on the screen
font1 = pygame.font.Font(None, 150)
font2 = pygame.font.Font(None, 50)
font3 = pygame.font.Font(None, 35)
font4 = pygame.font.Font(None, 100)
font5 = pygame.font.Font(None, 35)
font6 = pygame.font.Font(None, 35)

display_instructions = True
instruction_page = 1

# Loop until the user clicks the close button.
done = False

# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False

    # Set the screen background
    background = pygame.image.load('background.png')

    screen.blit(background, (0, 0))

    if instruction_page == 1:
        # Draw instructions, page 1
        text1 = font1.render("GALAGA", True, WHITE)
        screen.blit(text1, [185, 120])
        text2 = font2.render("v2.0.19", True, WHITE)
        screen.blit(text2, [340, 220])
        text3 = font3.render("CLICK TO CONTINUE", True, WHITE)
        screen.blit(text3, [275, 500])

    if instruction_page == 2:
        # Draw instructions, page1
        text4 = font4.render("START", True, WHITE)
        screen.blit(text4, [290, 100])
        text2 = font2.render("CONTROLS", True, WHITE)
        screen.blit(text2, [300, 400])
        text3 = font3.render("MOVE LEFT                            LEFT ARROW ", True, WHITE)
        screen.blit(text3, [150, 450])
        text5 = font5.render("MOVE RIGHT                          RIGHT ARROW", True, WHITE)
        screen.blit(text5, [150, 500])
        text6 = font6.render("Fire                                          SPACE BAR", True, WHITE)
        screen.blit(text6, [150, 550])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()

# Game Window

# Create the game window
screen = pygame.display.set_mode((800, 600))

# Adding  the background of the game window.
background = pygame.image.load('background.png')

# Adding  the background music of the game window.
mixer.music.load('music.mp3')
mixer.music.play(-1)

# Change the title and icon of the game window
pygame.display.set_caption("GALAGA v2.0.19")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Setting the player's spaceship.
playerSpaceship = pygame.image.load('ship.png')
playerX = 360
playerY = 510
playerXmovement = 0


def playerShip(x, y):
    screen.blit(playerSpaceship, (x, y))


# Setting the enemy.

enemyAlien = []
enemyX = []
enemyY = []
enemyXmovement = []
enemyYmovement = []
numEnemies = 6

for i in range(numEnemies):
    img = random.randint(1, 6)
    if img == 1:
        enemyAlien.append(pygame.image.load('enemy1.png'))
    if img == 2:
        enemyAlien.append(pygame.image.load('enemy2.png'))
    if img == 3:
        enemyAlien.append(pygame.image.load('enemy3.png'))
    if img == 4:
        enemyAlien.append(pygame.image.load('enemy4.png'))
    if img == 5:
        enemyAlien.append(pygame.image.load('enemy5.png'))
    if img == 6:
        enemyAlien.append(pygame.image.load('enemy6.png'))

    enemyX.append(random.randint(0, 800 - 64))
    enemyY.append(random.randint(10, 90))
    enemyXmovement.append(4)
    enemyYmovement.append(30)


def enemyShip(x, y, i):
    screen.blit(enemyAlien[i], (x, y))


# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 500
bulletXmovement = 0
bulletYmovement = 10
bullet_state = 'ready'


def fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


# Check the collision between the enemy and the bullet
def checkCollision(eX, eY, bX, bY):
    d = math.sqrt((eX - bX) ** 2 + (eY - bY) ** 2)
    if d < 30:
        return True
    else:
        return False


# Score font
score = 0
score_font = pygame.font.Font(None, 32)


def score_count(x, y):
    score_ = score_font.render('Score : ' + str(score), True, (255, 255, 255))
    screen.blit(score_, (x, y))


# Game over font
game_over_font = pygame.font.Font(None, 74)


def game_over():
    game_over_text = game_over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(game_over_text, (250, 250))


# Holds the game window.
running = True
while running:

    # To set RGB ratio (red, blue, green) of game window.
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if the Right and Left arrow key has been pressed.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXmovement -= 5
            if event.key == pygame.K_RIGHT:
                playerXmovement += 5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound('fire.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire(bulletX, bulletY)

        # Check if the Right and Left arrow key has been released.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXmovement = 0

    # Checking the boundaries to make the ship, enemies and bullet stay in the game window.

    playerX += playerXmovement
    if playerX < 6:
        playerX = 6
    elif playerX > 800 - 70:
        playerX = 800 - 70

    # Enemy movement

    for i in range(numEnemies):
        # Game over
        if enemyY[i] > 460:
            for j in range(numEnemies):
                enemyY[j] = 2000
            game_over()
            break

        enemyX[i] += enemyXmovement[i]
        if enemyX[i] < 0:
            enemyXmovement[i] = 4
            enemyY[i] += enemyYmovement[i]
        elif enemyX[i] > 800 - 64:
            enemyXmovement[i] = -4
            enemyY[i] += enemyYmovement[i]

        collision = checkCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explode = mixer.Sound('explosion.wav')
            explode.play()
            bulletY = 500
            bullet_state = 'ready'
            score += 1

            enemyX[i] = random.randint(0, 800 - 64)
            enemyY[i] = random.randint(10, 90)

        enemyShip(enemyX[i], enemyY[i], i)

    if bulletY <= 0 - 32:
        bulletY = 500
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire(bulletX, bulletY)
        bulletY -= bulletYmovement

    playerShip(playerX, playerY)
    score_count(10, 10)

    pygame.display.update()
