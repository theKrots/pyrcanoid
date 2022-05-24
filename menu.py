"""
Describe pyrcanoid menu classes
"""
import pygame

from typing import Type


class Menu:
    middle_width: int
    middle_height: int
    run_display: bool
    cursor_rect: pygame.Rect
    offset: int

    def __init__(self, game) -> None:
        self.game = game
        self.middle_width = int(self.game.SCREEN_WIDTH / 2)
        self.middle_height = int(self.game.SCREEN_HEIGHT / 2)
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self) -> None:
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self) -> None:
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    state: str = 'Start'
    start_x: int
    start_y: int
    quit_x: int
    quit_y: int

    def __init__(self, game) -> None:
        super().__init__(game)
        self.start_x = self.middle_width
        self.start_y = self.middle_height + 30
        self.quit_x = self.middle_width
        self.quit_y = self.middle_height + 50
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self) -> None:
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Pyrcanoid', 40, self.middle_width, self.middle_height - 100)
            self.game.draw_text('Main Menu', 20, self.middle_width, self.middle_height - 20)
            self.game.draw_text('Start Game', 20, self.start_x, self.start_y)
            self.game.draw_text('Quit', 20, self.quit_x, self.quit_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self) -> None:
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.quit_x + self.offset, self.quit_y)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'

        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.quit_x + self.offset, self.quit_y)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Quit':
                self.game.playing = False
                self.game.running = False
                self.display_menu = False
                pygame.quit()

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.middle_width, self.middle_height + 20
        self.controlsx, self.controlsy = self.middle_width, self.middle_height + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.middle_width, self.middle_height - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.middle_width, self.middle_height - 20)
            self.game.draw_text('Made by me', 15, self.middle_width, self.middle_height + 10)
            self.blit_screen()
