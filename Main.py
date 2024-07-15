import random
import pygame
import time

pygame.init()

# Game Display
display_width = 800
display_height = 600

# Color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A BIT RACEY')
clock = pygame.time.Clock()

try:
    carImg = pygame.image.load('RaceCar.png')
    carImg = pygame.transform.scale(carImg, (80, 100))
except pygame.error:
    print("Error: Unable to load image")
    pygame.quit()
    quit()


def objects(obj_x, obj_y, obj_w, obj_h, color):
    pygame.draw.rect(gameDisplay, color, [obj_x, obj_y, obj_w, obj_h])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def msg_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    msg_display("You Crashed")


# Car initial position
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    object_startX = random.randrange(0, display_width)
    object_startY = -600
    object_speed = 7
    object_width = 100
    object_height = 100

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        objects(object_startX, object_startY, object_width, object_height, black)
        object_startY += object_speed
        car(x, y)

        if x > display_width - car_width or x < 0:
            crash()

        if object_startY >= display_height:
            object_startY = 0 - object_height
            object_startX = random.randrange(0, display_width)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
