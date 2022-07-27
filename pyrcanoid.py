# Arcanoid clone written with Python and pygame

import os
import pygame
from pygame import Vector2
from pygame import Rect

os.environ['SDL_VIDEO_CENTERED'] = '1'


class GameState:
    def __init__(self):
        self.world_size = Vector2(60, 48)
        self.bat_pos = Vector2(30, 47)

    def update(self, move_bat_command):
        self.bat_pos += move_bat_command

        if self.bat_pos.x < 0:
            self.bat_pos.x = 0
        elif self.bat_pos.x >= self.world_size.x - 4:
            self.bat_pos.x = self.world_size.x - 5


class UserInterface:
    def __init__(self):
        pygame.init()

        self.game_state = GameState()

        self.cell_size = Vector2(20, 20)

        window_size = self.game_state.world_size.elementwise() * self.cell_size
        self.window = pygame.display.set_mode((int(window_size.x), int(window_size.y)))
        pygame.display.set_caption('Pyrcanoid')
        self.move_bat_command = Vector2(0, 0)
        self.clock = pygame.time.Clock()
        self.running = True

    def process_input(self):
        self.move_bat_command.x = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self.move_bat_command.x += 1
                elif event.key == pygame.K_LEFT:
                    self.move_bat_command.x -= 1

    def update(self):
        self.game_state.update(self.move_bat_command)

    def render(self):
        self.window.fill((0, 0, 0))

        sprite_point = self.game_state.bat_pos.elementwise() * self.cell_size
        pygame.draw.rect(self.window, (0, 0, 255), (
            int(sprite_point.x),
            int(sprite_point.y),
            int(self.cell_size.x * 5),
            int(self.cell_size.y))
        )

        pygame.display.update()

    def run(self):
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(60)


game = UserInterface()
game.run()
pygame.quit()
