import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    frames = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        for object in updatable:
            object.update(dt)
        # render player object
        for object in drawable:
            object.draw(screen)
        # updates screen
        pygame.display.flip()

        # set to 60 fps
        dt = frames.tick(60) / 1000

if __name__ == "__main__":
    main()