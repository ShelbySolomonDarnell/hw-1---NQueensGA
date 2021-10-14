"""
Name: Professor S
Description: An improvement on a stochastic hillclimber/search that
    uses sexual reproduction and mutation to steadily improve a 
    solution.
"""
import random
import base
from population import Population
from individual import Individual


thePop = Population(40, 4)
print(thePop)

mostFit = thePop.findMostFit()
lestFit = thePop.findWeakest()
print(f"Most fit {mostFit}\nLeast fit {lestFit}")

ndx = 1 
while mostFit.getFitness() > 0:
    child = thePop.crossOver()
    if ( random.randint(1,10) < 4 ):
        child.mutate()
    thePop.replaceWeakest(child)
    mostFit = thePop.findMostFit()
    print(f"[Generation {ndx}] {mostFit}")
    ndx+=1