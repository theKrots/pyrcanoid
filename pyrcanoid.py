# Arcanoid clone written with Python and pygame

# Import and initialize the pygame library
from typing import Tuple, Optional
import pygame
import random

# Import necessary constants from pygame.constants
from pygame.constants import (
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN
)

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FULLSCREEN = pygame.FULLSCREEN
SCALED = pygame.SCALED

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now and attribute of 'player'

class Player(pygame.sprite.Sprite):
    surf: pygame.Surface
    rect: Optional[pygame.rect.Rect]
    def __init__(self) -> None:
        super().__init__()
        self.surf = pygame.Surface((70, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (
            (SCREEN_WIDTH - self.surf.get_width()) / 2, SCREEN_HEIGHT - self.surf.get_height())
            )
    
    # Move the sprite based on user keypress
    def update(self, pressed_move_key):
        if pressed_move_key[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_move_key[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Define the ball object by pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'ball'
class Ball(pygame.sprite.Sprite):
    surf: pygame.Surface
    rect: Optional[pygame.rect.Rect]
    speed_x: int
    speed_y: int
    def __init__(self) -> None:
        super().__init__()
        self.surf = pygame.Surface([10, 10])
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (
            (SCREEN_WIDTH - self.surf.get_width()) / 2, 
            (SCREEN_HEIGHT - self.surf.get_height()) / 2
        ))
        self.speed_x = 1
        self.speed_y = 4
    
    def get_speed(self) -> Tuple[int, int]:
        return (self.speed_x, self.speed_y)

    def update_speed(self, speed_x: int, speed_y: int) -> None:
        self.speed_x += speed_x
        self.speed_y += speed_y
    
    def reverse_speed_x(self) ->None:
        self.speed_x = -self.speed_x

    def reverse_speed_y(self) ->None:
        self.speed_y = -self.speed_y

    def update_ball(self) -> None:
        self.rect.move_ip(self.get_speed())

# Define enemy class
class Enemy(pygame.sprite.Sprite):
    surf: pygame.Surface
    rect: Optional[pygame.rect.Rect]
    def __init__(self) -> None:
        super().__init__()
        self.surf = pygame.Surface((80, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN|SCALED)

# Initialize player. Right now, this is just a rectangle.
player = Player()
ball = Ball()

# Create group to hold enemy sprites and all sprites

ball_sprite = pygame.sprite.Group()
ball_sprite.add(ball)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ball)

enemies = pygame.sprite.Group()

# Generate enemies
for i in range(0, 10):
    for j in range(0, 5):
        enemy = Enemy()
        enemy.rect = enemy.surf.get_rect(topleft = [i * 80, j * 20])
        enemies.add(enemy)
        all_sprites.add(enemy)

# Variable to keep the main loop running
running = True
clock = pygame.time.Clock()

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
    
    # Get all the keys currently pressed.
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypress.
    player.update(pressed_keys)

    # Update ball position
    ball.update_ball()

    # Fill the screen with black
    screen.fill((0, 0, 0))
    
    # This the player on the screen
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)
    
    # Check if the ball have collided with the player
    if pygame.sprite.spritecollideany(player, ball_sprite):
        ball.reverse_speed_y()
        ball.update_speed(random.randint(-4, 4), 0)
    
    # Check if the ball reaches screen borders
    if ball.rect.top <= 0:
        ball.reverse_speed_y()
    if ball.rect.left <= 0:
        ball.reverse_speed_x()
    if ball.rect.right >=SCREEN_WIDTH:
        ball.reverse_speed_x()
    if ball.rect.bottom >= SCREEN_HEIGHT:
        running = False

    # Check if the ball have collided with the enemy
    if pygame.sprite.spritecollideany(ball, enemies):
        ball.reverse_speed_y()
        pygame.sprite.spritecollideany(ball, enemies).kill()

    # Check if there are any enemies 
    if not enemies.sprites():
        running = False

    # Update the display
    pygame.display.flip()
    clock.tick(30)