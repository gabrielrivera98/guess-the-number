import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
attempts = 10
guess = 0
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'hard':
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.\nGuess again.")
        attempts -= 1
    elif guess < number:
        print("Too low.\nGuess again.")
        attempts -= 1
    else:
        print(f"You got it! the answer was {number}")
        break
