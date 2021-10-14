"""
Base.py contains helper functions for the Genetic Algorithm. 
"""
from itertools import permutations

import individual
from individual import Individual

def calculateHorizontalConflicts(ndv):
    cntr = 0
    for j in range(ndv.getSize()):
        for i in range(j+1,ndv.getSize()):
            if ( ndv.rep(j) == ndv.rep(i) ) :
                cntr+=1
    return cntr

def calculateDiagonalConflicts(ndv):
    cntr = 0
    for j in range(ndv.getSize()):
        ndx = 1 
        for i in range(j+1,ndv.getSize()):
            #check for upward diagonal conflict
            if ( ndv.rep(j)+ndx == ndv.rep(i) ):
                cntr+=1
            #check for downward diagonal conflict
            if ( ndv.rep(j)-ndx == ndv.rep(i) ):
                cntr+=1
            ndx+=1
    return cntr



def calculateFitness(individual):
    horizontalConflicts = calculateHorizontalConflicts(individual)
    diagonalConflicts   = calculateDiagonalConflicts(individual)
    return horizontalConflicts + diagonalConflicts

def count_iterable(i):
    return sum(1 for e in i)

repSize = 5
vert = range(repSize)
muts = permutations(vert)
print(f"There are {count_iterable(muts)} permutations for an integer list of length 5")


"""
# Test the functions
for ndx in range(20):
    solution = Individual(9)
    print(f"\t{solution}")
    conflicts = calculateFitness(solution)
    print(f"\tSolution {ndx+1}\tConflicts {conflicts}")
"""

