
'''
Problem Statement:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

Computational Analysis: Runtime complexity is O(n * sqrt(n)) where n is the upper limit of the range
of iteration. We iterate through n numbers, performing the helper function for each n. The helper
function scales as O(sqrt(n)), giving us the final total runtime complexity. Space complexity is constant,
we rely only on pointers and counters. 

DSA:

Math: 

'''

'''
Program Attempt 1:
The first implementation that comes to mind is performing a kind of brute force: Go from 
1 to 10k and, at each number, get the sum of divisors and store it. Then at the end of the
loop, analyze the sum of divisors storage and check for amicable numbers. Let's focus on this 
first before thinking of how to make it more efficient. I'd need a helper function that gives the
sum of divisors for a given n. And then a helper function that takes in a list of sum-of-divisors
and outputs the sum of amicable numbers. ACTUALLY, I don't think I need to use a data structure for 
holding sum-of-divisors. I can on-the-spot, within the loop, test if it's an amicable pair and add 
it to a running sum if so. 
'''

def get_sum_of_divisors(n: int) -> int: 
    import math
    sum = 1
    for i in range(2, int(math.sqrt(n))+ 1):
        num = n / i 
        if num.is_integer():
            sum += num
            if num != i:
                sum += i
    
    return int(sum)


def amicable_numbers(n: int) -> int:
    already_checked_numbers = set()

    amicable_sum = 0

    for i in range(2, n):
        if i in already_checked_numbers:
            continue
        already_checked_numbers.add(i)
        divisors_sum = get_sum_of_divisors(i)
        
        if i != divisors_sum and divisors_sum < n and get_sum_of_divisors(divisors_sum) == i:
            already_checked_numbers.add(divisors_sum)
            amicable_sum += i + divisors_sum
    
    return amicable_sum
        


if __name__ == '__main__':
    ans = amicable_numbers(10000)
    print(ans)
