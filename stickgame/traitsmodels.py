from traits.api import *
from traitsui.api import *

class Game(HasTraits):
    sticks_on_the_board = Int()
    how_many_do_you_draw = Int()
    draw = Button()

    view = View(
        VGroup(
            Item('sticks_on_the_board', style='readonly'),
            Item('how_many_do_you_draw'),
            Item('draw', show_label=False)
        )
    )

class GameConfig(HasTraits):
    sticks = Int(default_value=20)
    start_new_game = Button()

    def _start_new_game_fired(self):
        g = Game(sticks_on_the_board=self.sticks)
        g.configure_traits()



    view = View(
        Item('sticks'),
        Item('start_new_game', show_label=False)
    )


if __name__ == '__main__':
    g = GameConfig()
    g.configure_traits()
