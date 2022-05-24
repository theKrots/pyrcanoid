import pygame

from typing import Tuple

from game import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

class Ball(pygame.sprite.Sprite):
    surf: pygame.Surface
    rect: pygame.rect.Rect
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
