
'''
Problem Statement: Starting in the top left corner of a 2x2 grid, and only being able to move to the right
and down, there are exactly 6 routes to the bottom right corner (RRDD, RDRD, RDDR, DRRD, DRDR, DDRR). How
many such routes are on a 20x20 grid?

Computational Analysis: The underlying runtime complexity of calculating the binomial coefficient (2n n) is O(n),
as it can which can be efficiently computed using optimized algorithms that handle factorial operations in linear time. 
Space complexity is constant. 

DSA: No special data structures or algorithms are used here.

Math: The problem is approached through combinatorics, specifically leveraging the binomial coefficient to count 
the distinct permutations of paths consisting of D and R moves. Each path can be uniquely identified by the 
sequence of these moves, where both the number of D and R operations are equal to the grid's dimension, n.

'''

#Program Attempt 1
#Okay so intuitively, I feel like there must be some underlying relationship between the size of the grid and the
#number of routes. Actually, even better, I feel like this is a DP problem. Like for instance, the 2x2 grid contains
#instances of the 1x1 grid problem, right? And there are multiple ways to get to the 1x1 grid setup. So similarly, 
#calculating 3x3 grid routes would be like "how many unique ways are there to get to the 2x2 grid problem"? Then
#multiply that number by 6. But also, keep in mind the all-down and all-up approaches... that complicates things.
#Okay, so I feel like it is some form of recursion, DP, but the exact implementation, I'm unsure on....
#Ok, back from the top. So our base case is when we are at the bottom right of the 20x20 grid. Then, we have 0
#moves left. The question we ask: what positions can directly precede it? The answer is to the left one or up one
#(such that, from those positions, we get to the bottom right by either doing R or D respectively). Okay, cool.
#Now for each of those positions, what positions can directly precede it? That's the recursive element: we continue
#asking this question for each position, but make sure we keep within the 20x20 bounds (i.e., can't do D 21 times).
#Wait a minute... I'm wondering if we can calculate this very fast using some permutation formula. Like, each route
#will be a list with 20 R's and 20 D's. We just need to find all possible combinations of this, and we're set. But
#is there a mathematical formula/shortcut I could employ here? According to ChatGPT, yes there is: use the binomial
#coefficient formula to get the number of combinations. Simple.

def routes_counter(n: int) -> int:
    import math
    return math.comb(2*n, n)

if __name__ == '__main__':
    ans = routes_counter(20)
    print(ans)
    pass