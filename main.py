numbers = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_numbers = [num for num in numbers if is_prime(num)]
print("Liczby pierwsze:", prime_numbers)