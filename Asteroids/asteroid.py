import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

        print("Asteroid created at", x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            a1 = self.velocity.rotate(angle)
            a2 = self.velocity.rotate(-angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            left_vec = self.velocity.rotate(angle)
            right_vec = self.velocity.rotate(-angle)

            left_ast = Asteroid(self.position.x, self.position.y, new_radius)
            left_ast.velocity = left_vec * 1.2

            right_ast = Asteroid(self.position.x, self.position.y, new_radius)
            right_ast.velocity = right_vec * 1.2
