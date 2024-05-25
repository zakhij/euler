import math

"""
Computational Analysis: O(sqrt(N)). Worst case scenario, we check every number up to sqrt(N).
Math: The main math component involves prime numbers and understanding prime factorization. The 
solution relies on the fundamental theorem of arithmetic, which states that every integer greater 
than 1 can be uniquely factorized into a product of prime numbers (except for the order of the 
factors). This property allows us to iteratively divide the given number by its smallest prime 
factors until we identify the largest prime factor.
"""



#Program Attempt 1
#My brute-force intuition is to go through the list of prime numbers A less than X and return the first one where X % a = 0. This solution
#would require first creating the list of prime numbers less than X, which would mean iterating over every single integer
#less than X, checking if it's prime, and if so, adding it to the list. But then that begs the question, how do we check if an integer
#is prime? We'd need to do a modulus (%) test with that integer for every integer smaller than it. As such, building the list is O(n^2).
#So instead, let's thing of a smarter approach... I think the first part of my strat is fine, since that's O(n) (and, bc it's a separate
#step, has an ADDITIVE relationship to the second part for time complexity calculation). The real problem, and chance for optimization, is 
#in the second part. I just Google'd something called the Sieve of Eratosthenes which can produce my prime number list in O(nloglogn)
#time. Also, I only need to look at prime numbers less than or equal to (X/2), because any number greater than that cannot be a factor 
#of X (i.e.,the best case scenario is for X/2 to be a prime number as well).
def getPrimesLessThan(num: int) -> list[int]:
    isPrime = [True] * (num + 1)
    isPrime[0]=isPrime[1]=False

    x = 2
    while (x * x <= num):
        if isPrime[x]:
            for i in range (x*x,num+1,x):
                isPrime[i] = False
        x += 1
    return [p for p in range(num+1) if isPrime[p]]


#Program Attempt 2
#My first attempt failed due to memory constraints. Switching to segmented sieve, where we process sqrt(X) chunks of sqrt(X) size. 
#Now, i need 3 functions to compute the list of prime numbers less than X. Function A gets the list of chunk ranges.Function B
#takes the lower and upper limit of each chunk range and returns the list of primes within that range. And Function C puts A
#and B together, calling Function B for each chunk in Function A's output. 

def get_list_of_chunks(num: int) -> list[tuple[int]]:
    chunks = []

    chunk_size = int(math.sqrt(num))

    for start in range(2, num+1, chunk_size):
        end = min(start + chunk_size - 1, num)
        chunks.append((start, end))
    
    return chunks

def process_chunk(lower:int, upper: int, primes: list[int]) -> list[int]:

    chunk_primes = [True] * (upper-lower + 1)

    for prime in primes:

        start = max(prime*prime, lower + (prime - lower % prime) % prime)
        for i in range(start, upper+1,prime):
            chunk_primes[i-lower] = False

    return [p for p in range(lower, upper+1) if chunk_primes[p-lower]]


def get_primes_less_than_v2(num: int) -> list[int]:
    final_prime_list = []
    chunk_list = get_list_of_chunks(num)
    
    # Process initial chunk to get primes up to sqrt(num)
    initial_limit = int(math.sqrt(num)) + 1
    final_prime_list = process_chunk(2, initial_limit, [])

    for chunk in chunk_list:
        chunk_primes = process_chunk(chunk[0], chunk[1], final_prime_list)
        final_prime_list.extend(chunk_primes)

    return final_prime_list


#Program Attempt 3
#Okay, program attempt 2 does work, but it takes waaaaay too long to find a list of primes under X. And there's not
#much room for improving on the algorithmic base of the program. Instead, I need to use a new algorithmic base
#entirely. It was my choice to generate the list of primes less than X, but that's unnecessary for this specific
#problem. Instead, after consulting ChatGPT, we will perform trial division. In fact, this is very simple: we 
#iteratively shave down the beastly number by stripping it of other primes, starting from all of its 2 primes.
#Once all the 2 primes are gone, move to 3. Strip it down, move to 4, and so on, until we've stripped it down
#completely, at which point we know that we hit its largest prime factor (which we record throughout this process).

def largest_prime_factor(n):
    factor = 2
    biggestFactor = 1

    while n > 1:
        if n % factor == 0:
            biggestFactor = factor
            n //= factor
        factor+=1

    return biggestFactor


if __name__ == '__main__':
    import time
    #target = 600,851,475,143
    target = 600851475143
    print(largest_prime_factor(target))
    
    
    """
    target_modified = int(target / 2)
    print("Target:", target_modified)

    start_time = time.time()
    primes = get_primes_less_than_v2(target_modified)
    end_time = time.time()

    print("Number of primes found:", len(primes))
    print("Execution time:", end_time - start_time, "seconds")
    """








