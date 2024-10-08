"""
Problem Statement:
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify 
it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 4s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator. If the product of these four fractions 
is given in its lowest common terms, find the value of the denominator.

Computational Analysis: While there isn't an input variable n to cleanly describe the computational
complexity with, we should still note that the runtime includes a nested loop on three variables:
the denominator, the numerator, and the extra digit. The extra digit range is constant, while the
denominator and numerator ranges are dictated by the specific problem condition (containing 2 digits).
The helper function inside the nested loop is constant, however. Space complexity is dictated by
the two data structures for storing numerators and denominators. In theory, though, these are not 
necessary, and so it could be constant.

DSA: Our strategy boils down to combinatorial exploration: iterating over the entire possible solution
space and checking each potential solution. 

Math: We leverage some math principles for micro-optimizations of our solution, such as observing that
the numerator must be smaller than the denominator and that the extra digit must be placed at the back
of the numerator and the front of the denominator. Additionally, we use gcd when getting the final solution.

"""

"""
Program Attempt 1:
I wish "trivial example" was defined more concretely. Does it just mean when we cancel out a 0? I assume
so. Anyways, this seems like a hard problem, an unexpected intersection between digit manipulation and
fractional values. There has to be some underlying pattern to exploit, right? Let's look at the freebie
given, 49/98 -> 4/8, and see if it gives us any hints as to what to look for...
Right away, one key observation is that the 4 and the 8 are not located in the same digit spot in the 
larger fraction; this makes sense, as I believe the only case where they could be in the same digit spot
is for trivial examples like 10/20. I see that 4 and 8 are both even, but I'm not sure if this is
an absolute necessity. 
Something I am also thinking about is whether we can directly arrive at the fractions, or if we need
to iterate over a space of potential candidates. I assume it's the latter. But then I think, what
space is there to iterate over? The space is not clearly defined, we'd need to intuit it ourselves based
on the derived rules. 
Okay, so breaking it down, we have 2 components: the original numerator, the original denominator, the extra
digit, the index of the extra digit in the numerator, and the index of the extra digit in the denominator.
We follow these rules:
- Original denominator > original numerator
- Extra digit is 1-9
- The index of the extra digit in the numerator > index of the extra digit in the denominator
Hmmm. I still don't have confidence in this approach. WAIT! I'm so silly, I'm forgetting a key thing, that
we are only examining fractions where the numerator and denominator each contain 2 digits, just like
the provided example of 49/98. Okay, that greatly reduces the search space. So now, let's think about
what components we need... We need a nested loop to iterate over all valid numerator and denominator pairs,
and we need to iterate over all valid extra digit values for each pair. We need a helper function to 
determine whether a given numer, denom, and extra digit is valid for this exercise. We need to contain 
all the valid fractions. Then, we need a helper function that can provide us the end result, the simplified
denominator of the product of all valid fractions.
"""


def is_valid_fraction(numer: int, denom: int, digit: int) -> bool:

    new_numer = int(str(numer) + str(digit))
    new_denom = int(str(digit) + str(denom))

    return new_numer / new_denom == numer / denom


def main() -> None:
    import math

    numers = []
    denoms = []
    for denom in range(2, 10):
        for numer in range(1, denom):
            for digit in range(1, 10):
                if is_valid_fraction(numer, denom, digit):
                    numers.append(numer)
                    denoms.append(denom)
                    print(f"numer {numer}, denom {denom}, digit {digit}")

    product_numer = 1
    for numer in numers:
        product_numer *= numer

    product_denom = 1
    for denom in denoms:
        product_denom *= denom

    numer_gcd = math.gcd(product_numer, product_denom)
    print(product_denom // numer_gcd)


if __name__ == "__main__":
    main()
