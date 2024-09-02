
'''
Problem Statement: If the numbers 1 to 5 are written out in words: one, two, three, four, five, then 
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the numbers from 1 to 1000 (one thousand) 
inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is 
in compliance with British usage.

Computational Analysis: Thanks to memoization, the runtime complexity is O(N). Each number 1 to N is processed
exactly once, each processing involves a constant amount of work, including dictionary lookups and simple string 
operations. The space complexity is O(N), reflecting the memoization table

DSA: Dictionaries are key here, serving two primary purposes: mapping single digits/teens to their word forms, and 
storing precomputed results (memoization) to optimize the recursive decomposition of numbers. We use recursion to 
break down each number into manageable sub-components (hundreds, tens, and units), which each can be processed on
their own. Memoization ensures we avoid redundant processing, converting what would be an exponential problem into 
a linear one by caching results of subproblems.

Math: Not many math principles are used here. We do perform some simple division/modulo by 10 when navigating
across digits' places in a given number. 

'''

#Program Attempt 1
#My initial thought is we iterate from 1 to 1000, running each number through a special function that outputs 
#the number of letters in it. What is that special function? I imagine it analyzes each digit, along with its 
#placement, and determines the number of letters associated with the digit+placement combo (i.e. 4 in the 
#last place is "four", while in the second to last place is "forty"). So, we need a dictionary to map the 
#digit+placement with the designated letter count. The question is, what should that dictionary look like?
#How do we incorporate both digit and placement? What about eleven, twelve, thirteen, fifteen, eighteen? 
#Hmmm. I'm actually thinking the best data structure might be some sort of tree, where the different digits'
#place are represented by different layers (the deeper the tree, the more significant the digit). That can
#cleanly represent 1 --> 2 being twelve.
#ACTUALLY, WAIT. Nevermind the tree structure. I should implement some type of backtracking-ish algorithm
#to avoid redundant computation on subsequent numbers. For example, if I'm at 322, then going to 323, I 
#shouldn't have to recalculate the "three hundred and twenty" part. So yes, probably still a dict, and make
#sure in implementation to have separate variables for the separate placements. 


def letter_counter(x: int, num_digits: int) -> int:
    dict_teen = {0: 3, 1: 6, 2: 6, 3: 8, 4: 8, 5: 7, 6: 7, 7: 9, 8: 8, 9: 8}

    dict1 = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
    dict2 = {0: 0, 2: 6, 3: 6, 4: 6, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
    
    power_of_ten = 10 ** (num_digits - 1)
    if num_digits == 1:
        return dict1[x]
    elif num_digits == 2 and x//10 % 100 == 1:
        return dict_teen[x%10]
    
    if num_digits == 2:
        return dict2[x // power_of_ten] + letter_counter(x % power_of_ten, num_digits-1)
    
    if num_digits == 3:
        if x % power_of_ten == 0:
            return dict1[x // power_of_ten] + 7 #"hundred"
        else:
            return dict1[x // power_of_ten] + 10 + letter_counter(x % power_of_ten, num_digits-1) #"hundred and"
    
    if num_digits == 4:
        return 11 #"one thousand"

    power_of_ten = 10 ** (x - 1)
    return x % power_of_ten

def number_letter_counter_to_n(n: int) -> int:
    import math
    sum = 0
    for i in range(1,n+1):
        num_digits = int(math.log10(i)) + 1
        sum += letter_counter(i, num_digits)
    
    return sum


#Program Attempt 2
#My first attempt failed. I notice, however, I think a pattern improvement. We should memoize our letter counts,
#similar to the lattice paths problem. Like, for 987, we already saw "87", so we should store the length of 87 in
#ANOTHER dict with the understanding that we only use the first few dicts if we come across a number we've never
#seen before. I did also double check my dict values, some of them WERE off. But they should be good now...

dict2 = {0: 0, 2: 6, 3: 6, 4: 6, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
dict1 = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}

d_already_seen = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}

def count_letters_in_n(x: int, num_digits: int) -> int:
    if x in d_already_seen.keys():
        return d_already_seen[x]
    
    power_of_ten = 10 ** (num_digits - 1)

    if num_digits == 2:
        cnt = dict2[x // power_of_ten] + letter_counter(x % power_of_ten, num_digits-1)
        d_already_seen[x] = cnt
        return cnt
    
    if num_digits == 3:
        if x % power_of_ten == 0:
            cnt = dict1[x // power_of_ten] + 7  #"hundred"
            d_already_seen[x] = cnt
            return cnt
        else:
            cnt = dict1[x // power_of_ten] + 10 + letter_counter(x % power_of_ten, num_digits-1) #"hundred and"
            d_already_seen[x] = cnt
            return cnt
    
    if num_digits == 4:
        return 11 #"one thousand"


def number_letter_counter_to_n2(n: int) -> int:
    import math
    sum = 0

    for i in range(1,n):
        num_digits = int(math.log10(i)) + 1
        sum += count_letters_in_n(i, num_digits)
    
    return sum
    
    
#Program Attempt 3
#Hmmm. My 2nd program attempt gave me the same exact answer (in the same execution time) as 1st program attempt.
#After consulting ChatGPT, I had the right idea for memoization, but my implementation was off. Now, here's
#the GPT-guided implementation:
words = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

# Tens dictionary
tens = {
    20: 'twenty', 30: 'thirty', 40: 'forty',
    50: 'fifty', 60: 'sixty', 70: 'seventy',
    80: 'eighty', 90: 'ninety'
}

memo = {}

def number_to_words(n):
    if n in memo:
        return memo[n]
    

    if n < 20:
        return words[n]
    if n < 100:
        if n in tens:
            result = tens[n]
        else:
            result = tens[n // 10 * 10] + words[n % 10]
        memo[n] = result
        return result
    if n < 1000:
        remainder = n % 100
        if remainder == 0:
            result = words[n // 100] + 'hundred'
        else:
            result = words[n // 100] + 'hundredand' + number_to_words(remainder)
        memo[n] = result
        return result
    if n == 1000:
        return 'onethousand'
    

def letter_count(n):
    words = number_to_words(n)
    return len(words)

def number_letter_counter_to_n3(n):
    total = 0
    for i in range(1, n + 1):
        total += letter_count(i)
    return total


if __name__ == '__main__':
    import time
    start = time.time()
    ans = number_letter_counter_to_n3(1000) 
    end = time.time()
    print(ans)
    print(end - start)
