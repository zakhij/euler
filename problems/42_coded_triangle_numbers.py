"""
Problem Statement:
The nth term of the sequence of triangle numbers is given by, t_n = (1/2)*n*(n+1); so the 
first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55,...
By converting each letter in a word to a number corresponding to its alphabetical position and adding 
these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. 
If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

Computational Analysis: I was going to say that our solution is O(n) where n is the number of words, but it's more
accurate to describe it as O(k), where k is the number of letters in the text file. We do some constant work
per word regarding solving the formula, yes, but we also do some work per letter in determining its score.
Space complexity is O(n) due to holding all the words when reading the text file.

DSA: No special data structures or algorithms used. 

Math: We solve for n in the triangle numbers equation given, using a discriminant, in checking for triangle number
validity. 

"""

"""
Program Attempt 1:
I think the solution is pretty straightforward: iterate across each word in the text file and run each
through some triangle number checker. 
"""


def is_triangle_word(word: str) -> bool:
    import math

    t_n = sum(ord(c) - 64 for c in word)

    discriminant = 1 + 8 * t_n

    sqrt_discriminant = int(math.isqrt(discriminant))
    if sqrt_discriminant * sqrt_discriminant != discriminant:
        return False

    n = (-1 + sqrt_discriminant) / 2

    return n.is_integer() and n >= 0


def main() -> int:
    with open("problems/0042_words.txt") as f:
        words = f.read().replace('"', "").split(",")

    return sum(1 for word in words if is_triangle_word(word))


if __name__ == "__main__":
    ans = main()
    print(ans)
