"""
Problem Statement:
Take the number 192 and multiply it by each of 1, 2, and 3:
192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 
192384576 the concatenated product of 192 and (1,2,3).
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving 
the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ..., n) where n > 1?


Computational Analysis: We iterate across all integers up to N, where N represents the max integer
that could possibly produce a viable product set that results in a 9-digit solutions. In our case,
N is 9999. Across each iteration, we perform constant work to test the integer for a viable
pandigital. As such, runtime complexity is O(N). Space complexity is also O(N) technically due to the
list of candidates, but in reality it should be much much smaller than N. 

DSA: We employ a brute-force check across all integers in the state space, testing for viability on each.
In each check, we employ some simple int/string manipulation and set membership.

Math: The solution leverages properties of multiplication and digit length to ensure each concatenated 
product is exactly nine digits, helping to curb the size of N. 

"""

"""
Program Attempt 1:
I first think of a brute-force method for this. We could go either forward or backwards. Going forward
would be testing integers with product sets and seeing if they land on a pandigital. Record the
largest pandigital we find across our iteration. Going backwards would be iterating over the space of 
9-digit pandigitals: we start with the largest one, 987654321, check if it matches the criteria, and 
if not, move on. The problem is that the conditional check here is non-trivial, we'd basically be 
doing brute-force going forward anyways.
So, let's do the going-forward method: Iterate from 1 to N, where N+1 is the first integer
where a (1, 2) product set results in a 10-digit solution. N happens to be 9999. For each integer n, 
find the product set, if it exists, that is 9 digits. 
"""


def is_pandigital(num_str: str) -> bool:
    return len(num_str) == 9 and set(num_str) == set("123456789")


def test_int(n: int) -> int:
    concat_product = ""

    mult = 1
    while len(concat_product) < 9:
        concat_product += str(n * mult)
        mult += 1

    return int(concat_product) if is_pandigital(concat_product) else 0


def get_largest_pandigital_multiple(max_range: int) -> int:

    candidates = [test_int(n) for n in range(1, max_range) if test_int(n)]
    return max(candidates)


if __name__ == "__main__":
    ans = get_largest_pandigital_multiple(9999)
    print(ans)
