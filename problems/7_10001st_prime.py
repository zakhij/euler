
'''
Problem Statement
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?

Computational Analysis
The runtime complexity is O(sqrt(n*logn)), as the primality check is O(sqrt(n)) and we do this for
n*logn numbers. This simplifies to just O(sqrt(n)). Because we rely on counters, constant space is used. 

Math: The main math principles used here are found in checking primality. We employ a form of trial
division in the loop. Traditional trial division makes use of the fact that n can be divided by every 
number less than sqrt(n) to check for primality. We take this one step further using the mathematical
fact that primes greater than 3 can be written in the form 6k+/-1 (and thus, numbers that don't fit 
this mold can be ruled out).

'''

#Program Attempt 1
#Okay, the complexity of this problem depends on the patterns of sequential primes. I don't think we can
#directly access the 10,001st prime number. And I don't think that knowing the value of ith prime number
#gives us any lead as to the value of the i+1th prime number. So instead, my strategy is going be simple:
#iterate through all integers, check for primality, and keep a counter for primes encountered. Then, once
#that counter hits 10001, we're done. Since the number of primes up to N is π(N) ≈ N/log(N), then the 
#number of iterations to get the nth prime is nlog(n). Then, the primality test... not sure. I consulted
#ChatGPT to build the is_prime function for me. The complexity of the loop is O(sqrt(n)). 
#Result: It worked! The only slight optimization would be iterating current at 1 and then doing current +=2,
#because there's no reason to check for even numbers. That would cut our search space in half. 

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
    


def get_nth_prime(n: int):
    prime_count = 0
    current = 0
    while prime_count < n:
        if is_prime(current):
            prime_count += 1
        
        current += 1
    
    return current - 1

    
if __name__ == '__main__':
    answer = get_nth_prime(10001)
    print(answer)