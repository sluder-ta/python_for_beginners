import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player}, and the computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock! You lose."
        else:
            return "Rock smashes scissors! You win!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut paper! You lose."
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        else:
            return "Scissors cut paper! You win!"

game_choices = get_choices()
print(check_win(game_choices["player"], game_choices["computer"]))