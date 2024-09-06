"""
Problem Statement:
The decimal number, 585 = 1001001001 in binary and is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
Please note that the palindromic number, in either base, may not include leading zeros.

Computational Analysis: This program is pretty simply O(n), as the palindromic checks on each
number takes constant time and we iterate through each. It's also constant space.

DSA: This is a brute-force check on all potential numbers under the input; we do not directly
compute the palindromes, but instead check all candidates in the search space. We employ
pretty simple string manipulation in the palindromic check.

Math: No real math principles used here. We abstract away the binary conversion using Python's
built-in library methods. 

"""

"""
Program Attempt 1:
This seems like a relatively straightforward brute-force check on all numbers less
than X. I was wondering if it made sense to construct a list of all decimal-based
palindromes from the bottom-up (so we don't have to iterate through all numbers
under X), but that is a bit complicated. I was also thinking of doing a union
operation between constructing a list of all decimal-based palindromes and all
binary-based palindromes, but that also seems complicated and less efficient. Let's
keep it simple.
"""


def is_decimal_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def is_binary_palindrome(n: int) -> bool:
    return bin(n)[2:] == bin(n)[2:][::-1]


def main(n: int) -> int:
    sum = 0
    for i in range(n):
        sum += i if is_binary_palindrome(i) and is_decimal_palindrome(i) else 0

    return sum


if __name__ == "__main__":
    ans = main(1000000)
    print(ans)
