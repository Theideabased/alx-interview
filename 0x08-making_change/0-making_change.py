#!/usr/bin/python3
"""Module to determine the fewest number of coins needed to meet a given
total."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
    coins (list): A list of the coin denominations available.
    total (int): The total amount to reach with the fewest coins.

    Returns:
    int: Fewest number of coins needed to reach the total, or -1 if it
    cannot be done.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to use the largest coin first
    coins.sort(reverse=True)

    coin_count = 0  # To keep track of how many coins are used
    for coin in coins:
        if total == 0:
            break  # If total becomes zero, stop

        # Use as many of this coin as possible
        num_coins = total // coin
        coin_count += num_coins
        total -= num_coins * coin

    # If after all this, the total isn't 0, it means we couldn't match the
    # exact total
    if total != 0:
        return -1

    return coin_count
