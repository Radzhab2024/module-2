numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#numbers = [4, 5]
primes = []
not_primes = []
for i in range(len(numbers)):
    counter = 0
    is_prime = False
    num = numbers[i]
    for j in range(num + 1):
        if j == 0:
            continue
        elif num % j == 0:
            counter += 1
    if counter <= 2:
        is_prime = True
    else:
        is_prime = False
    if is_prime == True:
        primes.append(num)
    else:
        not_primes.append(num)
print(f'primes = {primes}, not_primes = {not_primes}')





