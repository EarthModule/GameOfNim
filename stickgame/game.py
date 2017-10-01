from stickgame.players import HumanPlayer, AI, Player
import random


class Game(object):
    def __init__(self, player1: Player, player2: Player, sticks: int = 20) -> object:
        super().__init__()
        self.__sticks = sticks
        self.player1 = player1
        self.player2 = player2
        player1.name = 1
        player2.name = 2
        print(player1.name)
        print(player2.name)
        if random.randint(1, 2) == 1:
            self.player1.gives_turn_to(self.player2)
        else:
            self.player2.gives_turn_to(self.player1)

    @property
    def active_player(self):
        if self.player1.turn:
            return self.player1
        else:
            return self.player2

    @property
    def other_player(self):
        if self.player1.turn:
            return self.player2
        else:
            return self.player1

    @property
    def sticks_left(self):
        return self.__sticks

    def consume_turn_and_continue(self):

        print(str(self.__sticks) + " sticks left\n")
        print(self.active_player.name + "'s turn")
        self.__sticks -= self.active_player.draw()
        self.active_player.gives_turn_to(self.other_player)
        if self.sticks_left < 1:
            print('game ended')
            return False
        else:
            return True


if __name__ == '__main__':
    ai = AI(10)
    human = HumanPlayer()
    g = Game(human, ai, sticks=10)
    ai.assign_game(g)
    g.start()
