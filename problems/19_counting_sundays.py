
'''
Problem Statement:
You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday. Thirty days has September, April, June and November. All the rest have thirty-one, 
Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Computational Analysis: Runtime complexity is O(N), where N represents the number of days we look at. We
do a constant amount of work per day (create datetime object, check weekday/day properties). Of course,
this assumes that the datetime method calls are constant time. Space complexity is O(1): we don't use any 
lists, only a counter. 

DSA: In our final implementation, we don't use any special data structures or algorithms. Not even lists!
Just a counter and a for loop. And the datetime method calls abstract away algorithmic complexity.

Math: In theory, we rely on the math rules determined by the Gregorian calendar. But the datetime library
abstracts that away for us, thankfully. 

'''

'''
Program Attempt 1
There are a couple ways I envision doing this. So ultimately, we could use a "does this
fall on Sunday" checker function and a "does this fall on the 1st of the month checker".
More specifically, iterate from 1-X days elapsed since the start date, where
X represents the # of days between 12/31/2000 and 1/1/1901. I think the Sunday checker
is more trivial. Thus, we can just iterate over each Sunday (aka checking every 7th day
from 7-X) and check to see if it falls along the first of the month.
WE COULD ALSO separately compute a list of Sundays and list of 1st of months then do
some union operation on the 2 data structures, and perhaps that's faster than running
an arbitrary x value through the "does this fall on the 1st" checker function. Hmmm.
I think I like that approach better. 
The hard part of the problem is definitely seeing what falls on the 1st of the month.

'''
import time
def is_leap_year(year_offset: int) -> bool:
    return year_offset % 4 == 0

def construct_list_of_firsts(end: int) -> list[int]:
    firsts = [1]
    year_offset = 0
    while year_offset < end - 1:
        firsts_of_year = []
        if is_leap_year(year_offset):
            firsts_of_year.extend([1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336])
        else:
            firsts_of_year.extend([1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335])
        
        firsts.extend(map(lambda x: x + year_offset, firsts_of_year))
        year_offset += firsts_of_year[-1] + 31
    return firsts

def construct_list_of_sundays(end: int) -> list[int]:
    return [day for day in range(1, end) if day % 7 == 5]

def get_count_of_sundays_on_firsts(end: int) -> int:
    firsts = construct_list_of_firsts(end)
    sundays = construct_list_of_sundays(end)
    return len(set(firsts).intersection(sundays))

"""
Program Attempt 2
My first attempt worked. But, in retrospect, it's a bit clunky. I don't think I made any
real gains by my iterate of list of X, iterate list of Y, find union between X and Y 
strategy. It would've been fine to normally iterate. But, more specifically, I should've
broken down the iterations into separate nested loops corresponding to years/months (since
a month always has a first day). Anyways, I could've also just used Python's built-in
libraries for datetime, which I'll do in this implementation. Then, we can just check
the day and weekday properties on the datetime object for each day from 1901 to 2000.
"""

from datetime import datetime
from datetime import timedelta

def get_count_of_sundays_on_firsts2(start_date: datetime, end_date: datetime) -> int:
    num_days = (end_date - start_date).days
    ctr = 0
    for i in range(num_days):
        date_check = start_date + timedelta(days=i)
        if date_check.day == 1 and date_check.weekday() == 6:
            ctr += 1
    return ctr


if __name__ == '__main__':
    from datetime import datetime
    start_date = datetime(1901, 1, 1)
    end_date = datetime(2000, 12, 31)
    num_days = (end_date - start_date).days

    print(get_count_of_sundays_on_firsts(num_days))
    print(get_count_of_sundays_on_firsts2(start_date, end_date))