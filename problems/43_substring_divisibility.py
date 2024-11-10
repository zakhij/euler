"""
Problem Statement:
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 
in some order, but it also has a rather interesting sub-string divisibility property.
Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:
* d_2d_3d_4=406 is divisible by 2
* d_3d_4d_5=063 is divisible by 3
* d_4d_5d_6=635 is divisible by 5
* d_5d_6d_7=357 is divisible by 7
* d_6d_7d_8=572 is divisible by 11
* d_7d_8d_9=728 is divisible by 13
* d_8d_9d_10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

Computational Analysis: The time and space complexity of this problem are directly tied to the permutations 
function. Computing permutations of an n-length string is n!, so we can say that the time and space complexity
of these problems are O(n!), where n is the number of digits (in our case, 10). We perform constant time work
on the substring property check, so that doesn't add anything.

DSA: We first generate the entire possible state space via permutation, then brute force check that state space.

Math: We leverage the relationship between pandigitals and permutations to unlock this problem. 

"""

"""
Program Attempt 1:
The solution will ultimately be a brute force check on all 0-9 pandigitals. We can simply
get all the permutations of 0-9 (using built in package), then run a check on each.
"""


def has_substring_property(s: str) -> bool:

    return (
        int(s[1:4]) % 2 == 0
        and int(s[2:5]) % 3 == 0
        and int(s[3:6]) % 5 == 0
        and int(s[4:7]) % 7 == 0
        and int(s[5:8]) % 11 == 0
        and int(s[6:9]) % 13 == 0
        and int(s[7:10]) % 17 == 0
    )


def main() -> int:
    from itertools import permutations

    total = 0

    for perm in permutations("0123456789"):
        pandigital = "".join(perm)
        if has_substring_property(pandigital):
            total += int(pandigital)

    return total


if __name__ == "__main__":
    import time

    start = time.time()
    ans = main()
    print(ans)
    end = time.time()
    print(end - start)
