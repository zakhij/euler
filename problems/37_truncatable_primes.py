"""
Problem Statement:
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove 
digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Computational Analysis: It's difficult to assign a computational complexity in relation to an input size,
as there is no clearly defined input in this problem. However, we can say that we iterate from 11 up
all the way to the 11th truncatable prime, checking for primality along the way. Checking for 
trunacatable primality is O(sqrt(n)) (we perform this operation an X number of times, where X is digit length). 
If we designate n as the number of integers we iterate through, then our solution in total is O(nsqrt(n)).

DSA: Our solution is ultimately another brute-force, explore-the-potential-solution-space problem, as
we iterate up and check each potential candidate for trunacatable primality. We leverage an efficient
primality check algorithm as a helper function along the way.

Math: This problem is concerned with prime numbers, yet does not make considerable use of prime numbers' unique 
properties. We do exploit the property of truncatable primes needing to end in a 1/3/7 as a micro-optimization
for our iteration.

"""

"""
Program Attempt 1:
The brute force strategy seems quite simple: iterate up from 10, checking each number
for primality. If yes, then check if it's a truncatable prime (via helper functions).
Stop iterating once we have 11 such cases. 
However, I'm wondering if we can craft a smarter approach through some observations:
- The left-to-right truncatable prime must end with a 1, 3, or 7 (multi-digit
numbers that end with 2 or 5 are never prime).
- The right-to-left truncatable prime must start with a 1, 2, 5, or 7. 
This means that we can be smarter about how we iterate up: 11 -> 13 -> 17 -> 21 -> 23...
We borrow the is_prime helper from p7
"""


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_truncatable_prime_right(n: int) -> bool:
    str_n = str(n)
    while len(str_n) >= 1:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[:-1]
    return True


def is_truncatable_prime_left(n: int) -> bool:
    str_n = str(n)

    while len(str_n) >= 1:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    return True


def main() -> int:
    sum = 0
    count = 0

    n = 11
    while count < 11:
        if is_truncatable_prime_left(n) and is_truncatable_prime_right(n):
            count += 1
            sum += n
            print(n)
        if str(n)[-1] == "1":
            n += 2
        else:
            n += 4

    return sum


if __name__ == "__main__":
    print(main())
