import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    frames = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        player_object.draw(screen)
        pygame.display.flip()

        # set to 60 fps
        dt = frames.tick(60) / 1000

if __name__ == "__main__":
    main()