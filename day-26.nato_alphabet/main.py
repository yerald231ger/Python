import pandas

NATO_ALPHABET = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_ALPHABET_DICT = {row.letter: row.code for (index, row) in NATO_ALPHABET.iterrows()}

print(NATO_ALPHABET_DICT)

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        output_list = [NATO_ALPHABET_DICT[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()