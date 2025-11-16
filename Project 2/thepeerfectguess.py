import random
n = random.randint(1, 100)
guesses = 1
a = -1
while (a != n):
    a = int(input("Enter your guess: "))
    if (a < n):
        print("Your guess is too low.")
        guesses += 1
    elif (a > n):
        print("Your guess is too high.")
        guesses += 1

print(f"Congratulations! You've guessed the number {n} in {guesses} guesses.")