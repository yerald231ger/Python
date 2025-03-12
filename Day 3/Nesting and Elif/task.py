print("Welcome to the rollercoaster!")

exit_code = 1
while exit_code == 1:
    height = int(input("What is your height in cm? "))
    age = int(input("What age are you? "))
    bill = 0

    if height >= 120 and age >= 12:
        print("You can ride the rollercoaster")
        if age >= 55:
            bill = 5
        elif 12 <= age <= 15:
            bill = 3
        elif age < 18:
            bill = 7
        else:
            bill = 12

        wants_photo = input("Do you want a photo taken? Y or N: ")
        if wants_photo == "Y":
            print("Photo taken")
            bill += 3
        else:
            print("No photo taken")

        print(f"Your total bill is ${bill}")

        exit_code = 0
    else:
        print("Sorry you have to grow taller before you can ride.")
        exit_code = 1
