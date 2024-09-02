
'''
Problem Statement:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand 
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for 
each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
What is the total of all the name scores in the file?

Computational Analysis: Funnily enough, the sort operation dominates the actual calculation.
The sort operation is O(n log n) and the calculation is O(n). Space complexity is O(n).

DSA: We use Python's built-in sort function which is O(n log n), and we leverage the Python list
data structure for storing the names and processing each. We also use a dict for fast lookups
of the "value" of each letter. 

Math: No math concepts used here. 

'''

'''
Program Attempt 1:
This problem is relatively simple in terms of solution design, there's not much wiggle room. The simplest,
brute-force implementation is to transform the data file into a Python list, sort the list, then iterate
over each name in the list, calculating each name score independently. There MIGHT be slight optimizations
regarding caching alphabetical position values (e.g., CHRISTINE is just CHRISTINA -A +E.), but the gains
are marginal. Let's focus on the brute-force implementation.
'''
abc_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}


def name_score_calc(name: str, index: int) -> int:
    score = 0
    for l in name:
        score += abc_dict[l]
    return score * index

def name_scorer(name_data: str) -> int:
    names = name_data.replace('"', '').split(',')
    names.sort()

    total_score = 0
    
    for i, name in enumerate(names):
        total_score += name_score_calc(name, i+1)
    
    return total_score

if __name__ == '__main__':
    with open('0022_names.txt', 'r') as f:
        names = f.read()
        ans = name_scorer(names)
        print(ans)