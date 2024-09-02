
"""
Problem Statement: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

"""



def sum_3s_and_5s(n):
    running_sum = 0
    for i in range(n):
        if i % 3 == 0:
            running_sum += i
        elif i % 5 == 0:
            running_sum += i
    
    return running_sum


def sum_3s_and_5s_smarter(target):
    sum_of_3_multiples = sum_divisibles_by(3,target)
    sum_of_5_multiples = sum_divisibles_by(5,target)
    sum_of_15_multiples = sum_divisibles_by(15,target)
    return sum_of_3_multiples + sum_of_5_multiples - sum_of_15_multiples



def sum_divisibles_by(n,target):
    number_of_terms = (target - 1) // n
    return n * (number_of_terms+1)*number_of_terms//2



if __name__ == '__main__':
    first_attempt = sum_3s_and_5s(1000)
    print(first_attempt)
    second_attempt = sum_3s_and_5s_smarter(1000)
    print(second_attempt)

