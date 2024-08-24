"""
Problem Statement:
Euler discovered the remarkable quadratic formula: n^2 + n + 41.
It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when 
n = 41, 41^2 + 41 + 41 is clearly divisible by 41
The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive 
values 0 <= n <= 79. The product of the coefficients, -79 and 1601, is -126479
Considering quadratics of the form:
n^2 + an + b, where |a|<1000$ and |b|<=1000, 
where |n| is the modulus/absolute value of n, e.g |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces 
the maximum number of primes for consecutive values of n, starting with n = 0.

Computational Analysis: Our runtime complexity, in total, is O(n^3 * sqrt(n)/log(n)). This 
is because all pairs in the [a,b] space constitute n*n/log(n) (a being n, b being n/log(n)
reflecting the number of primes under n). And for each pair, we perform O(nsqrt(n)) computation
in checking for the prime numbers. However, this is an overestimation - in practice, we
certainly aren't going to need to check n quadratic values per pair. The Sieve of Eratosthenes 
is O(loglogn) but is a separate step and dominated by the rest of the function. 
But, it's responsible for the space complexity O(n/log(n)).

DSA: We leverage a brute-force method that traverses the entire state space, all [a,b] pairs that fit
the parameters.  

Math: This problem leverages heavy knowledge of primes, specifically how to efficiently calculate prime
numbers under a given value (sieve) and check for primality. 

"""

"""
Program Attempt 1:
Okay, my intuition is to brute force this by trying every combination of a and b, but
limited to the search space given (in our case, <1000). We can limit the search space
further with the knowledge that |b| must be prime. Does that also hold for a? Hmmm, even
if it does, I think the issue in the problem will be the computational complexity of 
testing a given [a, b] set of values: we'd need to plug in every value from 0 to a. 
Perhaps this is fine though, outside of a grander strategy to build the solution from
the ground up. So we'll need a function that calculates all primes up to 1000. A
function that assigns the [a,b] values to test for. And a function that tests a
given [a,b] set. Following this strategy, we can use sieve of eratosthenes to get
the list of possible b values. Then, we test for all possible values of a between
-n and n. For the space of possible [a,b] is n * (n/log(n)), where the latter represents
the number of primes expected under n. But we're not done: what computation do we need
to do per [a,b] pair? Well, iterate up from 1 to n, at each number, checking for primarily
of the quadratic function. This is O(n*sqrt(n)). So in total, n * (n/log(n)) * nsqrt(n). 
"""
import time


def sieve_of_eratosthenes(X: int) -> list[int]:
    """Helper to get prime #'s up to X (b values)"""
    sieve = [True] * (X + 1)
    for x in range(2, int(X**0.5) + 1):
        if sieve[x]:
            for i in range(x * x, X + 1, x):
                sieve[i] = False
    return [x for x in range(2, X + 1) if sieve[x]]


def evaluate_ab_quadratic(a: int, b: int) -> int:
    number_of_primes = 0
    for i in range(abs(a * b)):
        quadratic = i**2 + (a * i) + b
        if is_prime(quadratic):
            number_of_primes += 1
        else:
            break

    return number_of_primes


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


def get_quadratic_prime_coefficient(n: int) -> tuple:
    list_of_primes = sieve_of_eratosthenes(n)
    b_values = list_of_primes + [-x for x in list_of_primes]
    max = 0
    coeff = 0
    for b in b_values:
        for a in range(-n, n):
            quad = evaluate_ab_quadratic(a, b)
            if quad > max:
                max = quad
                coeff = a * b
    return (max, coeff)


if __name__ == "__main__":
    ans = get_quadratic_prime_coefficient(10000)
    print(ans)
