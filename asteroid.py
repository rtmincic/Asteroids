from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"White", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        angle_1 = self.velocity.rotate(angle)
        angle_2 = self.velocity.rotate(-angle)

        self.radius -= ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid.velocity =  angle_1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid.velocity =  angle_2 * 1.2