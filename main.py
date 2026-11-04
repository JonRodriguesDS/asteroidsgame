import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event, log_state
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    player = Player(x,y)
    score = 0
    font = pygame.font.Font(None, 36)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255 ,255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

        dt  = clock.tick(60) / 1000
        updatable.update(dt)

        for hit in asteroids:
            for shoot in shots:
                if hit.collides_with(shoot):
                    log_event("asteroid_shot")
                    hit.split()
                    shoot.kill()
                    score += 100
                    log_event("score +100")
        for objects in asteroids:
            if objects.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                print(f"Score: {score}")
                sys.exit()
        

   

if __name__ == "__main__":
    main()
