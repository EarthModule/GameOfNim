from random import randint


def input_validator(prompt):
    i = 0
    while i < 1 or i > 3:
        i = int(input(prompt))
    return i


class Player(object):
    def __init__(self):
        super().__init__()
        self.__my_turn = False
        self.prefix = "player"
        self.number = None

    @property
    def name(self):
        return self.prefix + str(self.number)

    @name.setter
    def name(self, new_number):
        self.number = new_number

    def gives_turn_to(self, player):
        self.turn = False
        player.turn = True

    @property
    def turn(self):
        return self.__my_turn

    @turn.setter
    def turn(self, new_value):
        if self.__my_turn != new_value:
            self.__my_turn = new_value

    def draw(self):
        pass


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.prefix = "Human"
        self.prompt = "How many sticks will you draw? (1-3)\n"

    def draw(self):
        return input_validator(self.prompt)


class BrainCell(object):
    def __init__(self):
        super().__init__()
        self.__memory_pattern = [1, 2, 3]
        self.__last_opinion = 0

    @property
    def decision(self):
        random_index = randint(0, len(self.__memory_pattern) - 1)
        opinion = self.__memory_pattern.pop(random_index)
        self.__last_opinion = opinion
        self.__rectify_memory()
        return opinion

    def __rectify_memory(self):
        for i in range(1, 4):
            # print('rectifying ' + str(i))
            if self.__memory_pattern.count(i) == 0:
                self.__memory_pattern.append(i)

    def learn_from(self, victory):
        if self.__last_opinion != 0:
            if victory:
                self.__memory_pattern.append(self.__last_opinion)
                self.__memory_pattern.sort()
            else:
                self.__rectify_memory()
                self.__memory_pattern.remove(self.__last_opinion)

            self.__last_opinion = 0


class AI(Player):
    def __init__(self, sticks):
        super(AI, self).__init__()
        self.prefix = 'AI'
        self.braincells = {}
        self.populate_braincells(sticks)
        self.game = None

    def assign_game(self, game):
        self.game = game

    def populate_braincells(self, sticks):
        for i in range(1, sticks + 1):
            self.braincells[i] = BrainCell()

    def learn_from_last_game(self, victorious):
        for key, value in self.braincells.items():
            value.learn_from(victorious)

    def make_decision(self, current_sticks):
        sticks = self.braincells[current_sticks].decision
        print("AI draws " + str(sticks) + " sticks\n")
        return sticks

    def draw(self):
        sticks = self.game.sticks_left
        return self.make_decision(sticks)


if __name__ == '__main__':
    b = BrainCell()
