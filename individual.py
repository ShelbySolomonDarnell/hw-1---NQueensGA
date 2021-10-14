"""
Name: Professor S
Description: A representation of an N-queen solution.
"""
import random
import base

class Individual:
    def __init__(self, size, representation=None):
        self.size = size
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.representation = []
        if representation == None:
            self.create()
        else:
            self.representation = representation
        self.fitness = base.calculateFitness(self)
    
    def create(self):
        for ndx in range(self.size):
            self.representation.append(random.randint(1,self.size))

    def getFitness(self):
        return self.fitness
    
    def getSize(self):
        return self.size

    def rep(self, ndx):
        res = -1
        if ndx > -1 and ndx < self.size:
            res = self.representation[ndx]
        return res

    """
    Description: Use a random number generator to change the value of a single 
        value in the individual to remove stale individuals.
    Parameters: none
    Return: nothing
    """
    def mutate(self):
        ndx = random.randint(0, self.size-1)
        newValue = random.randint(1, self.size)
        while ( newValue == self.representation[ndx] ):
            newValue = random.randint(1, self.size)
        self.representation[ndx] = newValue
        self.fitness = base.calculateFitness(self)
        
    def __str__(self):
        res = "\n\t[Individual] rep: "
        ndx = 0
        for val in self.representation:
            if ndx>0:
                res += ", "
            res += f"{self.letters[ndx].upper()}{val}"
            ndx+=1
        res += f" --> fit:{self.fitness}"
        return res
        





