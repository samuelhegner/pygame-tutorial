import sys
import pygame

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

def main():
    print("Initialising pygame!")

    pygame.init()

    # Setting up the game window
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))

    # Setting up the fps clock
    fpsClock = pygame.time.Clock()

    # Starting the game loop
    running = True

    while running:
        # Looping over every event that happened this frame
        for event in pygame.event.get():
            # Handling the Quit event
            if event.type == pygame.QUIT:
                running = False

        # Wiping the screen to black every frame
        screen.fill(BLACK)

        # Drawing all changes to the display
        pygame.display.update()

        # Updating the fps clock with our desired fps value
        fpsClock.tick(FPS)
    
    pygame.quit()
    sys.exit(0)


if __name__=="__main__":
    main()