"""
Problem Statement:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?

Computational Analysis: The runtime complexity is O(nloglognlogn), where n is the upper bound of
our space of potential candidates. Constructing the Sieve of Eratosthenes is O(nloglogn) and 
checking for pandigital-ness on each prime is O(logn). Space complexity is O(n), as we store
the list of primes. 

DSA: Ultimately, this is an iterative check. We use the sieve of eratosthenes to get all primes under N, 
then perform a systematic check on each prime to verify if they're also pandigital.

Math: We do use primes, but we don't leverage any special properties of primes here. There
is no relation or pattern between prime numbers and pandigital numbers to leverage finding
the answer. However, we do use the fact that all 9-digit and 8-digit pandigitals cannot 
be prime to significantly reduce the search space. 

"""

"""
Program Attempt 1:
I think in the big picture, we must rely on some sort of brute force checking algorithm: I don't see any
pattern or relation between prime numbers and pandigital numbers that we could leverage here.
The first approach that comes to mind is brute forcing the pandigital-ness of all primes up to X, where
X is the upper boundary of an n-digit pandigital (in our case, it's 987,654,321). We know that we can
efficiently curate a list of such primes using the Sieve of Eratosthenes. Then, we iterate through
the list of primes checking for pandigital-ness. The alternative would be to do the inverse: curate a 
list of valid pandigitals, then iterate through and checking for primality. Which is better?
The former. The list curation using the Sieve is O(nloglogn), and checking for pandigital-ness is 
roughly O(logn), as it depends on the count of digits. Meanwhile, curating the pandigital list is
O(n) and checking for primality is O(sqrt(n)). 
EDIT: Funny note: originally, I set the upper bound at 987654321, but it's actually 7654321. We 
know for a fact that 9-digit and 8-digit pandigitals cannot be prime, because the sums of their
digits are divisible by 3 (45 and 36 respectively). This one small insight is INCREDIBLY important,
as the space of n shrinks by a factor of 100. The program goes from taking 100 seconds to 0.5 sec.

"""


def sieve_of_eratosthenes(X: int) -> list[int]:
    sieve = [True] * (X + 1)
    for x in range(2, int(X**0.5) + 1):
        if sieve[x]:
            for i in range(x * x, X + 1, x):
                sieve[i] = False
    return [x for x in range(2, X + 1) if sieve[x]]


def is_pandigital(num_str: str) -> bool:
    return set(num_str) == set("123456789"[: len(num_str)])


def main(n: int) -> int:
    import time

    s1 = time.time()
    reversed_primes = sieve_of_eratosthenes(n)[::-1]
    s2 = time.time()
    print(s2 - s1)

    for prime in reversed_primes:
        prime_str = str(prime)
        if is_pandigital(prime_str):
            s3 = time.time()
            print(s3 - s2)
            return prime
    return 0


if __name__ == "__main__":
    ans = main(7654321)
    print(ans)
