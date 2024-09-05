"""
Problem Statement:
The number 197 is called a circular prime because all rotations of the digits: 197, 971, and 719, 
are themselves prime. There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

Computational Analysis: There are two separate components to think of for runtime complexity:
the sieve of eratosthenes and the primes iteration/validation. Surprisingly, the former
dominates the latter; the sieve is O(nloglogn) whereas the primes iteration is O(n/logn):
we can think to perform constant work per number (technically it depends on the # of digits),
and the number of iterations is dependent on the number of primes below n. Space complexity is
O(n/logn) for both, storing the list of primes.

DSA: We leverage the sieve of eratosthenes to get all primes under N, along with a systematic
check on each prime to verify if they're circular. We utilize a set for quick membership checking.

Math: We do use primes, but we don't leverage any special properties of primes here.

"""

"""
Program Attempt 1:
Yet again, I think a brute force check of all candidates works well here. Grab all primes
under X (1 million) using the classic sieve. Then for each prime in the list, check all
its rotations for primality. And thankfully, the number of rotations scales linearly with the number
of digits (unlike permutations, which would scale factorially!). 

"""


def sieve_of_eratosthenes(X: int) -> list[int]:
    sieve = [True] * (X + 1)
    for x in range(2, int(X**0.5) + 1):
        if sieve[x]:
            for i in range(x * x, X + 1, x):
                sieve[i] = False
    return [x for x in range(2, X + 1) if sieve[x]]


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


def is_circular_prime(prime: int) -> bool:

    prime_str = str(prime)

    for _ in range(1, len(prime_str)):
        prime_str = prime_str[1:] + prime_str[0]
        if not is_prime(int(prime_str)):
            return False

    print(f"{prime} is circ")
    return True


def main(limit: int) -> int:
    circular_primes_count = 0

    primes = sieve_of_eratosthenes(limit)

    for prime in primes:
        circular_primes_count += 1 if is_circular_prime(prime) else 0

    return circular_primes_count


"""
Program Attempt 2:
Silly me! I don't even need an is_prime helper function, we already compute the 
list of primes under X, so we can just do a simple check via set membership. 
Let's adjust our inner loop logic then 

"""


def is_circular_prime2(prime: int, primes_set: set) -> bool:
    prime_str = str(prime)
    for i in range(1, len(prime_str)):
        rotated = int(prime_str[i:] + prime_str[:i])
        if rotated not in primes_set:
            return False
    return True


def main2(limit: int) -> int:

    primes = sieve_of_eratosthenes(limit)

    primes_set = set(primes)
    circular_primes_count = sum(
        1 for prime in primes_set if is_circular_prime2(prime, primes_set)
    )

    return circular_primes_count


if __name__ == "__main__":
    l = main2(1000000)
    print(l)
