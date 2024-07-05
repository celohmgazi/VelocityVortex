import pygame

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


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


# Car initial position
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

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
        car(x, y)
        if x > display_width - car_width or x < 0:
            gameExit = True
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
