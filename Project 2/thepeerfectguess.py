import random

def play_perfect_guess():
    """
    A simple number guessing game.

    The computer selects a random number between a specified range,
    and the user has to guess it. The game provides feedback on whether
    the guess is too high or too low.
    """
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    target_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    guess_count = 0
    
    print("I'm thinking of a number between {} and {}. Can you guess it?".format(MIN_NUMBER, MAX_NUMBER))

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            guess_count += 1

            if user_guess < target_number:
                print("Your guess is too low.")
            elif user_guess > target_number:
                print("Your guess is too high.")
            else:
                print(f"Congratulations! You've guessed the number {target_number} in {guess_count} guesses.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    play_perfect_guess()