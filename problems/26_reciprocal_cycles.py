"""
Problem Statement:
A unit fraction contains 1 in the numerator. The decimal representation of the unit 
fractions with denominators 2 to 10 are given:
1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666... and has a 1-digit recurring cycle. It can be seen 
that 1/7 has a 6-digit recurring cycle. Find the value of d < 1000 for 
which 1/d contains the longest recurring cycle in its decimal fraction part.

Computational Analysis: The runtime complexity of this solution is O(n^2) and
the space complexity is O(n), both due to the worst-case scenario of looking
at the n-1 sized remainder space for a given digit per check_cycle call. 
DSA: We leverage a dictionary data structure to keep a mapping of remainders to their
positions, such that we can both quickly detect duplicate remainders and determine their
length.
Math: Our solution effectively carries out long division by "hand", keeping track of
the remainder along the way. 

"""

"""
Program Attempt 1:
This problem seems challenging on a multitude of levels. For starters, how can you even 
tell what the reciprocal cycle is for a given decimal? Can you just say "as soon as
we see a repeated digit"? But what about a sequence like "73795" where there are two
of the same digit in the cycle? Is that even possible though given the rules of division?
I don't think so... Well, The other thing I was going to mention is whether we can take 
shortcuts, or if we'd have to independently determine the reciprocal cycle for each, 
but we can ignore that, for now at least. We cannot just say "stop as soon as you see
a repeated digit", take 1/999 for instance: 0.001001001. The 1001 is a cycle, but because
it's .001, we hit 2 zeroes before ever getting a chance. Maybe a workaround is to exclude
zeroes? That feels janky.
"""


def check_cycle(i: int) -> int:
    digit_set = set()
    ctr = 0
    decimal = 1 / i
    for digit in str(decimal)[2:]:
        if digit == "0":
            continue
        if digit in digit_set:
            return ctr
        else:
            ctr += 1
            digit_set.add(digit)

    return 0


def get_max_length_reciprocal_cycles_under_n(n: int) -> int:
    max = 0
    max_num = 0
    for i in range(2, n):
        cycle_count = check_cycle2(i)
        if cycle_count > max:
            max = cycle_count
            max_num = i
    return max_num


"""
Program Attempt 2:
Yep, first attempt failed miserably. I am still unsure about what high-level approach
would work best: should I evaluate the decimals as-is? Can I instead focus on the
denominator value (i.e., perhaps there's a relationship between prime numbers as the
denominator and the presence/length of a reciprocal cycle)? The problem I'm currently
facing is creating a robust cycle detection function. Maybe I can borrow from graph
algorithms, specifically from DFS. And also, I should ignore the first few 0's. I
can do this by bucketing the input into different bands: If the denom is between 1-10,
we expect 0.X. 11-100, 0.0X, 101-1000: 0.00X. 
OKAY ACTUALLY. Upon consulting ChatGPT, I'm going about this wrong. The cycle detection
should be done by carrying out long division and examining the remainder! I was looking
at the repeating digit, but I need to look for a repeating reminder. 

"""


def get_max_length_reciprocal_cycles_under_n2(n: int) -> int:
    max = 0
    max_num = 0
    for i in range(2, n):
        cycle_count = check_cycle2(i)
        if cycle_count > max:
            max = cycle_count
            max_num = i
    return max_num


def check_cycle2(d: int) -> int:
    remainders = {}
    remainder = 1
    position = 0

    while remainder != 0 and remainder not in remainders:
        remainders[remainder] = position
        remainder = (remainder * 10) % d
        position += 1

    if remainder == 0:
        return 0
    else:
        return position - remainders[remainder]


if __name__ == "__main__":
    ans = get_max_length_reciprocal_cycles_under_n2(1000)
    print(ans)
