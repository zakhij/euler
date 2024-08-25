"""
Problem Statement:
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Computational Analysis: It's a bit difficult to describe the runtime complexity. The work done
per number is dependent on its digit count (d) and the number of numbers checked (n), O(n*d).
We can relate these to the input power, p: d scales linearly with p, n scales exponentially.
So in total, O(p*9^p). Space complexity is O(n) due to creating the list of digits per number.

DSA: No special data structures or algo's used for this problem. 

Math: No special math properties used for this problem. 

"""

"""
Program Attempt 1:
Jeez, this problem seems like a doozy in the get-go because of the limitless range. ALL NUMBERS?
Now, I do notice in the example that, curiously, the 4th-power numbers all have exactly 4 digits.
Is this a coincidence, or could I make the assumption that all sum-of-5th-power numbers will have
exactly 5 digits, so I only need to check the space between 10,000 and 99,999? I really want to 
make this assumption, because I'm not sure how we can intelligently derive these numbers; I can't
see an underlying pattern, and my intuition is that we'd need to brute force check the numbers. 
"""


def is_digit_sum_power(n: int, power: int) -> bool:
    sum = 0
    digit_list = [int(x) for x in str(n)]

    for digit in digit_list:
        sum += digit**power

    if sum == n:
        print(n)
    return sum == n


def get_sum_of_digit_n_power(power: int) -> int:
    sum = 0
    start = int("1" + "0" * (power - 1))
    end = int("9" * power)
    for i in range(2, end):
        sum += i if is_digit_sum_power(i, power) else 0
    return sum


"""
Program Attempt 2:
Alright, so based on some basic experimentation, I know that attempt 1 fails ONLY BECAUSE
our upper limit is too small. However, if I were to add an extra digit to the upper limit
(i.e., 99999 -> 999999) in our search, we get the right answer. The question is then: how
do we actually determine the upper limit, without this guesswork? Well, we can use the
maximum value of a single digit, 9^5 = 59049. We multiply this by 5 to get 59049 * 5 = 295245,
so we can set the upper limit to 295245.
"""


def get_sum_of_digit_n_power2(power: int) -> int:
    sum = 0
    limit = limit = power * 9**power
    for i in range(2, limit):
        if is_digit_sum_power(i, power):
            sum += i
    return sum


if __name__ == "__main__":
    ans = get_sum_of_digit_n_power2(5)
    print(ans)
