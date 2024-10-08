"""
Problem Statement:
Consider all integer combinations of a^b for 2<= a5 and 2<=b<=5:
2^2=4, 2^3=8, 2^4=16, 2^5=32
3^2=9, 3^3=27, 3^4=81, 3^5=243
4^2=16, 4^3=64, 4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125
If they are then placed in numerical order, with any repeats removed, we 
get the following sequence of 15 distinct terms:
4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125.
How many distinct terms are in the sequence generated by a^b for 2<=a<=100 and 2<=b<=100?

Computational Analysis: Runtime complexity is easily deduced as O(n^2): we create a nested
loop to explore all possible [a,b] pairs, where a and b share range of n. Thankfully, using
a set means that we can iterate through a given pair in constant time. Space complexity is 
O(n^2) as well though, because of this set holding all unique [a,b] pair values.

DSA: We utilize a set as our data structure of choice thanks to its quick addition and ability
to only store unique items, which aligns perfectly with the problem requirements.

Math: No complex math, although I tried leveraging prime factorization here (and in theory,
I believe there could be a way to intelligently leverage it to design a faster, bottom-up
solution). 

"""

"""
Program Attempt 1:
I think we can tackle this from the bottom up, leveraging prime factorization. For 
instance, we know that 9^3 can be rewritten as (3^2)^3, or 3^6. So in theory, we
can pro-actively seek out all of 3's "older siblings" under the threshold, 100,
and see how many can get crossed off. Continuing with this example, we'd look at 
81 (3^4), and we can say that there are duplicates all the way up to 81^25 (which is
3^100). So basically, look at each prime number under 100 and check its older siblings
using this technique. Then, we can just subtract all of these from the total
"""


def sieve_of_eratosthenes(X: int) -> list[int]:
    """Helper to get prime #'s up to X"""
    sieve = [True] * (X + 1)
    for x in range(2, int(X**0.5) + 1):
        if sieve[x]:
            for i in range(x * x, X + 1, x):
                sieve[i] = False
    return [x for x in range(2, X + 1) if sieve[x]]


def get_duplicates_on_prime(prime: int, max: int) -> int:
    sum = 0
    for i in range(2, max):
        if prime**i < max:
            max_duplicate_power = max // i
            sum += max_duplicate_power
            print(f"max power {max_duplicate_power} for prime, i {prime}, {i}")
        else:
            break

    return sum


def get_distinct_powers_2_to_n(n: int) -> int:
    primes = sieve_of_eratosthenes(n)[1::]
    print(primes)
    duplicates_sum = 0
    for prime in primes:
        duplicates_sum += get_duplicates_on_prime(prime, n)

    return (n - 1) ** 2 - duplicates_sum


"""
Program Attempt 2:
Man, I'm bummed that my first program didn't work. But, I guess that there are other
duplicates besides just derivations of the same prime factor. We'll have to go with ye
old brute-force method of checking every [a,b] exponent pair and keeping a set
for fast membership checks.
"""


def get_distinct_powers_2_to_n2(n: int) -> int:
    distinct_set = set()
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            power = a**b
            distinct_set.add(power)

    return len(distinct_set)


"""
Program Attempt 3:
Just for fun, I try to implement a more generalized version of attempt 1
to see if I can get the answer using that methodology. My attempt still
failed, unfortunately. 
"""


def get_duplicates_on_base(base: int, max: int) -> int:
    sum = 0
    for i in range(2, max):
        if base**i < max:
            isDerived.append(base**i)
            max_duplicate_power = max // i
            sum += max_duplicate_power
        else:
            break

    return sum


def get_distinct_powers_2_to_n3(n: int) -> int:
    global isDerived
    isDerived = []
    duplicates_sum = 0
    for i in range(2, n):
        if i not in isDerived:
            duplicates_sum += get_duplicates_on_base(i, n)

    return (n - 1) ** 2 - duplicates_sum


if __name__ == "__main__":
    ans = get_distinct_powers_2_to_n2(100)
    print(ans)
