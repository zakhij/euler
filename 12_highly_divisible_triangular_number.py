
'''
Problem Statement: The sequence of triangle numbers is generated by adding the natural numbers. So the 7th 
triangle number would be 1+2+3+4+5+6+7 = 28. Let's list the factors of the first 7 triangular numbers:
1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
We can see that 28 is the first triangular number to have over 5 divisors. 
What is the value of the first triangle number to have over five hundred divisors?

Computational Analysis: Determining the exact runtime complexity of this algorithm is challenging 
due to the intricacies of divisor distribution among natural numbers. Each call to our 
divisor-counting function, which operates at O(sqrt(n)), is applied potentially up to n times, where 
n reflects the sequence of triangular numbers. However, in practice, the number of iterations 
needed to find a triangular number with N divisors does not strictly follow n, and tends to be less due 
to increasing divisor density in larger numbers. Thus, in practice, we should outperform O(n*sqrt(n)).
Space complexity is O(1).

DSA: No data structures or special algorithms are used, really. Just pointers, loops, and basic arithmetic. 

Math: Our final attempt leverages 2 key math principles: the triangular number formula of T(n) = n*(n+1)/2
that generates triangular numbers in sequence, and the relationship in number of divisors for the product of 
n and n+1 (the # of divisors of the product of two coprime numbers is the product of their individual # of divisors)

'''

#Program Attempt 1
#Okay, so brute force would obviously be to count up the triangular numbers, then at each term, check its 
#divisors and see if the count exceeds 500. But, this is assuming that the list of divisors between triangular
#numbers is independent between one another. Ideally there exists a pattern such that we can pre-compute and store
#the divisors for a given term. Let's focus on the brute force case first though. So, we need: a way to increment
#triangular terms and a way to efficiently get a list of divisors for a given number. The first part is simple: keep
#a counter going that increments by 1 and a triangular term variable. Increment the first counter, then increment the term
#by the counter value to get the next term. The second part... might be more complex. We can brute force it, using a 
#nested loop going from 1 to the n/2 and do a modulus operation. 

def get_divisor_count(num: int) -> int:
    
    divisor_count = 0
    for i in range(1,num/2+1):
        if num % i == 0:
            divisor_count += 1
        
    return divisor_count

def triangular_divisor_finder(threshold: int) -> int:
    triangle_incrementer = 1
    triangle_number = 1

    while True:
        number_of_divisors = get_divisor_count(triangle_number)
        if number_of_divisors > threshold:
            return triangle_number
        else:
            triangle_incrementer += 1
            triangle_number += triangle_incrementer


#Program Attempt 2
#Okay program attempt 1 takes too long. It took over a minute. So I'm definitely missing a shortcut, because my brute
#force just ain't cutting it. I was thinking of a bottom-up approach, as in, look at the divisors and try to multiply them
#up to a triangular number. But the problem is, I'm not sure there's a pattern there. It's not like I can just multiply 1-500
#and then find the next triangular number. What if the answer has divisors like 1, 2, 3, 4, 5, 6, 8, 9... 501? I could
#try reducing the search space; for instance, only looking at evens? Actually, scratch that. The key to an efficient 
#algorithm, I think, is eliminating redundant computation by storing the # of divisors. For instance, take 28. It suffises
#to derive its number of factors as (# of factors of 28/2) + 1, right? So we can use a recursive approach to more
#efficiently calculate the number of divisors for any given number N. For any given number N, look at its smallest
#non-1 divisor.... JK it's not true!! Look at 28 again. 4 is a divisor of 28, but not 14. Dang it. Okay so instead,
#let's focus on more marginal gains. Okay yes, I can improve get_divisor_count by only iterating its loop up to 
#the sqrt(N) rather than up to N itself. This seems to do the trick, it took ~5 sec to process this now.


def get_divisor_count2(num: int) -> int:
    import math
    divisor_count = 0
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            divisor_count += 1
            if i != num // i:
                divisor_count += 1
        
    return divisor_count
            
    

def triangular_divisor_finder2(threshold: int) -> int:
    triangle_incrementer = 1
    triangle_number = 1

    while True:
        number_of_divisors = get_divisor_count2(triangle_number)
        if number_of_divisors > threshold:
            return triangle_number
        else:
            triangle_incrementer += 1
            triangle_number += triangle_incrementer

#Program Attempt 3
#Hold the phone!!! Upon consulting ChatGPT, there is another more efficient strategy we can devise, and it relies
#on 2 mathematical principles. First, any triangular number can be represented as T(n) = n*(n+1)/2. Second, the
#number of divisors for the product of 2 coprime numbers is simply the product of the number of divisors of those
#two numbers. n and n+1 are inherently coprime. Thus, we can efficiently derive the # of divisors of T(n) by looking
#at the number of divisors on n and n+1. So at a high level, we are changing how we iterate across triangular numbers
#and we are reducing the size of the number that we need to put through our helper function, which stays the same.

def count_divisors(n):
    import math
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def find_triangular_divisor_limit(limit:int) -> int:

    n = 1

    while True:

        if n % 2 == 0:
            divisors_n = count_divisors(n//2)
            divisors_n1 = count_divisors(n+1)

        else:
            divisors_n = count_divisors(n)
            divisors_n1 = count_divisors((n+1)//2)


        if divisors_n*divisors_n1 > limit:
            return int(n * (n+1) / 2)
        
        n += 1


if __name__ == '__main__':
    ans = find_triangular_divisor_limit(500)
    print(ans)
    pass