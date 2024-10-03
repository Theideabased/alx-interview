#!/usr/bin/python3
"""Given a pile of coin with different values print out
the fewest number needed to give and amount"""


def makechange(coins, total):
    """ coin is a list and how main element of the coin will
    be added to get the total
    makechange(coin, total)
    Return: 0 if total is 0
    -1 if sum of coin is greater than total
    -1 if no amount of coin element will give total"""
    sorted_coin = sorted(coins, asc=True)
    if total = 0:
        return 0
    for coin in range(len(sorted_coin)):
        list_total = list_total + sorted_coins[coin]
        if list_total >= total:
            return -1
        elif list_total == total:
            return len(sorted_coin)

