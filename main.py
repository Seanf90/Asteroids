import pygame
import sys
from constants import *
from player import *
import time
from asteroidfield import *

def main():
    pygame.init()
    pygame.font.init()

    GAME_FONT = pygame.freetype.Font("./DepartureMono-Regular.otf", 22)

    margin = 40  
    top_offset = 30  
    score_pos = (margin, top_offset)
    lives_pos = (SCREEN_WIDTH - margin - 100, top_offset)

    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for a in asteroids:
            if a.collision(player) == False:
                player.update_lives()
                a.kill()
                if player.lives == 0:
                    print("Game Over!")
                    sys.exit()
                
        for a in asteroids:
            for s in shots:
                if a.collision(s) == False:
                    player.update_score(1)
                    a.split()

        screen.fill("black")
        GAME_FONT.render_to(screen, score_pos, f"Score: {player.score}", ("white"))
        GAME_FONT.render_to(screen, lives_pos, f"Lives: {player.lives}", ("white"))

        for d in drawable:  
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(144) / 1000


if __name__ == "__main__":
    main()