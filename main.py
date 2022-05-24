from game import Game
from menu import MainMenu

my_game = Game()
my_menu = MainMenu(my_game)

while my_game.running:
    my_menu.display_menu()
    my_game.game_loop()
