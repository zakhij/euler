
'''
Problem Statement:The following iterative sequence is defined for the set of positive integers:
n -> n/2 (if n is even)
n -> 3n+1 (if n is odd)
For instance, using the rule above and starting with 13, we get the sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has 
not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Computational Analysis: Our algorithm operates in linear time: computing the chain for all numbers up to N.
And we ensure that we only compute the chain for each number once: if it's already computed, we rely on constant-time
lookups in the dictionary. The space complexity is O(n) also, as we maintain a dict of all numbers' chains.

DSA: We leverage a dictionary for memoization of the chains, replacing redundant computation with fast lookups. 

Math: No big math principles used here, besides the fact that chains are inherently recursive. 

'''

#Program Attempt 1
#Okay, so obviously the brute-force attempt is do-able here. Iterate from x=1 -> x = 1,000,000 where at each x
#we compute its chain, and check its chain length against the max chain length. This is clearly feasible. Two
#questions that come to mind though - First, can we reduce the space of x's we iterate on? And second, can we
#re-use chain computations? The second should surely be yes. For instance, the chain length for 80 would just be
#the chain length of 40 + 1. But that's a simple example. And not all chains are related, I think. We could try
#to work backwards in building the largest chain. So for instance, we know the chain will end when we hit a
#2^i number. And we know that we hit a 2^i number by doing 3n+1 in reverse (so (2^i - 1) / 3): That number must
#be odd. Hmmm, but can we really do that computation ourselves? Idk. Let's focus on the brute force method first.
#WAIT. Silly me. We should tabularize the results of each number's chain to avoid redundant computation. Like, 
#in the example above with 13, if we already know that 5's chain length is 6, we can stop computation there and just
#do 4 + 6. So as we move up, we keep a dictionary of chain lengths we build upon and can always refer back to.

def get_longest_collatz_under_n(n: int) -> int:
    chains = {}

    for i in range(2,n):
        if i in chains.keys():
            continue

        current_dict = {}
        current = i
        chain_length = 1

        current_dict[current] = chain_length
        while current > 1:

            if current in chains.keys():
                for key in current_dict.keys():
                    current_dict[key] += chains[current]
                break
            else:
                for key in current_dict.keys():
                    current_dict[key] += 1
                if current == 1:
                    break

                current_dict[current] = 1
            
            if current % 2 == 0:
                current //= 2
            else:
                current = (current * 3) + 1
        
        for key in current_dict:
            chains[key] = current_dict[key]
        
    max = 0
    winner = 0
    for key in chains.keys():
        if chains[key] > max:
            winner = key
            max = chains[key]
    
    return winner


#Program Attempt 2
#So Program Attempt 1 does work. And my base concept is sound. But, there is a more elegant way to implement the memoization:
#we can use a better data structure, defaultdict, and we can more elegantly record the chain lengths of the encountered #'s
#by leveraging a list to store the sequence, then, at the end, going through the sequence.

def get_longest_collatz_under_n2(n: int) -> int:
    from collections import defaultdict
    chains = defaultdict()
    chains[1] = 1

    for i in range (2, n):
        sequence = []
        current = i

        while current != 1 and current not in chains:
            sequence.append(current)
            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1
        
        for j, num in enumerate(reversed(sequence)):
            chains[num] = chains[current] + j + 1
    
    max_length = max(chains.values())

    for key in chains:
        if chains[key] == max_length:
            return key
    



    

if __name__ == '__main__':
    ans = get_longest_collatz_under_n2(1000000)
    print(ans)