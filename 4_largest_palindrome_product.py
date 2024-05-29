
'''
Problem Statement: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers 
is 9009 = 91 x 99. Find the largest palindrome made from the product of two 3-digit numbers.

Computational Analysis: O(n^2), where n is number of 3-digit numbers. This is a refined brute-force approach with a nested loop.

Math: No mathematical properties are used to significantly reduce the time complexity, but basic properties, like multiplicative symmetry 
and products scaling in proportion to their factors enable us to prune the search space.

'''


#Program Attempt 1
#Okay, so brute force would be to check every product combination of i and j where 100 <= i, j <= 999. That is SUPER inefficient.
#I think we'd need some strategy in the shape of "start i,j = 999, then decrement until we find a palindrome", but the difficulty
#is in determining the rules for decrementing (such that we don't skip over any pairs). I'm also having difficulty understanding
#if we can use previous solutions at all. Like, does the product of 994 and 982, even if not palindromic, reveal any info about what
#pairs to check next? Or do we treat each pair as its own independent shot at getting a palindromic product?
#Even assuming independence, I think, upon further reflection, math can help us pre-emptively reduce our search space. For example, knowing
#that for palindrome k, k[0] == k[-1] (first digit = last digit). I think ultimately this is what ChatGPT is going to tell me, that we can
#pre-emptively determine whether a product is doomed to fail just by looking at the digits of i and j, which saves a boatload of computation.
#For now though, I'll try the brute force method. I'll need a palindrome checker, a multiplier, and a combinatorial iterator. 

def palindrome_checker(product):
    string_product = str(product)

    for i in range(len(string_product)):
        if string_product[i] == string_product[-1-i]:
            continue
        else:
            return False
    return True

def iterator(low, high):
    best = 0
    for i in range(high+1,low,-1):
        for j in range(high+1, low, -1):
            product = i * j
            isPalindrome = palindrome_checker(product)
            if isPalindrome and product > best:
                best = product
    return best
            

#Program Attempt 2
#My suspicions proved to be wrong, actually. I expected there to be some reduction of search space via math pre-emptively knowing what's
#not a palindrome (and so avoiding the product calculation entirely), but nope! Program attempt 1 worked just fine. There are some slight
#improvements to be made to prune the search space, though, namely in the j loop. We iterate from i to j to avoid redundant calculations,
#and we break out of that j loop early if we find a palindrome (because we decrement j, all other palindromes in that j loop will necessarily
#of a lesser value, so no point in looking for them). With these improvements, runtime goes from 0.178 seconds to 0.002 seconds! So about a 100x
#increase, actually! (We probably search only 1/100 of the space as we do in the first program attempt).

def palindrome_checker2(product):
    return str(product) == str(product)[::-1]

def iterator2(low, high):
    best = 0
    for i in range(high+1,low,-1):
        for j in range(i, low, -1):
            product = i * j
            isPalindrome = palindrome_checker2(product)
            if product < best:
                break
            if isPalindrome and product > best:
                best = product

    return best

if __name__ == '__main__':
    import time
    start = time.time()
    answer = iterator2(100,999)
    print(answer)
    end = time.time()
    print(start-end)
