from circleshape import *
from constants import *
from main import *
import pygame 


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.score = 0
        self.lives = 3

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = velocity
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                return
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN

    def update_score(self, add):
        self.score += add

    def update_lives(self):
        self.lives -= 1

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        width = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, width)

    def update(self, dt):
        self.position += (self.velocity * dt)