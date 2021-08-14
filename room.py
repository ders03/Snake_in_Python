"""
This module implements the four walls of the room within which Snake is played.
"""
from gui import Gui

class Room:
    """The room has a width and height, a character to draw, and color."""

    def __init__(self, width, height, c,
            fore_color, back_color):
        self.width = width
        self.height = height
        self.c = c
        self.fore_color = fore_color
        self.back_color = back_color

    def draw(self, gui):
        # Top of room; chars removed for scoreboard
        gui.draw_line(self.c, 0, 0, self.width//2 - 2, 0,
                      self.fore_color, self.back_color)
        gui.draw_line(self.c, self.width//2 + 1, 0, self.width - 1, 0,
                      self.fore_color, self.back_color)
        # Bottom of room
        gui.draw_line(self.c, 0, self.height - 1, self.width - 1,
                      self.height - 1, self.fore_color, self.back_color)
        # Left side of room
        gui.draw_line(self.c, 0, 1, 0, self.height - 1,
                      self.fore_color, self.back_color )
        # Right side of room
        gui.draw_line(self.c, self.width - 1, 1, self.width -  1,
                      self.height - 1, self.fore_color, self.back_color)

    def draw_first_line(self, gui):
        # Split room in half for level one
        gui.draw_line(self.c, gui.get_width()//2, 5, gui.get_width()//2,
                      gui.get_height() - 6, "ORANGE", "PURPLE")

    def draw_two_lines(self, gui):
        # Split room in to thirds for level two
        gui.draw_line(self.c, gui.get_width()//4, 0, gui.get_width()//4,
                      gui.get_height() - 6, "ORANGE", "PURPLE")
        gui.draw_line(self.c, (gui.get_width()//4)*3, 5, (gui.get_width()//4)*3,
                      gui.get_height() - 1, "ORANGE", "PURPLE")
