"""
Problem Statement:
We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once; for example, the 5-digit number, 15324, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 times 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be 
written as a 1 through 9 pandigital. HINT: Some products can be obtained in more 
than one way so be sure to only include it once in your sum.


Computational Analysis: The runtime complexity scales with the number of multicand,
multiplier pairs we iterate over: we perform constant time operations in each 
iteration. The space complexity scales with the number of pandigital products, due
to the set.

DSA: We effectively perform brute-force search, with some optimizations to reduce
the search space. We employ a set to effectively handle duplicate products.  

Math: The main math property leveraged in our solution is regarding anticipating
the number of digits possible in the multicand and multiplier. 

"""

"""
Program Attempt 1:
Interesting. My first thought goes towards a brute force implementation, trying
every combination in the given space. However, we can be smart in choosing our
space to iterate over. I'm looking at the number of digits, specifically, since
we know for sure that the multicand/multiplier/product must be 9 digits total.
So that limits us to 1 x 4 = 4 and 2 x 3 = 5, I believe. 
It's also critical to have a helper function that validates whether a given
multiplier, multicand pair gives a product that satisfies our definition.
"""


def is_pandigital_product(multicand: int, multiplier: int) -> bool:
    digit_set = set()
    for digit in str(multicand):
        if digit == "0":
            return False
        elif digit in digit_set:
            return False
        digit_set.add(digit)

    for digit in str(multiplier):
        if digit == "0":
            return False
        elif digit in digit_set:
            return False
        digit_set.add(digit)

    for digit in str(multiplier * multicand):
        if digit == "0":
            return False
        elif digit in digit_set:
            return False
        digit_set.add(digit)

    return True


def get_pandigital_products() -> int:
    prod_set = set()

    for multicand in range(1, 10):
        for multiplier in range(1000, 9999):
            if is_pandigital_product(multicand, multiplier):
                prod_set.add(multicand * multiplier)

    for multicand in range(11, 100):
        for multiplier in range(100, 999):
            if is_pandigital_product(multicand, multiplier):
                prod_set.add(multicand * multiplier)

    return sum(prod_set)


if __name__ == "__main__":
    ans = get_pandigital_products()
    print(ans)
