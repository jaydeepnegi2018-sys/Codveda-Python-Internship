import random

secret_number = random.randint(1, 100)
max_attempts = 7

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number correctly.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"Game Over! The correct number was {secret_number}")
