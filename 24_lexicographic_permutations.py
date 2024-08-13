
'''
Problem Statement:
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Computational Analysis:

DSA:

Math:

'''

'''
Program Attempt 1:
I'm unsure if we can directly access the Xth lexicographic permutation. Maybe we can, however, efficiently go
from the Xth to the X+1th lexicographic permutation. If we can, then we can just count up to 1 million. If we cannot,
then we need to further brute force it: count up and iterate across all 10-digit integers: at each integer,
check if it's a lexicographic permutation. If so, increment a counter. Do this until we hit 1 million on the counter.
I want to first focus on this secondary approach. The question becomes, however, how can we efficiently check if 
a number is a lexicographic permutation? We can iterate over the digits of the given integer, and if there are any
duplicates, we know it cannot be lexicographic.
UPDATE: It takes 11 seconds when n=10,000 and 110 seconds when n=100,000. So the implementation should take
1100 seconds, or 18 min, for n=1M. Not good. I think we need to change our high-level strategy. 
'''

def is_lexicographic(n: int) -> bool:
    s = set()
    for digit in str(n):
        if digit in s:
            return False
        else:
            s.add(digit)
    
    return True

def nth_lexicographic_permutation(n: int) -> int:

    ctr = 1 #Start at 1 to capture 0123456789
    
    i = 1000000000 #First 10-digit integer

    while ctr < n:
        if is_lexicographic(i):
           # print(f"{i} is lexo, #{ctr}")
            ctr += 1
        i +=1
    
    return i-1

'''
Program Attempt 2:
Okay, the brute-force method in PA1 is simply taking way too long. I think we need to go back to the originally
discussed idea of directly calculating the X+1th lexicographic permutation and then going up to the millionth term
that way. This is going to be a bit more complex and will instead involve playing around with the digits, I think.

'''

if __name__ == '__main__':
    import time
    start = time.time()
    ans = nth_lexicographic_permutation(100000)
    end = time.time()
    print(ans)
    print(end-start)