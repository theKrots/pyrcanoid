import pygame

from typing import Optional

from game import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

from pygame import (
    K_LEFT,
    K_RIGHT
)

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
