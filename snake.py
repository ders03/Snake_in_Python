"""
This module implements the snake class.
"""
from gui import Gui
from position import Position
from typing import List
import time
import random

class Snake:
    """This is the Snake.

    It has a list of positions. The head is at index 0.
    The tail occupies the rest of the list.
    """
    def __init__(self, direction="d"):
        self.gui = Gui()
        self.init = Position(self.gui.get_width()//2, self.gui.get_height()//2)
        self.tail_pos = Position(self.gui.get_width()//2 - 1, self.gui.get_height()//2)
        self.tail_pos_2 = Position(self.gui.get_width()//2 - 2, self.gui.get_height()//2)
        self.ls_p = [self.init, self.tail_pos, self.tail_pos_2]
        self.ls_c = [">", "+", "+"]
        self.direction = direction

    def current_pos(self):
        return self.ls_p

    def draw(self, gui):
        #Start and Right
        if self.direction == "d":
            self.ls_c[0] = ">"
        #Left
        if self.direction == "a":
            self.ls_c[0] = "<"
        #Up
        if self.direction == "w":
            self.ls_c[0] = "^"
        #Down
        if self.direction == "s":
            self.ls_c[0] = "V"
        #Draw from back to front
        for x in range(len(self.ls_p) - 1, -1, -1):
            gui.draw_text(self.ls_c[x], self.ls_p[x].get_x(),
                                             self.ls_p[x].get_y(),
                                             "RED", "PURPLE")

    def move(self):
        """
        Initiate new head and insert,
        modify base positions,
        pop base head
        """
        #Right
        if self.direction == "d":
            new_head = Position(self.ls_p[0].get_x(), self.ls_p[0].get_y())
            new_head.xpos += 1
            self.ls_p.insert(0, new_head)
            for x in range(len(self.ls_p) - 1, 1, -1):
                self.ls_p[x].xpos = self.ls_p[x-1].xpos
                self.ls_p[x].ypos = self.ls_p[x-1].ypos
            self.ls_p.pop(1)
        #Left
        if self.direction == "a":
            new_head = Position(self.ls_p[0].get_x(), self.ls_p[0].get_y())
            new_head.xpos -= 1
            self.ls_p.insert(0, new_head)
            for x in range(len(self.ls_p) - 1, 1, -1):
                self.ls_p[x].xpos = self.ls_p[x-1].xpos
                self.ls_p[x].ypos = self.ls_p[x-1].ypos
            self.ls_p.pop(1)
        #Up
        if self.direction == "w":
            new_head = Position(self.ls_p[0].get_x(), self.ls_p[0].get_y())
            new_head.ypos -= 1
            self.ls_p.insert(0, new_head)
            for x in range(len(self.ls_p) - 1, 1, -1):
                self.ls_p[x].xpos = self.ls_p[x-1].xpos
                self.ls_p[x].ypos = self.ls_p[x-1].ypos
            self.ls_p.pop(1)
        #Down
        if self.direction == "s":
            new_head = Position(self.ls_p[0].get_x(), self.ls_p[0].get_y())
            new_head.ypos += 1
            self.ls_p.insert(0, new_head)
            for x in range(len(self.ls_p) - 1, 1, -1):
                self.ls_p[x].xpos = self.ls_p[x-1].xpos
                self.ls_p[x].ypos = self.ls_p[x-1].ypos
            self.ls_p.pop(1)

    def change_direction(self, direction_string):
        """
        Screen out duplicate and invalid directions
        change direction

        """
        if self.direction in ["a", "d"] and direction_string not in ["a", "d"]:
            self.direction = direction_string
        elif self.direction in ["w", "s"] and direction_string not in ["w", "s"]:
                self.direction = direction_string

    def grow(self):
        """
        Add new position. Same as move() but doesn't pop old head
        """
        new_tail = Position(self.ls_p[-1].get_x(), self.ls_p[-1].get_y())
        self.ls_p.append(new_tail)
        self.ls_c.append("+")
        for x in range(len(self.ls_p) - 1, 1, -1):
            self.ls_p[x].xpos = self.ls_p[x-1].xpos
            self.ls_p[x].ypos = self.ls_p[x-1].ypos

    def collides_tail(self):
        """
        Start at end because most likely to get hit,
        2nd pos is impossible to hit
        """
        for position in self.current_pos()[-1:2:-1]:
            if self.current_pos()[0].equals(position) == True:
                    return True

    def explosion(self):
        """
        Stop snake movement and draw explosion
        """
        self.gui.clear()
        self.draw(self.gui)
        self.gui.draw_text("*", self.init.xpos, self.init.ypos,
                           "PURPLE", "YELLOW")
        self.gui.refresh()
        time.sleep(0.2)
        self.gui.clear()
        self.draw(self.gui)
        self.gui.draw_text("*", self.init.xpos + 1, self.init.ypos,
                          "PURPLE", "YELLOW")
        self.gui.draw_text("*", self.init.xpos, self.init.ypos + 1,
                          "PURPLE", "YELLOW")
        self.gui.draw_text("*", self.init.xpos, self.init.ypos - 1,
                          "PURPLE", "YELLOW")
        self.gui.draw_text("*", self.init.xpos -1, self.init.ypos,
                          "PURPLE", "YELLOW")
        self.gui.refresh()
        time.sleep(0.1)
        self.gui.clear()
        self.draw(self.gui)
        self.gui.draw_text("*", self.init.xpos, self.init.ypos,
                           "PURPLE", "YELLOW")
        self.gui.draw_text("*", self.init.xpos + 1, self.init.ypos - 1,
                          "PURPLE", "YELLOW")
        self.gui.draw_text("*", self.init.xpos + 1, self.init.ypos + 1,
                          "PURPLE", "YELLOW")
        self.gui.draw_text("*", self.init.xpos - 1, self.init.ypos - 1,
                          "PURPLE", "YELLOW")
        self.gui.draw_text("*", self.init.xpos -1, self.init.ypos + 1,
                          "PURPLE", "YELLOW")
        self.gui.refresh()
        time.sleep(0.1)
        self.gui.clear()

    def wham(self):
        # This looks complicated until you read it. It's just drawing characters.
        self.gui.clear()
        self.draw(self.gui)
        self.gui.refresh()
        time.sleep(0.05)
        self.gui.clear()
        # Different cases for L and R side of screen to prevent draw errors at corner cases
        # L side
        if self.direction in ["w", "s"] and self.current_pos()[0].xpos <= self.init.xpos:
            self.gui.draw_text("W", self.current_pos()[0].xpos - 1, self.current_pos()[0].ypos,
                               "RED", "CYAN")
            self.gui.draw_text("H", self.current_pos()[0].xpos, self.current_pos()[0].ypos,
                              "RED", "ORANGE")
            self.gui.draw_text("A", self.current_pos()[0].xpos + 1, self.current_pos()[0].ypos,
                              "RED", "CYAN")
            self.gui.draw_text("M", self.current_pos()[0].xpos + 2, self.current_pos()[0].ypos,
                              "RED", "MAGENTA")
        elif self.direction in ["a", "d"] and self.current_pos()[0].xpos <= self.init.xpos:
            self.gui.draw_text("W", self.current_pos()[0].xpos, self.current_pos()[0].ypos - 1,
                               "RED", "CYAN")
            self.gui.draw_text("H", self.current_pos()[0].xpos, self.current_pos()[0].ypos,
                              "RED", "ORANGE")
            self.gui.draw_text("A", self.current_pos()[0].xpos, self.current_pos()[0].ypos + 1,
                              "RED", "CYAN")
            self.gui.draw_text("M", self.current_pos()[0].xpos, self.current_pos()[0].ypos + 2,
                              "RED", "MAGENTA")
        # R side
        else:
            if self.direction in ["w", "s"]:
                self.gui.draw_text("W", self.current_pos()[0].xpos - 2, self.current_pos()[0].ypos,
                                   "RED", "CYAN")
                self.gui.draw_text("H", self.current_pos()[0].xpos - 1, self.current_pos()[0].ypos,
                                  "RED", "ORANGE")
                self.gui.draw_text("A", self.current_pos()[0].xpos, self.current_pos()[0].ypos,
                                  "RED", "CYAN")
                self.gui.draw_text("M", self.current_pos()[0].xpos + 1, self.current_pos()[0].ypos,
                                  "RED", "MAGENTA")
            elif self.direction in ["a", "d"]:
                self.gui.draw_text("W", self.current_pos()[0].xpos, self.current_pos()[0].ypos - 2,
                                   "RED", "CYAN")
                self.gui.draw_text("H", self.current_pos()[0].xpos, self.current_pos()[0].ypos - 1,
                                  "RED", "ORANGE")
                self.gui.draw_text("A", self.current_pos()[0].xpos, self.current_pos()[0].ypos,
                                  "RED", "CYAN")
                self.gui.draw_text("M", self.current_pos()[0].xpos, self.current_pos()[0].ypos + 1,
                                  "RED", "MAGENTA")

        self.gui.refresh()
        time.sleep(0.4)
        self.gui.clear()
        self.draw(self.gui)
        self.gui.refresh()
