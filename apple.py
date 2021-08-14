"""
This module represents the apple that appears at random places on the screen.
"""
import random
from typing import List
from gui import Gui
from position import Position

gui = Gui()

# Rewritten and works
def collides(p, positions):
    """Return true if p is any of the positions in the list."""
    for position in positions:
        if p.equals(position) == True:
            return True
        else:
            return False

def rand_x():
    x = random.randrange(1, gui.get_width() - 2)
    return x

def rand_y():
    y = random.randrange(1, gui.get_height() - 2)
    return y

def rand_pos():
    pos = Position(rand_x(), rand_y())
    return pos

class Apple:
    """The apple's location is randomly generated."""

    def __init__(self, Position=rand_pos()):
        self.position = Position
        self.xpos = self.position.get_x()
        self.ypos = self.position.get_y()

    def draw(self, gui):
        gui.draw_text("*", self.position.get_x(), self.position.get_y(),
                                                         "GREEN", "RED")

    def is_eaten(self):
        self.position = rand_pos()
