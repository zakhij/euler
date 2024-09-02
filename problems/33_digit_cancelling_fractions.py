"""
Problem Statement:
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify 
it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 4s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator. If the product of these four fractions 
is given in its lowest common terms, find the value of the denominator.

Computational Analysis:

DSA:

Math:

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
Hmmm. I still don't have confidence in this approach. Let's ask ChatGPT...

"""


if __name__ == "__main__":
    pass
