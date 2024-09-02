
'''
Problem Statement: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Computational Analysis: The Sieve of Eratosthenes operates with a runtime complexity of 
O(nloglogn). Although the outer loop only extends up to sqrt(n), the workload of the inner 
loop (marking non-primes) decreases significantly as the algorithm progresses, a direct 
consequence of the diminishing frequency of multiples for larger prime numbers.

DSA: No special data structures are employed, just lists and loop and conditionals.

Math: We are dealing with prime numbers, and we specifically use the Sieve of Eratosthenes, an ancient algorithm
for finding primes under a given number N that exploits prime factorization to pre-emptively eliminate prime number
candidates and unveils the distribution of primes.

'''

#Program Attempt 1
#There are two ways to approach this, I'm thinking. The first way is to initialize a sum and a counter,
#iterate the counter starting from 1 to 2 million, and at each number, check if it's prime: if so, we
#add it to the sum. We'd just need a prime checker and execute it at every number (trial division?).
# The second way is using a specific math formula/algo to get a list of primes less than X. Then, 
#iterate through the list to get the sum. The second way I THINK is faster, and I think it's Rho's
#Algorithm? Lemme look it up... nope it's Sieve of Eratosthenes. Well, let's do it.


def sieve(N: int) -> int:
    import math
    l = [True for i in range(N)]
    l[0] = l[1] = False
    limit = int(math.sqrt(N)) + 1
    for i in range(2,limit):
        if l[i]:
            j = i**2
            while j < N:
                l[j] = False
                j += i        
    prime_sum = sum([i for i, is_prime in enumerate(l) if is_prime])
    return prime_sum









if __name__ == '__main__':
    num = 2000000
    ans = sieve(num)
    print(ans)
