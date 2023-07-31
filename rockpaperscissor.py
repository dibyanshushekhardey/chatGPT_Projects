import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    choices = ['rock', 'paper', 'scissors']

    while True:
        # Prompt the user for their choice
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        # Check if the user's choice is valid
        if player_choice not in choices:
            print("Invalid choice! Please try again.")
            continue

        # Randomly select the computer's choice
        computer_choice = random.choice(choices)

        print("Your choice:", player_choice)
        print("Computer's choice:", computer_choice)

        # Determine and display the winner
        winner = determine_winner(player_choice, computer_choice)
        print(winner)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == '__main__':
    play_game()
