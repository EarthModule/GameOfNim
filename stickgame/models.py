from random import randint


class BrainCell(object):
    def __init__(self):
        super(BrainCell, self).__init__()
        self.learned_decisions = [1, 2, 3]
        self.last_decision = 0

    def get_random_decision(self):
        index = randint(0, len(self.learned_decisions)-1)
        decision = self.learned_decisions.pop(index)
        self.last_decision = decision
        self.add_missing_decisions()
        return decision

    def add_missing_decisions(self):
        if self.learned_decisions.count(1)==0:
            print('added 1')
            self.learned_decisions.append(1)
        elif self.learned_decisions.count(2)==0:
            print('added 2')
            self.learned_decisions.append(2)
        elif self.learned_decisions.count(3)==0:
            print('added 3')
            self.learned_decisions.append(3)

    def learn_last_decision(self, victorious):
        if self.last_decision != 0:
            if victorious:
                self.learned_decisions.append(self.last_decision)
                self.learned_decisions.sort()
            else:
                self.learned_decisions.remove(self.last_decision)
            self.add_missing_decisions()
            self.last_decision = 0




class AI(object):
    def __init__(self, sticks_on_board=20):
        super(AI, self).__init__()
        self.braincells = {}

    def populate_braincells(self, sticks):
        for i in range(1, sticks):
            self.braincells[i] = BrainCell()

    def learn_from_last_game(self, victorious):
        for key, value in self.braincells.iteritems():
            value.learn_last_decision(victorious)

    def make_decision(self, current_sticks):
        return self.braincells[current_sticks].get_random_decision()


if __name__ == '__main__':
    b = BrainCell()


