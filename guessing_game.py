import random
import time

# A welcome message and the game rules
print("=" * 60)
print("       🎮 Welcome to the Number Guessing Game! 🎮")
print("=" * 60)
print()
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.")
print()
print("Wishing you all the best! 🍀")
print()
print("=" * 60)
print()

# Select difficulty level
print("Please select the difficulty level:")
print()
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")
print()

choice = input("Enter your choice (1, 2, or 3): ")
print()

# Defining each difficulty level based on the user's choice
if choice == "1":
    difficulty = "Easy"
    chances = 10
elif choice == "2":
    difficulty = "Medium"
    chances = 5
elif choice == "3":
    difficulty = "Hard"
    chances = 3
else:
    print("‼️ Invalid choice! Please restart the game. ‼️")
    exit()

# Confirm selection message
print(f"Great! You have selected the {difficulty} difficulty level.")
print(f"You are given {chances} chances to guess the number.")
print("Let's start the game! Are you ready?")
print()
print("=" * 60)
print()

# Set up the range and generate a random number
lower_bound = 1
upper_bound = 100
max_attempts = chances
secret_number = random.randint(1, 100)

# Read in the user's input
def get_guess():
    while True:
        try:
            guess = int(input(f"Enter your guess: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input. Please enter the number within a specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Validate the user's guess
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Lower"
    else:
        return "Greater"
    
# Track the number of attempts and detect end-of-game conditions
def play_game():
    # Generate a NEW random number for each game
    secret_number = random.randint(1, 100)
    
    # Start the timer for THIS round
    start_time = time.time()

    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "Correct":

            # Stop the timer when the guess is correct
            end_time = time.time()

            # Calculate the duration
            duration = end_time - start_time

            # Display the message and time taken
            print(f"🎉 Congratulations! You guessed the correct number in {attempts} attempts.")
            print(f"⏱️  You finished the game in {duration:.2f} seconds.")

            won = True
            break
        elif result == "Lower":
            print(f"❌ Incorrect! The secret number is greater than {guess}.")
        else:
            print(f"❌ Incorrect! The secret number is lower than {guess}.")
        
        print(f"Attempts remaining: {max_attempts - attempts}")
        print()

    if not won:
        end_time = time.time()
        duration = end_time - start_time
        print(f"😢 Sorry, you ran out of attempts! The secret number was {secret_number}.")
        print(f"⏱️  You tried for {duration:.2f} seconds.")

# Main game loop
while True:
    play_game()
    
    # Ask the user if they want to play again
    play_again = input("Do you want to play another round? (yes/no): ")

    # Check the user's input to break the loop
    if play_again.lower() != "yes":
        print("Thanks for playing! Bye bye ^^")
        break