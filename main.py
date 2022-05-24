from game import Game

my_game = Game()

while my_game.running:
    my_game.curr_menu.display_menu()
    my_game.game_loop()
