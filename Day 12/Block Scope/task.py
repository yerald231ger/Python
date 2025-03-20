
# get the remaining number of a division
def is_prime_number(num1):
    if num1 == 1:
        return False
    for i in range(2, num1):
        if num1 % i == 0:
            return False
    return True


result = is_prime_number(7)
