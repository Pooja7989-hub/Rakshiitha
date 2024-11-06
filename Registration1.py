import random

def guess_the_number():
    print("Welcome to the 'Guess the Number' game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Select a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        # Get the player's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        # Check the player's guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
    guess_the_number()
