
'''
Problem Statement: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2. For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

Computational Analysis: Using the parametrization method in Attempt 2, we get O(sqrt(N)). We have only 1 loop,
iterating over m, that increases at a rate of sqrt(N), and there's constant work done inside of the loop.

DSA: Nothing special: just basic control structures such as loops and conditional checks, integers, and basic
arithmetic operations.

Math: We leverage several mathematical principles surrounding Pythagorean triplets, the first and most obvious
being the triplet equation (a^2 + b^2 = c^2). In Attempt 2, we leverage more advanced math relations, such as
the Euclidean method to parameterize primitive Pythagorean triplets using two integers m and n where m > n > 0 
and gcd(m, n) = 1. Primitive Pythagorean triplets can be considered as 'base' triplets. All Pythagorean triplets 
can be expressed by scaling the values of a, b, and c of a given primitive triplet by some constant k.
'''

#Program Attempt 1
#My first thought is to iteratively look at Pythagorean triplets, then go up and up until we hit a + b + c = 1000.
#But then the question becomes, how do we iteratively look at Pythagorean triplets? I'd need to create that list
#myself. Would it be iterating over a, b, and c and checking if a^2 + b^2 = c^2? So like, check within the spaces
#of a < 1000, b < 1000, c < 1000 (1000 is just a starter number, it can probably be optimized further) for every
#single combination of those 3 variables, then a) check if it satisfies the Pythagorean equation and b) check if 
#they add up to 1000. Wait a minute... why would I not first check if they add up to 1000? Also, I can use that
#constraint, that a + b + c = 1000, as the starting point, since it's probably a smaller space to search through.
#I can add logic to trim the search space, like that c must be greater than a and b. So I'll need to use nested
#loops, for sure. The outermost loop will be c going from 0 (could this be 500?) to 1000. Then, for each candidate c,
#we explore the 2D candidate [a, b] solution space, which will require another nested loop for a and for b.

def triplet_iterator(goal: int) -> int:
    for c in range(goal):
        for a in range(c):
            for b in range(c):
                if a + b + c == goal:
                    if a**2 + b**2 == c**2:
                        return a*b*c

            
#Program Attempt 2
#So the first program attempt did work, yay! However, it's heavily brute-forced: the runtime complexity is O(N^3)
#because we search over the entire 3D space between a, b, and c. Now, I could alter the loop ranges to practically
#reduce the search space, but at the end of the day, it's a brute-force search over the 3D space. We instead can
#utilize a completely new paradigm, leveraging mathematical properties of Pythagorean triplets. Namely, 
#Euclid's method for representing primitive Pythagorean triplets using m and n (where gcd(m,n) = 1). Reframing the
#problem in terms of 2 variables instead of 1 and making us of its mathematical relations allows us to reduce
#the search space dramatically. 

def find_triplet(goal: int) -> int:
    for m in range(2, int((goal // 2) ** 0.5) + 1):
        if (goal // 2) % m == 0:
            n = int(((goal // 2) / m ) - m)
            if m > n > 0:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if a + b + c == goal:
                    return a*b*c
    return




if __name__ == '__main__':
    goal = 1000
    ans = find_triplet(goal)
    print(ans)