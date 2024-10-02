import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot

def main():
    pygame.init()

    frames = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #initialization of objects
    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field_object = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        for object in updatable:
            object.update(dt)
        # render objects
        for object in drawable:
            object.draw(screen)
        # updates screen
        pygame.display.flip()
        # check for collision
        for this_asteroid in asteroids:
            if this_asteroid.is_colliding(player_object) == True:
                print("Game over!")
                exit()
            for this_shot in shots:
                if this_asteroid.is_colliding(this_shot) == True:
                    this_asteroid.kill()
                    this_shot.kill()

        # set to 60 fps
        dt = frames.tick(60) / 1000

if __name__ == "__main__":
    main()