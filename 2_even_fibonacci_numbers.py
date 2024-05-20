

"""
Solution Type: Recursion
Computational Analysis: O(n), where n is number of terms in Fib sequence before 4M
Math: Although not utilized in my program, it's provable that every third Fib term is even. 
Implementing this would provide modest gains by avoiding checking for evenness on every term.
"""

#Program Attempt 1
def fibber(sum, before, current):
    val = before + current
    if val > 4000000:
        return sum

    else:
        if val % 2 == 0:
            return fibber(sum+val,current,val)
        else:
            return fibber(sum,current,val)

sum = fibber(2, 1, 2)
print(sum)

