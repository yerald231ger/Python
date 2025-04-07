def divide_numbers(a, b, index):
    try:
        fruits = ["Apple", "Pear", "Orange"]
        fruit = fruits[index]
        print(fruit)
        
        # Attempt to perform division
        if b == 0:
            # Raise (throw) an exception manually
            raise ValueError("Cannot divide by zero!")
        
        result = a / b
        
    except ValueError as ve:
        # Handle the specific ValueError exception
        print(f"Value Error: {ve}")
    except IndexError as ie:
        # Handle the specific IndexError exception
        print(f"Index Error: {ie}")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An error occurred: {e}")
    else:
        # This block runs if no exceptions were raised
        print(f"The result is: {result}")
    finally:
        # This block always executes, regardless of exceptions
        print("Division operation completed")

# Test the function
print("Example 1: Valid division")
divide_numbers(10, 2, 0)

print("\nExample 2: Division by zero")
divide_numbers(10, 0, 0)

print("\nExample 3: Invalid input type")
divide_numbers("10", 2, 0)

print("\nExample 4: Index out of range")
divide_numbers(10, 2, 4)
