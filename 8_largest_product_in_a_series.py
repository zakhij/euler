

'''
Problem Statement:
The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

Computational Analysis: O(N), where N is the number of digits in the number. The length of the sliding window is irrelevant. The
amount of computation done per sliding window instance is constant. 

DSA: We use a queue data structure to for an efficient implementation of the sliding window, thanks to its constant-time append
and pop operations. Other than that, we make use of simple loops for iteration and counters for tracking. 

Math: We don't make use of any major mathematical principles, other than understanding the rules of multiplication (especially 
concerning multiplying 0). 
'''

#Program Attempt 1
#I think this can be done in one pass-through. The idea is simple: Initialize a 13-length array that will slide over the 
#digits of this number. Start the array at N[0] (and up to N[12]). Then, multiply the numbers together to get the total product.
#Set this as the max product seen so far. Then, start sliding: pop N[0], divide the current product by it, then recruit N[13],
#including multiplying it into the current product. Compare it with the max product. Continue this until we reach the end.

def func(stringN: str) -> int:
    from collections import deque
    q = deque()
    zeroes = 0
    current_max = 1
    for l in stringN[:13]:
        q.append(int(l))
        current_max *= int(l)

    highest_max = current_max
    print(q)
    for l in stringN[13:]:
        popped = q.popleft() #0 is a problem
        current_max /= popped
        current_max *= int(l)
        if current_max > highest_max:
            highest_max = current_max
        q.append(int(l))

    return highest_max

#Program Attempt 2
#Hmmm. 0 is a problem. Because it destroys any product value. We need to keep track of the placement of 0s. 
# More specifically, discard any arrays that have 0 in it. I think we need to add additional logic that 
# checks for 0. Maybe by using a counter? So we first consult the counter (checking for 0s) before calc'ing
#the product of the current 13-digit window. I think for this first working implementation, we just focus
#on handling the 0. We discard the sliding window concept, which means that whenever the 13-digit window
#doesn't have 0, we have to multiply all 13 digits. This is still O(N) technically, but definitely longer.
#The optimizations of removing redundant multiplication computation can come later though.

def func2(stringN: str) -> int:
    zero_counter = 0
    highest_max = 0
    from collections import deque
    q = deque()

    for l in stringN[:13]:
        q.append(int(l))
        if int(l) == 0:
            zero_counter += 1
        
    if zero_counter == 0:
        print(q)
        current_max = 1
        for item in q:
            current_max *= item
        highest_max = current_max
    
    for l in stringN[13:]:
        popped = q.popleft()
        if popped == 0:
            zero_counter -= 1
        
        q.append(int(l))
        if int(l) == 0:
            zero_counter += 1

        if zero_counter == 0:
            current_max = 1
            for item in q:
                current_max *= item
            if current_max > highest_max:
                highest_max = current_max
    return highest_max


#Program Attempt 3
#Ok, so program attempt 2 works. But it is pretty inefficient, and there's some code redundancy we can clean up.
#Let's tackle these separately. So the first issue, the inefficiency: the main issue is that we iterate over the
#entire 13-digit window every time we slide the window (given that zero_counter == 0). I think we can retrofit
#the sliding window logic from Attempt 1 to address this and, in theory, improve performance by 13x. Next, the
#code redundancy can be cleaned up by adding helper functions to abstract out some of the functionality. 


def optimized_product_finder(digits: str) -> int:
    from collections import deque

    q = deque()
    current_max = 1
    highest_max = 0
    zero_counter = 0

    for l in digits[:13]:
        q.append(int(l))
        if int(l) == 0:
            zero_counter += 1
        else:
            current_max *= int(l)
    
    if zero_counter == 0:
        highest_max = current_max
    
    for l in digits[13::]:
        outgoing = q.popleft()
        
        q.append(int(l))

        if int(l) == 0:
            zero_counter += 1
        else:
            current_max *= int(l)

        if outgoing == 0:
            zero_counter -= 1
        else:
            current_max //= outgoing
        
        if zero_counter == 0 and current_max > highest_max:
            highest_max = current_max
    return highest_max
        







if __name__ == '__main__':
    giant_N = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
    
    # Remove newline characters
    giant_N = giant_N.replace('\n', '')
    
    v = optimized_product_finder(giant_N)
    print(v)
    
    