
'''
Problem Statement:
The Fibonacci sequence is defined by the recurrence relation:
F_n = F_{n - 1} + F_{n - 2}, where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:
F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144
The 12th term, F_12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Computational Analysis: Determining the runtime complexity requires answering two questions:
how many Fib terms do we need to iterate on, and how much computation is done per iteration?
The first question relies on understanding the relationship between the number of digits (n)
and the number of Fib terms.  The Fibonacci sequence grows exponentially, meaning that the 
number of terms needed to achieve a number of digits does not scale linearly with the number 
of digits, but rather grows at a logarithmic rate relative to the Fibonacci index. Now, the 
amount of computation done per term. It's O(1), as all we do is add the previous 2 terms 
and then access the first digit of the next and current terms. That means in total, the runtime 
complexity is O(logn). Space complexity is constant too. We don't use any data structures to 
store the Fib numbers, only pointers.

DSA: No data structures are deployed here. For algorithms, we use Fibonacci's recursion but 
retrofitted as a while loop to avoid recursive stack overflow.

Math: This problem revolves around the Fibonacci sequence, most clearly. However, we also use
a key mathematical insight regarding the value of the first digit of consecutive terms to 
optimize the computational complexity of work done inside the loop. More specifically, we notice
that if a term's first digit is greater than its subsequent term's first digit, that necessarily
implies an +1 increase to the digit count.

'''

'''
Program Attempt 1:
My first observation is that we're going to be dealing with really big numbers.
Thankfully, Python mitigates this issue with its arbitrary-precision integers. 
So, we could brute-force a check along the fibonacci sequence: at each number,
check the number of digits it has and stop once we hit 1000. This is, of course,
assuming we cannot directly access the Fib sequence with X digits, which I don't
think is possible. I think there are some definite inefficiencies with this strategy,
namely we don't exploit the fact that there will be a relationship in the number
of digits between the Xth and X+1th # of digits... Hmm, I'm thinking of something now. 
If the X+1th term's first digit is less than the Xth term's first digit, then that must
mean we've gone up a level, right? So all we really need to check is the first digit!
'''
def fibber(last, current, term_count, digit_count, limit) -> int:
    if digit_count >= limit:
        return term_count
    next = current + last
    if str(current)[0] > str(next)[0]:
        return fibber(current, next, term_count+1, digit_count+1, limit)
    else:
        return fibber(current, next, term_count+1, digit_count, limit)


'''
Program Attempt 2:
First attempt fails due to recursive overflow, we make too many recursive calls (over
a thousand). So instead of recursion, we will use a while loop.
'''

def fibber2(limit: int) -> int:
    last = 1
    current = 1
    term_count = 2
    digit_count = 1
    while True:
        if digit_count >= limit:
            return term_count
        
        next = current + last
        if str(current)[0] > str(next)[0]:
            digit_count += 1
        
        term_count += 1
        last = current
        current = next



if __name__ == '__main__':
    #ans = fibber(1, 1, 2, 1, 1000)
    ans = fibber2(100)
    print(ans)