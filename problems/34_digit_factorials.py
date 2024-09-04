"""
Problem Statement:
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.

Computational Analysis: Similar to p30, it's hard to describe the computational complexity
as a function of a simply understood input. The work done per number is dependent on its digit 
count and the inner workings of the factorial function provided by the math library. The
space complexity is purely dependent on the digit count.

DSA: This is yet another iterate-through-solution-space type of problem, where we validated
each possible solution using a custom-defined checking function.

Math: The main mathematical principle leveraged is simply the understanding of the upper limit
based on the growth of the possible digit factorial sum (each additional digit can augment the
sum by at most 9!, so at 7 digits, the sum is simply outpaced)

"""

"""
Program Attempt 1:
I think I can just iterate from 10 to 999999, and for each number, calculate the sum of its digits' factorials.
I don't think I can solve this bottom-up (i.e., know directly which numbers will meet this condition), I just have to
test over the space of potential candidates. The question is, what range? Should I stop at 999? 9999? 99999999? Infinity?
Well, we know that 9! (362,880) is the biggest number that any 1 digit can contribute. So let's stop at 7 digits. After all,
the product of 8 * 9! still has 7 digits. 
This reminds me of a similar upper threshold issue I encountered with problem 30.

"""
from math import factorial


def is_digit_factorial(n: int) -> bool:
    return n == sum([factorial(int(d)) for d in str(n)])


def main() -> None:
    sum = 0
    for n in range(10, 7 * factorial(9) + 1):
        if is_digit_factorial(n):
            sum += n

    print(sum)


if __name__ == "__main__":
    main()
