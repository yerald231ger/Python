import random

stages = [r'''
  ┟───┐
  ┊   │
  O   │
 /│\  │
 / \  │
      │
▔▔▔▔▔▔▔▔▔
''', r'''
  ┟───┐
  ┊   │
  O   │
 /│\  │
 /    │
      │
▔▔▔▔▔▔▔▔▔
''', r'''
  ┟───┐
  ┊   │
  O   │
 /│\  │
      │
      │
▔▔▔▔▔▔▔▔▔
''', '''
  ┟───┐
  ┊   │
  O   │
 /│   │
      │
      │
▔▔▔▔▔▔▔▔▔''', '''
  ┟───┐
  ┊   │
  O   │
  │   │
      │
      │
▔▔▔▔▔▔▔▔▔
''', '''
  ┟───┐
  ┊   │
  O   │
      │
      │
      │
▔▔▔▔▔▔▔▔▔
''', '''
  ┟───┐
  ┊   │
      │
      │
      │
      │
▔▔▔▔▔▔▔▔▔
''']

RED_START = "\033[1;31m"
RED_END = "\033[0;0m"
BLUE_START = "\033[1;34m"
BLUE_END = "\033[0;0m"
word_list = ["hamstrings"]

chosen_word = random.choice(word_list)
print("\nThe Hangman Game")

placeholder = ["_"] * len(chosen_word)
print()
tries = len(stages) - 1

while tries >= 0:

    guess = input("Guess a letter: ").lower()

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            placeholder[index] = letter

    print(f"\nYou have {tries} tries left.")

    displayed = "".join(placeholder)

    print()
    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")

    print(stages[tries])
    if guess not in chosen_word:
        tries -= 1
        print(f"{RED_START}the letter is not in the word{RED_END}")

    print(" " + BLUE_START + displayed + BLUE_END)
    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")

    if displayed == chosen_word:
        print("\nYou WIN.")
        exit(0)

print("\nYou lose.")
