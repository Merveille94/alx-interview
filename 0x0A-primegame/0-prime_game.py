#!/usr/bin/python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_count(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    count = 0

    for i in range(2, n + 1):
        if primes[i]:
            count += 1
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return count


def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)
    prime_counts = [prime_count(i) for i in range(max_n + 1)]

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

