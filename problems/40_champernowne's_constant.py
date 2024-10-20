"""
Problem Statement:
An irrational decimal fraction is created by concatenating the positive integers:
0.12345678910111213141516171819202.
It can be seen that the 12th digit of the fractional part is 1.
If d_n represents the nth digit of the fractional part, find the value of the following expression.
d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000.

Computational Analysis: Our solution has a runtime complexity of O(n), where n is the greatest 
digit we're looking for (in this case, 1000000). We have a space complexity of O(1), since
our solution leverages pointers rather than a list data structure.

DSA: Our solution is ultimately brute force, as we iterate through all digits until we get the nth sequence entry.
We don't leverage any noteworthy algorithms, and we use pointers for iterating through digits. We do use
a set for fast membership lookup, though.

Math: No special math properties are leveraged here.

"""

"""
Program Attempt 1:
The decimal part is irrelevant to this problem. Ultimately, given an index i (equivalent to d_n), 
we want to know what the value is at that index in the sequence of consecutive integers. This
seems... pretty easy then. We'd throw a bunch of consecutive integers into a list and then just
pull out the values we need for the stated d_i's.  
"""


def listify_int(n: int) -> list[int]:
    return [int(x) for x in str(n)]


def main(d_n_list: list[int]) -> int:
    final = 1
    ctr = 0
    n = 1

    end = d_n_list[-1]
    d_n_set = set(d_n_list)
    while ctr < end:
        list_n = listify_int(n)
        for d in list_n:
            ctr += 1
            if ctr in d_n_set:
                final *= d
        n += 1

    return final


if __name__ == "__main__":
    ans = main([1, 10, 100, 1000, 10000, 100000, 1000000])
    print(ans)
