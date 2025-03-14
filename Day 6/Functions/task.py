import random


# def write_line_code_in_blue(text):
#     print(f"\033[34m{text}\033[0m")
#
#
# text_input = input("Which phrase do you want to write in green? \n")
# write_line_code_in_blue(text_input)

magic_number = random.randint(1, 100)
# print the magic number in light gray
print(f"\033[37m{magic_number}\033[0m")

number = int(input("What is the magic number?"))

while number is not magic_number:
    print("That is not the magic number, try again? \n")
    number = int(input())

print("You found the magic number!")
