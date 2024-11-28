#!/usr/bin/python3
"""Module to determine the fewest number of coins needed to meet a given
total."""
from typing import List


def makeChange(coins: List[int], total: int):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
    coins (list): A list of the coin denominations available.
    total (int): The total amount to reach with the fewest coins.

    Returns:
    int: Fewest number of coins needed to reach the total, or -1 if it
    cannot be done.
    """
    coin_length = len(coins)
    for i in range(coin_length):
        for j in range(0, coin_length - i - 1):
            if coins[j] > coins[j + 1]:
                coins[j], coins[j+1] = coins[j+1], coins[j]
    used_coins = []
    n = len(coins)
    i = n - 1
    while (i >= 0):
        while (total >= coins[i]):
            total -= coins[i]
            used_coins.append(coins[i])
        i -= 1    
    return(len(used_coins))
