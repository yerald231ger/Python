import random
import my_module

numbers_to_generate = int(input("How many random numbers do you want to generate? "))
list_of_random_numbers = []

for _ in range(numbers_to_generate):
    list_of_random_numbers.append(random.randint(1, 10))

print("How many times each number was generated:")

for number in range(1, 11):
    print(f"{number}: {list_of_random_numbers.count(number)}")

print("By the way, my favourite number is", my_module.my_favourite_number)
print(my_module.function)
print(my_module.function_with_parameters("Hello"))

