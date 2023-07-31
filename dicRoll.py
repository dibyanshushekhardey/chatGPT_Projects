import random

def roll_dice():
    # Simulate rolling a dice
    dice_value = random.randint(1, 6)
    return dice_value

def main():
    # Ask the user for the number of dice rolls
    num_rolls = int(input("Enter the number of times you want to roll the dice: "))

    # Roll the dice and display the results
    print("Rolling the dice", num_rolls, "times:")
    for _ in range(num_rolls):
        dice_roll = roll_dice()
        print("Dice rolled:", dice_roll)

if __name__ == '__main__':
    main()
