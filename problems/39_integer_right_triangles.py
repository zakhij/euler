"""
Problem Statement:
If p is the perimeter of a right angle triangle with integral length sides {a, b, c},
there are exactly three solutions for p = 120: {20,48,52}, {24,45,51}, {30,40,50}.
For which value of p < 1000 is the number of solutions maximized?


Computational Analysis: Both program attempts seem similar in the sense that we use nested loops to iterate
across pairs, do some calculations, and write to a dict data structure. However, in the first attempt, the space
we iterate over is much larger: it's all [a,b] pairs that we know meet the perimeter requirement, but we must
test for pythagorean compliance. The space of both a and b scale linearly with this perimeter req, so the
runtime complexity is O(n^2), where n is the max allotted perimeter (even though we leverage some math principles
to cut the search space and in practice get better performance). In the second attempt, we iterate over all [m, n]
pairs, where the pairs are guaranteed to be pythagorean-compliant. The number of candidate m's grows at a rate
of sqrt(n). As such, the runtime complexity is O(sqrt(n)*sqrt(n)) = O(n). Space complexity in both cases is
is O(n), given our dictionary of perimeters. 

DSA: We use loops to to algorithmically iterate over the space of possible [a,b]/[m,n] pairs and use a dict to track the
results of these iterations. 

Math: In PA1, we leverage the combination of constraints given to us (a+b+c=p, p<1000, a^2+b^2=c^2) to reduce our search
space for [a,b] pairs. This is most notable in our calculating of b_max. In PA2, we leverage Euclid's formulation of 
Pythagorean triples to completely transform our approach to the problem, building valid Pythagorean triples from the
ground up rather than checking for Pythagorean compliance over a brute-force search, giving us much better performance.

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


"""
Program Attempt 2:
Our first solution works well, but we can do even better by exploiting some more math, specifically Euclid's pythagorean
triples formulation: a = k(m^2 - n^2), b = k(2mn), c = k(m^2+n^2) where m > n, m and n are coprime, and k is a scaling
factor. So instead of iterating over rather large nested loops in testing pairs, we could build valid pythagorean triples
from the ground up. We'd still use a nested loop, but it would be iterating over smaller ranges
Using this new formulation, we can describe the perimeter p = k(m^2-n^2 + 2mn + m^2+n^2) = 2km(m+n). We know that
the absolute minimum value of k is 1 and of n is 2. As such, using our p < 1000 constraint, we find that the max possible 
valid value of m is 21: 1000=2m(m+2) --> 500 = m^2 + 2m --> m^2 + 2m - 500 --> x = 21.4. 
"""


def calc_perimeter(k: int, m: int, n: int) -> int:
    return 2 * k * m * (m + n)


def main2(p: int) -> int:
    from math import gcd
    from collections import Counter

    perimeter_counts = Counter()

    for m in range(3, p // 2):
        for n in range(2, m):
            k = 1
            if gcd(n, m) == 1:
                while calc_perimeter(k, m, n) < p:
                    perimeter_counts[calc_perimeter(k, m, n)] += 1
                    k += 1
    return perimeter_counts.most_common()[0][0]


if __name__ == "__main__":
    ans = main2(1000)
    print(ans)
