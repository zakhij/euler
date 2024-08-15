
'''
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

Computational Analysis:

DSA:

Math:

'''

'''
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
'''

def check_cycle(i: int) -> int:
    digit_set = set()
    ctr = 0
    decimal = 1 / i
    for digit in str(decimal)[2:]:
        if digit == '0':
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
    for i in range(2,n):
        cycle_count = check_cycle(i)
        if cycle_count > max:
            max = cycle_count
            max_num = i
    return max_num

if __name__ == '__main__':
    ans = get_max_length_reciprocal_cycles_under_n(1000)
    print(ans)