#!/usr/bin/python3
"""Maria and Ben are playing a game. Given a set of
consecutive integers starting from 1 up to and including n"""


def isWinner(x, nums):
    """They play x rounds of the game, where n may be different for
    each round. Assuming Maria always goes first and both players
    play optimally, determine who the winner of each game is."""
    # Step 1: Edge case
    if x <= 0 or not nums:
        return None
    
    # Step 2: Find the largest n in nums to optimize prime calculations
    max_n = max(nums)
    
    # Step 3: Use Sieve of Eratosthenes to find all prime numbers up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    
    # Step 4: Precompute the number of primes up to each number n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)
    
    # Step 5: Simulate the rounds
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    # Step 6: Determine the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

