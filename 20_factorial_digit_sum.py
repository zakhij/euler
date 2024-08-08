
'''
Problem Statement:
n! means n x (n-1) x ... 3 x 2 x 1. For example, 10! = 10 x 9 x ... 3 x 2 x 1 = 3268800,
and the sum of the digits in the number 10! is 3+2+6+8+8+0+0=27.
Find the sum of the digits in the number 100!.

Computational Analysis:

DSA:

Math:

'''

'''
Program Attempt 1
In Python, I COULD just do this brute-force thanks to arbitrary precision arithmetic,
but I think that goes against the spirit of this problem. But then... I'm not sure
how to solve it. It's not like I could build up to the solution using previous factorial
values, so I'm not sure how to get the solution without necessarily calculating the
number of 100!. (The answer is I couldn't, but I'd instead need to use lists/strings to
perform manual multiplication of large numbers).
'''
import math

def get_sum_of_digits_factorial(n: int) -> int:
    fact = math.factorial(n)
    return sum([int(i) for i in str(fact)])



if __name__ == '__main__':
    l = math.factorial(100)
    print(str(l))
    ans = get_sum_of_digits_factorial(100)
    print(ans)