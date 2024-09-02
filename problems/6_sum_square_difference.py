
'''
Problem Statement: 
The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025. Hence the 
difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025 - 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.

Computational Analysis: O(1). We can compute the sum of 1-N and sum of squares of 1-N in constant time.
We also use constant space in this formula. 

Math: Going from O(N) to O(1) involves applying the Sum of the First n Natural Numbers (and its derivative
for sum of squares of the First n Natural Numbers).

'''

#Program Attempt 1
#This problem on its surface looks really easy to solve. I can quite easily put together an O(N) solution
#by iterating from 1 to N and doing the necessary (constant-time-per-number) operations to add to the sums.
#Then at the end, one-time squaring and subtraction. 
#Result: I feel like this is too easy... perhaps there is another
#way to get this done in less than O(N) time?

def difference(N):
    sum_of_squares = 0
    sum_to_be_squared = 0
    for n in range(1,N+1):
        sum_of_squares += n**2
        sum_to_be_squared += n
    squared_sum = sum_to_be_squared ** 2
    return squared_sum - sum_of_squares


#Program Attempt 2
#Upon further investigation, it appears that we can get this to O(1) by exploiting a mathematical shortcut 
#formula, sum(n) = n(n + 1)/2. There's a similar formula for calculating the sum of squares, which is
#sum of Squares(n)= n(n+1)(2n+1)/6. 
#Result: It works!
 
def sum_of_squares_1_to(N):
    return (N * (N + 1) * (2*N + 1)) / 6

def sum_1_to(N):
    return (N * (N + 1)) / 2


def difference2(N):
    return sum_1_to(N) ** 2 - sum_of_squares_1_to(N)

if __name__ == '__main__':
    #answer = difference(100)
    #print(answer)
    answer2 = difference2(100)
    print(answer2)