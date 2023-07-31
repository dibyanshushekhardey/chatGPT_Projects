import random
import string

def generate_password(length):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Prompt the user for the desired password length
    length = int(input("Enter the length of the password: "))

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == '__main__':
    main()
