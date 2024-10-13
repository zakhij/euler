"""
Problem Statement:
If p is the perimeter of a right angle triangle with integral length sides {a, b, c},
there are exactly three solutions for p = 120: {20,48,52}, {24,45,51}, {30,40,50}.
For which value of p < 1000 is the number of solutions maximized?


Computational Analysis: Using a nested loop to iterate across [a,b] pairs, our runtime complexity is O(n^2), where n is
the max allotted perimeter. Though the loop ranges for both a and b scale linearly as n increases, we leverage mathematical
principles to in practice severely cut down the search space, so it should be much faster in practice. Space complexity
is O(n), given our dictionary of perimeters. 

DSA: We use loops to to algorithmically iterate over the space of possible [a,b] pairs and use a dict to track the
results of these iterations. 

Math: We leverage the combination of constraints given to us (a+b+c=p, p<1000, a^2+b^2=c^2) to reduce our search
space for [a,b] pairs. This is most notable in our calculating of b_max. 

"""

"""
Program Attempt 1:
To start, we will think of relevant mathematical relationships between perimeter (a+b=c) and right angle (a^2+b^2=c^2).
Let us iterate over different [a,b] pairs, calculating c values and validating if it satisfies the Pythagorean condition. 
If so, take a note of its perimeter. We'll have a data structure for storing perimeters and their counts. 
Now, we also should be smart about the ranges of a and b to iterate over, given the p < 1000 constraint. Using the other
two given equations (Pythagorean formula, perimeter formula), we get that b_max = 1000(a-500)/(a-1000). As such, we can
introduce a double nested loop: a from 1 to 500, and b from 1 to either b_max or a (to avoid duplicate sets), whichever is lower. 
"""


def calc_b_max(p: int, a: int) -> int:
    numer = p * (a - p // 2)
    denom = a - p
    return numer // denom


def main(p: int) -> int:
    from collections import Counter
    from math import sqrt

    perimeter_counts = Counter()

    for a in range(1, p // 2):
        b_max = calc_b_max(a, p)
        for b in range(1, min(a, b_max) + 1):
            c = sqrt(a**2 + b**2)
            if c.is_integer():
                perimeter_counts[a + b + c] += 1

    return perimeter_counts.most_common()[0][0]


if __name__ == "__main__":
    ans = main(1000)
    print(ans)
