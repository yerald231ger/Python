print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")

while size != "S" and size != "M" and size != "L":
    print("Invalid size. Please enter S, M or L.")
    size = input("What size pizza do you want? S, M or L: ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

while pepperoni != "Y" and pepperoni != "N":
    print("Invalid option. Please enter Y or N.")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")

while extra_cheese != "Y" and extra_cheese != "N":
    print("Invalid option. Please enter Y or N.")
    extra_cheese = input("Do you want extra cheese? Y or N: ")

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
