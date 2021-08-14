"""
This is the main program for the snake game. See READ_ME.
"""

import time
from position import Position
from gui import Gui
from room import Room
from snake import Snake
from apple import Apple, collides
from end_game import end_game

# Game speed modifier, putting it here keeps debugging simple.
# DO NOT MOVE. See Line 33 for init speed, Lines 45 - 59 for ingame arg
def game_speed(speed):
    if speed < 0.03:
        speed = 0.03
    time.sleep(speed)

def main():


    try:
        # Create the new Gui and start it. This clears the screen
        # and the Gui now controls the screen
        gui = Gui()
        # Create the room, the snake and the apples.
        room = Room(gui.get_width(), gui.get_height(), "#", "WHITE", "BLUE")
        snake = Snake()
        apple = Apple()
        apple_two = Apple()
        apple_three = Apple()
        speed = 0.1
        # Switch for args passed to end_game
        # ALSO USED to trip apple relocation
        state="OFF"
        # The main loop of the game. Use "break" to break out of the loop
        continuePlaying = True
        player_score = 0
        # If there's too many apples game gets too easy, keep low, implement an append if want mechanics are there
        apples_in_play = [apple, apple_two, apple_three]
        while continuePlaying:
            # Get a key press from the user
            c = gui.get_keypress()
            # Check for apple relocation and modify speed. See line 81 for next
            if state == "OFF":
                pass
            elif state == "APPLE":
                apple.is_eaten()
                speed -= float(0.02)
                state = "OFF"
            elif state == "APPLE TWO":
                 apple_two.is_eaten()
                 speed -= float(0.02)
                 state = "OFF"
            elif state == "APPLE THREE":
                apple_three.is_eaten()
                speed -= float(0.02)
                state = "OFF"
            # Force Apple outside snake
            # By default Apple does not draw on base case walls
            # IF Apple COLLIDES additional walls isn't checked until walls are triggered
            # Lines 97 and 107 force Apple outside walls
            if player_score < 30:
                while collides(apple.position, snake.current_pos()) == True:
                    apple.is_eaten()
            elif 30 < player_score < 80:
                while collides(apple.position, snake.current_pos()) == True:
                    apple.is_eaten()
                while collides(apple_two.position, snake.current_pos()) == True:
                    apple_two.is_eaten()
            elif player_score >= 80:
                while collides(apple.position, snake.current_pos()) == True:
                    apple.is_eaten()
                while collides(apple_two.position, snake.current_pos()) == True:
                    apple_two.is_eaten()
                while collides(apple_three.position, snake.current_pos()) == True:
                    apple_three.is_eaten()
            else:
                pass
            # Do something if the user wants to quit
            # Do something depending on what was pressed
            if c == "q":
                continuePlaying = False
            elif c in ["w", "a", "s", "d"]:
                snake.change_direction(c)
            # Base case for animation
            # See lines 115 - 129
            snake.move()
            gui.clear()
            # Draw procedure triggered by game phase
            if player_score < 30:
                pass
            elif 30 < player_score < 80:
                room.draw_first_line(gui)
                apple_two.draw(gui)
                # Force Apple outside one wall, two apples in play, if implement append change this
                for item in apples_in_play[0:1]:
                    while item.xpos == gui.get_width()//2 and 5 <= item.ypos <= gui.get_height() - 6:
                        item.is_eaten()
                    else:
                        pass
            elif player_score >= 80:
                room.draw_two_lines(gui)
                apple_two.draw(gui)
                apple_three.draw(gui)
                # Force Apple outside two walls
                for item in apples_in_play:
                    while item.xpos == gui.get_width()//4 and item.ypos < gui.get_height() - 6:
                        item.is_eaten()
                    while item.xpos == (gui.get_width()//4)*3 and item.ypos < 5:
                        item.is_eaten()
                    else:
                        pass
            # Scoreboard and Base case for animation, Lines 89 - 90 included in this
            if player_score == 00:
                gui.draw_text(str(player_score)[0], gui.get_width()//2 - 1, 0,
                    "BLACK", "RED")
                gui.draw_text(str(player_score)[0], gui.get_width()//2, 0,
                    "BLACK", "RED")
            else:
                gui.draw_text(str(player_score)[0], gui.get_width()//2 - 1, 0,
                    "BLACK", "RED")
                gui.draw_text(str(player_score)[1], gui.get_width()//2, 0,
                    "BLACK", "RED")
            room.draw(gui)
            apple.draw(gui)
            snake.draw(gui)
            gui.refresh()
            # Detect whether the snake ate an apple, or it hit the wall
            # or it hit its own tail, and pass args if True
            if snake.current_pos()[0].equals(apple.position) == True:
                player_score += 10
                state = "APPLE"
                snake.grow()
                game_speed(speed)
                gui.clear()
                snake.draw(gui)
                room.draw(gui)
                if 30 < player_score < 80:
                    room.draw_first_line(gui)
                    apple_two.draw(gui)
                elif player_score >= 80:
                    room.draw_two_lines(gui)
                    apple_two.draw(gui)
                    apple_three.draw(gui)
                gui.refresh()
            # Start collision detection if additional apple is in play
            elif player_score > 30:
                if snake.current_pos()[0].equals(apple_two.position) == True:
                    player_score += 10
                    state = "SECOND APPLE"
                    snake.grow()
                    game_speed(speed)
                    gui.clear()
                    snake.draw(gui)
                    room.draw(gui)
                    if player_score < 80:
                        room.draw_first_line(gui)
                        apple.draw(gui)
                    elif player_score >= 80:
                        room.draw_two_lines(gui)
                        apple.draw(gui)
                        apple_three.draw(gui)
                    gui.refresh()
            # Start collision detection if additional apple is in play
            elif player_score >= 80:
                if snake.current_pos()[0].equals(apple_three.position) == True:
                    player_score += 10
                    state = "THIRD APPLE"
                    snake.grow()
                    game_speed(speed)
                    gui.clear()
                    snake.draw(gui)
                    room.draw(gui)
                    room.draw_two_lines(gui)
                    apple.draw(gui)
                    apple_two.draw(gui)
                    gui.refresh()
            # Tail collision
            if snake.collides_tail() == True:
                state = "SNAKE"
                snake.wham()
                snake.explosion()
                break
            # Wall collision
            if snake.current_pos()[0].xpos in [0, gui.get_width() - 1]:
                state = "WALL"
                snake.wham()
                snake.explosion()
                break
            if snake.current_pos()[0].ypos in [0, gui.get_height() - 1]:
                state = "WALL"
                snake.wham()
                snake.explosion()
                break
            if snake.current_pos()[0].xpos == gui.get_width()//2 and 5 <= snake.current_pos()[0].ypos <= gui.get_height() - 6:
                if 30 < player_score < 80:
                    state = "WALL"
                    snake.wham()
                    snake.explosion()
                    break
            if snake.current_pos()[0].xpos == gui.get_width()//4 and snake.current_pos()[0].ypos <= gui.get_height() - 6:
                if player_score >= 80:
                    state = "WALL"
                    snake.wham()
                    snake.explosion()
                    break
            if snake.current_pos()[0].xpos == (gui.get_width()//4)*3 and snake.current_pos()[0].ypos >= 5:
                if player_score >= 80:
                    state = "WALL"
                    snake.wham()
                    snake.explosion()
                    break
            # This call makes the program go quiescent for some time, so
            # that it doesn't run so fast.
            # Line 13 for function definition
            # Line 31 for initial speed on game launch
            game_speed(speed)
    except Exception as e:
        # Some error occured, so we catch it, clear the screen,
        # print the log output, and then reraise the Exception
        # This will cause the program to quit and the error will be displayed
        gui.quit()
        raise e
    # Stop the GUI, clearing the screen and restoring the screen
    # back to its original state. Print the saved log output
    gui.quit()
    # The game has ended since we broke out of the main loop
    # Display the user's score here
    end_game(player_score, state)


if __name__ == "__main__":
    main()
