

'''
Problem Statement: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Computational Analysis: The program is divided into two separate parts. The first part is constructing the list of primes
under N (in our case, 20). This is O(NloglogN).The second part, iterating through each prime, is about O(N): the number of primes 
up to N is π(N), where π(N) is roughly N/log(N), and the operations/prime is O(logN). So, the program is dominated by the first 
part, and our time complexity is ultimately O(NloglogN). As for space: We keep a list of the primes, which again, is O(π(N)) long.

Math: Ultimately, this problem is finding the Least Common Denominator (LCM). We most greatly exploit prime factorization here,
making use of the fact that the LCM must contain each prime factor to the highest power that appears in the factorizations of 
the numbers in the range from 1-N (e.g., if 16 has 2^4 in its factorization, the LCM must have at least 2^4 as well).

'''

#Program Attempt 1
#This feels a bit like dynamic programming, in the sense that we can recursively tell if a number is divisible by, say,
#20, by understanding that it's divisible by both 4 and 5. (And we know that a number is divisible by 4 because it's 
#divisible by 2). So some prime factorization is at play here to reduce the work. As in, we can initially break down
#1 thru 20 into a smaller set of numbers to check divisibility based on their prime factors. I think that should look like
# [2, 3, 5, 7, 11, 13, 17, 19]. That's the real question: What's the smallest integer that holds this prime factorization?
# And well, the answer is just to multiply all of them together haha. So 2 x 3 x 5 x 7 x 11 x 13 x 17 x 19. Let's see
#if that works. 
#And the result is in... it does NOT work that way!

def calc_product_of_primes_less_than_20():
    return 2*3*5*7*11*13*17*19


#Program Attempt 2
#Ok silly me. The problem is my missing the fact that just bc 3 is a prime factor doesn't mean it's divisible by 9: it needs
#to have 3 * 3 as a prime factor to be divisible! So this means we need to take into account HOW MANY prime factors we need.
#But tbh, this seems pretty simple, and I also want to generalize this. So, I'm thinking we create a loop from 1 to N. 
#For each number n in the loop, break down its prime factorization. Hmm, actually, I'm not thinking of a couple different ways.
#Why not start from the ground up? Like, start at 2, the first prime number. Then, check if 2^2 is < N. If so, add another 2 to
#our data structure. Repeat 2^x until 2^x+1 > N, at which point, the prime 2 should be in our data structure x number of times.
#Then, repeat this for 3, then for 5, until the biggest prime still smaller than N. The other option is the 1-to-N loop, where
#I go through each number n, break down its prime factorization, see if its covered by our current working set of primes (duplicates
#included), and if not, add the necessary addition to the working set of primes. But this seems very inefficient. And if I wanted to
#make use of the fact that, for instance, 8 is just 4 (which we already visited) x 2, that's converging on the first approach detailed.
#So, let's do the first approach, working up. 
#RESULT: It works! I did hardcode the list of primes, but I'd otherwise use the Sieve method to get it for any arbitrary N. 

def calc_product_of_primes_less_than(N):
    from collections import Counter
    import math
    primes_list = [2,3,5,7,11,13,17,19] #hardcoded for N = 20

    final_product = 1
    for prime in primes_list:
        number_of_duplicate_primes = int(math.log(20,prime))
        final_product *= (prime** number_of_duplicate_primes)
        print(f"{number_of_duplicate_primes} of {prime} now gives us {final_product}")
    
    return final_product



if __name__ == '__main__':
    #answer = calc_product_of_primes_less_than_20()
    #print(answer)

    answer = calc_product_of_primes_less_than(20)
    print(answer)