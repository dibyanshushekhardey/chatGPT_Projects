import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize the number of attempts
    attempts = 0

    while True:
        # Ask the user to enter their guess
        guess = int(input("Guess the number (between 1 and 100): "))
        
        # Increment the number of attempts
        attempts += 1

        # Compare the guess with the secret number
        if guess == secret_number:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break
        elif guess < secret_number:
            print("Try again! The number is higher.")
        else:
            print("Try again! The number is lower.")

def main():
    print("Welcome to the Guess the Number game!")
    guess_number()

if __name__ == '__main__':
    main()
