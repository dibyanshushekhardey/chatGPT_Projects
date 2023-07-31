import random

def hangman():
    # List of words to choose from
    word_list = ['python', 'hangman', 'game', 'programming', 'computer']

    # Select a random word from the list
    secret_word = random.choice(word_list)

    # Create a list to store the guessed letters
    guessed_letters = []

    # Initialize the number of attempts
    attempts = 6

    while True:
        # Display the current status of the word
        current_word = ''
        for letter in secret_word:
            if letter in guessed_letters:
                current_word += letter + ' '
            else:
                current_word += '_ '
        print("Current word:", current_word)

        # Prompt the user to enter a letter
        guess = input("Enter a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter. Please try again.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in secret_word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        # Check if the player has won or lost
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You won!")
            break
        elif attempts == 0:
            print("Game over! You lost. The word was:", secret_word)
            break

        # Display the number of attempts left
        print("Attempts left:", attempts)

def main():
    print("Welcome to Hangman!")
    hangman()

if __name__ == '__main__':
    main()
