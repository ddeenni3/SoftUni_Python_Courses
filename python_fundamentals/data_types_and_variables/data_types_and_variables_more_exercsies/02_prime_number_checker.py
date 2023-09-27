def is_prime(number):
    prime = True
    for num in range(2, number):
        if number % num == 0:
            prime = False
            break
    return prime


print(is_prime(int(input())))
