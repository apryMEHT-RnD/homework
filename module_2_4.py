numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    is_prime = True
    i = numbers[i]
    if i < 2:
        continue
    else:
        j = i ** (1 / 2)
        for j in range(2, int(j +1)):
            if i % j == 0:
                is_prime = False
                break
        if not is_prime:
            not_primes.append(i)
        else:
            primes.append(i)
print("Primes: ", primes)
print("Not Primes: ", not_primes)



