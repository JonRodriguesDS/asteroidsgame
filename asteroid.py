import pygame
from logger import log_event
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,  y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,  "white",  self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            random_angle = random.uniform(20,50)
            new_vector_one = self.velocity.rotate(random_angle)
            new_vector_two = self.velocity.rotate(- random_angle)
            asteroid_one.velocity = new_vector_one * 1.2
            asteroid_two.velocity = new_vector_two * 1.2


