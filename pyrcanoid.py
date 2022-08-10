# Arcanoid clone written with Python and pygame

import os
import pygame
from pygame import Vector2
# from pygame import Rect

os.environ['SDL_VIDEO_CENTERED'] = '1'
WINDOW_WIDTH = 30
WINDOW_HEIGHT = 24


class Unit:
    def __init__(self, state, position, size):
        self.state = state
        self.position = position
        self.size = size

    def move(self, move_vector):
        raise NotImplementedError()


class Bat(Unit):
    def move(self, move_vector):
        new_pos = self.position + move_vector

        if new_pos.x < 0 or new_pos.x >= self.state.world_size.x - 4:
            return

        self.position = new_pos


class Ball(Unit):
    def __init__(self, state, position, size):
        super().__init__(state, position, size)
        self.speed = Vector2(1, 1)
        self.time = pygame.time.Clock()

    def move(self, move_vector):
        # TODO: Fix the ball
        self.time.tick(30)
        new_pos = self.position + self.speed
        if new_pos.x < 0:
            self.speed.x *= -1
        elif new_pos.x >= self.state.world_size.x - 1:
            self.speed.x *= -1
        if new_pos.y < 0:
            self.speed.y *= -1
        elif new_pos.y >= self.state.world_size.y - 1:
            self.speed.y *= -1

        self.position = new_pos


class GameState:
    def __init__(self):
        self.world_size = Vector2(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.units = [
            Bat(self, Vector2(int(WINDOW_WIDTH / 2), WINDOW_HEIGHT - 1), 5),
            Ball(self, Vector2(int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2)), 1)
        ]

    def update(self, move_bat_command):
        for unit in self.units:
            unit.move(move_bat_command)


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

    def render_unit(self, unit):

        sprite_point = unit.position.elementwise() * self.cell_size
        pygame.draw.rect(self.window, (0, 0, 255), (
            int(sprite_point.x),
            int(sprite_point.y),
            int(self.cell_size.x * unit.size),
            int(self.cell_size.y))
        )

    def render(self):
        self.window.fill((0, 0, 0))

        for unit in self.game_state.units:
            self.render_unit(unit)

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
