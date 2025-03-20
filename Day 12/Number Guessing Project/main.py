import random

print("GUESS THE NUMBER GAME")
print("I'm thinking of a number between 1 and 100...")
print("How difficult do you want the game to be?\n\n Type 'easy' or 'hard': ")
difficulty = input().lower()

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

number_to_guess = random.randint(1, 100)

print(f"You have {attempts} attempts to guess the number.")
print("OK, let's start guessing... type a number: ")

while attempts > 0:
    num = int(input())

    if num == number_to_guess:
        print("Congratulations! You guessed the number.")
    else:
        how_far = abs(number_to_guess - num)

        if num > number_to_guess:
            if how_far >= 40:
                print("Too way high.")
            elif how_far > 20:
                print("Too High")
            elif how_far > 10:
                print("Bit High")
            else:
                print("High")
        else:
            if how_far >= 40:
                print("Too way low.")
            elif how_far >= 20:
                print("Too Low.")
            elif how_far >= 10:
                print("Bit Low.")
            else:
                print("Low.")

        attempts -= 1

        print(f"You have {attempts} attempts left. Try again: ")

print("The number was: ", number_to_guess)
print("You ran out of attempts. Game over.")
