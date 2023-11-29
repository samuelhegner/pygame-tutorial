import random
import sys
import pygame

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Balloon(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)


# Screen globals
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Gameplay globals
FPS = 60

# Colours globals
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Spaceship globals
SHIP_WIDTH = 50
SHIP_HEIGHT = 50


def main():
    print("Initialising pygame!")
    pygame.init()

    # Setting games icon
    logo_image = pygame.image.load("2. Sprites/sprites/logo.png")
    spaceship_image = pygame.image.load("2. Sprites/sprites/spaceship.png")
    ball_image = pygame.image.load("2. Sprites/sprites/ball.png")

    pygame.display.set_icon(logo_image)

    # Setting up the game window
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))

    # Starting the game loop
    running = True

    # Setting up the spaceship
    spaceship = Spaceship(spaceship_image, SHIP_WIDTH, SHIP_HEIGHT)

    spaceship_group = pygame.sprite.Group()
    spaceship_group.add(spaceship)

    # Setting up the balloons
    balloon_group = pygame.sprite.Group()

    for n in range(50):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        balloon = Balloon(ball_image, x, y)
        balloon_group.add(balloon)

    while running:
        # Looping over every event that happened this frame. If the quit event is received, we stop the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Wiping the screen to black every frame
        screen.fill(BLACK)

        # Draw the balloon sprite group
        balloon_group.draw(screen)

        # Draw the spaceship sprite group
        spaceship_group.update()
        spaceship_group.draw(screen)

        # Drawing all changes to the display
        pygame.display.update()
    
    pygame.quit()
    sys.exit(0)


if __name__=="__main__":
    main()