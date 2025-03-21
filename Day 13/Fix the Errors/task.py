def get_age():
    valid_age = 0
    while valid_age < 1:
        try:
            valid_age = int(input("How old are you?"))
        except ValueError:
            print("Please enter a number.")

    return valid_age


age = get_age()

if age < 18:
    print(f"You can drive at age {age}.")


