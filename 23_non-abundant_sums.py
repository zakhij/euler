
'''
Problem Statement:
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
that 28 is a perfect number. A number n is called deficient if the sum of its proper divisors is less 
than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written 
as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers 
greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot 
be reduced any further by analysis even though it is known that the greatest number that cannot be expressed 
as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


Computational Analysis:

DSA:

Math:

'''

'''
Program Attempt 1:
For sure, we'll need a data structure list to store all abundant numbers from 1 to 28123. The real dilemma is,
what do we do with this list? As a brute force strategy, we could iterate from 1 to 28123 and, for each number,
individually check if it's a sum of two abundant numbers. But that check would be a lot of work, needing to test
every possible summation combination of the abundant numbers list. Instead, we could use the list of abundant numbers
and pro-actively create a subsequent set from that, the set of abundant sums less than 28123. The creation of this
set would be O(m^2) where m is the number of abundant numbers, so much less than all ints in the range. Then, we can
simply add up all positive ints not found in this set. 

'''

def is_abundant_num(n: int) -> bool:
    import math
    sum = 1
    for i in range(2, int(math.sqrt(n))+ 1):
        num = n / i 
        if num.is_integer():
            sum += num
            if num != i:
                sum += i 
    return True if sum > n else False
    
def get_list_of_abundant_nums_under_n(n: int) -> list[int]:
    abundant_num_list = []
    for i in range(1, n):
        if is_abundant_num(i):
            abundant_num_list.append(i)

    return abundant_num_list

def get_set_of_abundant_sums(abundant_list: list[int], limit: int) -> set:
    abundant_sum_set = set()

    for a in range(len(abundant_list)):
        for b in range(len(abundant_list[a:])):
            two_sum = abundant_list[a] + abundant_list[b]
            if two_sum < limit:
                abundant_sum_set.add(two_sum)
    
    return abundant_sum_set



def non_abundant_sums(n: int) -> int:
    abundant_list = get_list_of_abundant_nums_under_n(n)

    set_of_abundant_sums = get_set_of_abundant_sums(abundant_list, n)

    sum = 0
    for i in range(1,n):
        if i not in set_of_abundant_sums:
            sum += i
    
    return sum




if __name__ == '__main__':
    ans = non_abundant_sums(28123)
    print(ans)