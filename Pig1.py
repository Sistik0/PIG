import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit() and 2 <= int(players) <=4:
        players = int(players)
        break
    else:
        print("Invalid input. Please enter a number between 2 and 4.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "its your turn!\n")
        print("Your total score is:",(player_scores[player_idx]), "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n)? ").lower()
            if should_roll != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a",str(value) + "!")

            print("Your score is:", current_score)
        
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winder with a score of:", max_score)