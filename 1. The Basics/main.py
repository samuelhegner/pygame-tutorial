import sys
import pygame

# Screen globals
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Gameplay globals
FPS = 60

# Player globals
PLAYER_SPEED = 10

# Colours globals
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    print("Initialising pygame!")

    pygame.init()

    # Setting games icon
    logo = pygame.image.load("1. The Basics/sprites/logo.png")
    pygame.display.set_icon(logo)

    # Setting up the game window
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))

    # Setting up the fps clock
    fpsClock = pygame.time.Clock()

    # Setting up our player
    player = pygame.Rect((300, 250, 50, 50))

    # Starting the game loop
    running = True

    while running:

        # Looping over every event that happened this frame
        for event in pygame.event.get():
            # Handling the Quit event
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse button clicked!!!")
        
        # Initialising variables to track players x and y movement
        move_x = 0
        move_y = 0

        # Getting every key that was pressed this frame
        pressed_keys = pygame.key.get_pressed()

        # handling player input (up, down, left, right)
        if pressed_keys[pygame.K_UP]:
            move_y -= PLAYER_SPEED
        
        if pressed_keys[pygame.K_DOWN]:
            move_y += PLAYER_SPEED

        if pressed_keys[pygame.K_LEFT]:
            move_x -= PLAYER_SPEED

        if pressed_keys[pygame.K_RIGHT]:
            move_x += PLAYER_SPEED
        
        # Applying the movement to the players location
        player.move_ip(move_x, move_y)

        # Wiping the screen to black every frame
        screen.fill(BLACK)

        # Drawing the player
        pygame.draw.rect(screen, RED, player)

        # Drawing all changes to the display
        pygame.display.update()

        # Updating the fps clock with our desired fps value
        fpsClock.tick(FPS)
    
    pygame.quit()
    sys.exit(0)


if __name__=="__main__":
    main()