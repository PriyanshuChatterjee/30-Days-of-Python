import math

def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i == 0):
            return False

        else:
            return True

print(is_prime(12))          