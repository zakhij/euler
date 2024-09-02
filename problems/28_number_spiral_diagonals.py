"""
Problem Statement:
Starting with the number 1 and moving to the right in a clockwise direction a 5x5 spiral is formed as follows:
21 22 23 24 25
20 7  8  9  10
19 6  1  2  11
18 5  4  3  12 
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101
What is the sum of the numbers on the diagonals in a 1001x1001 spiral formed in the same way?

Computational Analysis: Runtime complexity is O(n), as we perform constant work in each diagonal,
and the number of diagonals scales linearly with the length (n) of the spiral. Space complexity
is constant, as we only use pointers that we update.

DSA: We are able to directly iterate across all diagonals by following the designated pattern,
only needing to use pointers and basic arithmetic to increase the step size. 

Math: No special rules, unless we want to consider the diagonal pattern of this pattern a
special mathematical property. 

"""

"""
Program Attempt 1:
Summing the diagonals seems pretty simple, since they follow a rudimentary pattern:
x_n+1 = x_n + c. Do this 4 times, then c+= 1. The other component is keeping track
of the length, making sure we stop when we hit the designated length of 1001. But yes,
the solution seems rather simple: iterate across the diagonals, keeping pointers updated
and stop once we hit the length.
"""


def sum_number_spirals(length: int) -> int:
    sum = 1
    current_length = 3
    increase = 2
    current_val = 1

    while current_length <= length:
        for _ in range(4):
            current_val += increase
            sum += current_val

        increase += 2
        current_length += 2

    return sum


if __name__ == "__main__":
    ans = sum_number_spirals(1001)
    print(ans)
