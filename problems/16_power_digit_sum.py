
'''
Problem Statement: 2^15 = 32768 and the sum of its digits are 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of 2^1000?

Computational Analysis: The main runtime-based operation is sifting through the stringified number. The length
grows linearly with the exponent value, n (~0.303n precisely). Same goes for the space complexity.

DSA: No special data structures/algorithms used, just list comprehension

Math: No special math properties used, outside of calculating exponents and summing.

'''

#Program Attempt 1
#Lol so technically I could just compute in Python 2^1000 directly and sum up its digits. I'm not sure if that
#matches the spirit of the problem though. But how else am I supposed to get the sum of its digits? I assume
#I can only derive the sum of the digits by knowing the value of the digits. And while technically the placement
#of the digits doesn't matter in this problem, how else can I know the digit values without computing the value of
#2^1000? Oh well. 

def sum_digits(base: int, exp: int) -> int:
    num = base ** exp
    return sum(int(d) for d in str(num))


if __name__ == '__main__':
    an = sum_digits(2, 1000)
    print(an)