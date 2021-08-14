def end_game(player_score, state="OFF"):
    if player_score < 30:
        print("Your score was: " + str(player_score) + " (- . -)")
        print("Warm those fingers up, you'll do better next time!")
    elif 30 < player_score < 100:
        print("Your score was: " + str(player_score) + " <(^ - ^)^")
    elif player_score > 100:
        print("Your score was: " + str(player_score) + "（╯°□°）╯︵ ┻━┻")
    if state in ["SNAKE", "WALL"]:
        if state == "SNAKE":
            print("Stop hitting yourself")
        if state == "WALL":
            print("That's probably a concussion, don't hit walls")
        else:
            pass
