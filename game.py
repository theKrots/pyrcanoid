import pygame

from typing import Tuple
# from menu import MainMenu, OptionsMenu, CreditsMenu

class Game():
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600
    FULLSCREEN = pygame.FULLSCREEN
    SCALED = pygame.SCALED
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    running: bool
    playing: bool
    font_name: str
    def __init__(self) -> None:
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.display = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.font_name = '8-BIT WONDER.TTF'
        # self.main_menu = MainMenu(self)
        # self.options = OptionsMenu(self)
        # self.credits = CreditsMenu(self)
        # self.curr_menu = self.main_menu

    def game_loop(self) -> None:
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.draw_text('Thanks for Playing', 20, int(self.SCREEN_WIDTH / 2), int(self.SCREEN_HEIGHT / 2))
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                # self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self) -> None:
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text: str, size, x: int, y: int) -> None:
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)