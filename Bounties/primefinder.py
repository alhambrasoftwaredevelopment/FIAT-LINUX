def get_primes(n):
    numbers = set(range(n, 1, -1))  # sets up the range to be a set (no repeats) and run backwards
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    print(primes)


get_primes(999)
