number_to_check = int(input("What number do you want to check? "))

number_to_check = number_to_check % 2
print(f"The result is: {number_to_check}")

if number_to_check == 0:
    print("The result is even")
else:
    print("The result is odd")
