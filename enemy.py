import pygame

class Enemy(pygame.sprite.Sprite):
    surf: pygame.Surface
    rect: pygame.rect.Rect
    def __init__(self) -> None:
        super().__init__()
        self.surf = pygame.Surface((80, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()