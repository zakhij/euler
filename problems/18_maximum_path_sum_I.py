
'''
Problem Statement:By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23:
3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, 
Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute 
force, and requires a clever method! ;o)

Computational Analysis: Runtime complexity is O(N), with N being the count of numbers in the pyramid. We visit
each number once in our computations via the loop, doing constant work (update-in-place operation + max comparison).
Space complexity is also O(N), matching the pyramid: we don't use additional overhead to keep track of separate routes.

DSA: We leverage a list of lists to iterate through the pyramid. And, we use dynamic programming to
iteratively build up to the max path sum, exploiting the fact that this dependency structure allows 
us to solve smaller subproblems first (determining the max path sum for nodes at the bottom 
of the pyramid) and then use these solutions to iteratively solve for larger subproblems. 
By the time we reach the apex of the pyramid, we have combined all subproblem solutions to get the final answer.

Math: No big math principles used here.

'''

#Program Attempt 1
#As the note suggests, we could just brute force this by trying literally every path. Also, a greedy algorithm 
#won't guarantee the optimal solution, because short-term maximizing could result in going off a path that's
#good in the long-term. Honestly, as I think about it, I think that the "clever method" outside of brute-force
#relies on recursion and memoization (not dissimilar to what I was thinking for lattice paths). Like, multiple
#paths will share the same start, so we could just cache those sub-paths, I'm thinking. Well, memoization is 
#still going to be used to compare each path against each other (so it'll probably not be good for the P67 version
#wher the number of paths explodes and we cant cache them all, but that's for later). Okay, the idea is still to
#try all possible paths. And we can save time by storing subpaths. 
#Cool. So we'll need a function that converts the string input into a list of lists. Then, we need a function
#that iterates through the list. More specifically, at each number, we can either choose left or right as our
#adjacent number: that spawns a new path. At the end, we should have a data structure that stores a sum value
#for each path, and we find the max of this data structure. The problem is: how do we perform iteration? Actually, 
#maybe this should be approached like a weighted graph problem: we perform DFS to brute-explore all paths. But then, how
#do we ensure that a path has been visited? Well, maybe we just do backtracking...
#Actually, upon consulting ChatGPT, it seems like DP is the best way. More specifically,
#bottom up, since that means we have a lot fewer paths to compare. Basically, we visit
#each number once: at each number, we update it with the sum of itself and the larger
#of the two numbers below it.

def input_converter(input: str) -> list[list[int]]:
    lines = input.strip().split('\n')
    pyramid = [list(map(int, line.split())) for line in lines]
    return pyramid



def max_path_sum_finder(input_str: str) -> int:
    pyramid = input_converter(input_str)
    for i in range(len(pyramid) - 2, -1, -1):
        current_row = pyramid[i]
        prev_row = pyramid[i+1]
        for index in range(len(current_row)):
            current_row[index] += max(prev_row[index], prev_row[index+1])
    
    return pyramid[0][0]


#Program Attempt 2
#The first program works. But, I'm wondering if I could also use DP going from top to bottom.
# THE ANSWER IS YES!! Logic is a bit more complicated due to how sums are calculated going
# top-down, but yes, it's good.

def max_path_sum_finder_top_to_bottom(input_str: str) -> int:
    pyramid = input_converter(input_str)
    for i in range(1, len(pyramid)):
        current_row = pyramid[i]
        prev_row = pyramid[i-1]
        for index in range(len(current_row)):
            if index == 0:
                current_row[index] += prev_row[index]
            elif index == len(current_row) - 1:
                current_row[index] += prev_row[index-1]
            else:
                current_row[index] += max(prev_row[index], prev_row[index-1])
        
        
    return max(pyramid[-1])




if __name__ == '__main__':
    pyr = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
ans = max_path_sum_finder(pyr)
print(ans)
ans2 = max_path_sum_finder_top_to_bottom(pyr)
print(ans2)