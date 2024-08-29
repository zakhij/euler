"""
Problem Statement:
In the United Kingdom the currency is made up of pound (£) and pence (p). 
There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?

Computational Analysis: Given a static coin distribution, we determine
this problem is O(n) in both time and space complexity: the amount of
work performed per coin scales with n, and so does the table size.

DSA: This is a classic dynamic programming problem. We use a list to store 
the number of ways each amount can be constructed, building on previously 
computed values to fill out the table for larger amounts, which avoids 
recalculating solutions for smaller subproblems.

Math: The problem involves combinatorial principles, calculating the number 
of combinations of coin denominations that can sum up to various amounts.

"""

"""
Program Attempt 1:
Okay so this is a combinatorics problem. When I look at it, I intuit that the 
solution is recursive, some dynamic programming implementation. Like, we'll
look at how many ways we can make $1, and that sub-problem builds up to the
larger overall problem of making $2. Yes, exactly. We initialize a tab of how
many ways to build up every amount up to $2, then build up each entry by
looking at previous entries. 
"""


def count_ways_to_make_amount(amount):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]

    return ways[amount]


if __name__ == "__main__":
    ans = count_ways_to_make_amount(200)
    print(ans)
