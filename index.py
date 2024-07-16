import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid. Try again!")
        continue

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has started")
        print("Your total score at the moment is", players_score[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                current_score = 0
                print("\nYou rolled a 1. Turn finished.")
                break
            else:
                current_score += value
                print("You rolled a", value)
            print("Your score is", current_score)

        players_score[player_idx] += current_score
        print("\nYour total score is", players_score[player_idx], "\n")

win_score = max(players_score)
winning_idx = players_score.index(win_score)
print("\n\nThe winner is player numer", winning_idx + 1)
