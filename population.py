"""
Population for the Genetic algorithm
"""
import random
import base
import individual
from individual import Individual

class Population:
    def __init__(self, size, representationSize):
        self.size = size
        self.representationSize = representationSize
        self.reps = []
        for ndx in range(size):
            self.reps.append(Individual(representationSize))

    def crossOver(self):
        dadNdx = random.randint(0,self.size-1)
        momNdx = random.randint(0,self.size-1)
        while ( momNdx == dadNdx ):
            momNdx = random.randint(0,self.size-1)
        splitPoint = random.randint(0,self.representationSize-1)

        dad = self.reps[dadNdx]
        mom = self.reps[momNdx]
        childRep = []
        for ndx in range(self.representationSize):
            if ndx < splitPoint:
                childRep.append(dad.rep(ndx))
            else:
                childRep.append(mom.rep(ndx))
        return Individual(self.representationSize, childRep)
    
    def findWeakest(self):
        leastFit = None
        for member in self.reps:
            if leastFit == None:
                leastFit = member
            if member.getFitness() > leastFit.getFitness():
                leastFit = member 
        return leastFit
    
    def findMostFit(self):
        mostFit = None
        for member in self.reps:
            if mostFit == None:
                mostFit = member
            if member.getFitness() < mostFit.getFitness():
                mostFit = member 
        return mostFit

    def getIndividual(self, ndx):
        return self.reps[ndx] 

    def replaceWeakest(self, child):
        #del self.reps[self.findWeakest()]
        self.reps.remove(self.findWeakest())
        self.reps.append(child)

    def __str__(self):
        res = "[Proposed Solutions]"
        for member in self.reps:
            res += f"\t{member}"
        return res
