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

        # Generate irregular asteroid shape
        self.vertices = self._generate_irregular_shape()

        print("Asteroid created at", x, y)

    def _generate_irregular_shape(self):
        """Generate random irregular polygon vertices for asteroid shape"""
        num_vertices = random.randint(8, 12)
        vertices = []

        for i in range(num_vertices):
            angle = (i / num_vertices) * 360
            # Vary the distance from center to create irregular shape
            distance = self.radius * random.uniform(0.7, 1.3)

            # Calculate vertex position relative to center
            rad = angle * (3.14159 / 180)
            x = distance * pygame.math.Vector2(1, 0).rotate(angle).x
            y = distance * pygame.math.Vector2(1, 0).rotate(angle).y

            vertices.append((x, y))

        return vertices

    def draw(self, screen):
        # Calculate absolute positions of vertices
        points = [(self.position.x + vx, self.position.y + vy) for vx, vy in self.vertices]
        pygame.draw.polygon(screen, "white", points, width=2)

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
