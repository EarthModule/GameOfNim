from stickgame.players import AI
from stickgame.game import Game

ai1 = AI(20)
ai2 = AI(20)

for i in range(0, 10000):
    game = Game(ai1, ai2)
    ai1.assign_game(game)
    ai2.assign_game(game)
    while game.consume_turn_and_continue():
        continue
    loser = game.active_player
    winner = game.other_player
    winner.learn_from_last_game(True)
    loser.learn_from_last_game(False)
