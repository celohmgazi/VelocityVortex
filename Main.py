import pygame

pygame.init()

# Game Display
display_width = 800
display_height = 600

# Color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


x = (display_width * 0.45)
y = (display_height * 0.8)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A BIT RACEY')
clock = pygame.time.Clock()
carImg = pygame.image.load('RaceCar.png')

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
