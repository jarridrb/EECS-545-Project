from Graph import Graph
import numpy as np
import sys
sys.path.insert(0, '/home/jrectorb/eecs/545/EECS-545-Project/KernelKMeans')
from Cluster import *
from pdb import set_trace as st

class FarthestFirstInitialization:
    def __init__(self, similarityMatrix):
        self.similarityMatrix = similarityMatrix

    def __distFromSelectedCluster(self, selectedCluster, candidateCluster):
        firstTerm = selectedCluster.thirdTermVal()

        secondTerm = 0
        for i in selectedCluster.clusterPoints:
            for j in candidateCluster.clusterPoints:
                secondTerm += self.similarityMatrix[i][j]
        secondTerm = (-2 * secondTerm) / (selectedCluster.size() * candidateCluster.size())

        thirdTerm = candidateCluster.thirdTermVal()
        distance = firstTerm + secondTerm + thirdTerm

        return distance


    def __farthestCluster(self, selectedClusters, candidateClusters):
        farthestCluster = -1
        farthestDist = -1

        for i in range(len(candidateClusters)):
            thisDist = 0
            for selectedCluster in selectedClusters:
                thisDist += self.__distFromSelectedCluster(selectedCluster, candidateClusters[i])

            if farthestDist == -1 or thisDist > farthestDist:
                farthestDist = thisDist
                farthestCluster = i

        return farthestCluster

    def InitializeClusters(self, neighborhoods, k):
        candidateClusters = [Cluster(self.similarityMatrix) for i in range(len(neighborhoods.keys()))]
        bestSize = -1
        largestCluster = -1

        # Need case if len(candidateClusters) < k
        if k == len(candidateClusters):
            selectedClusters = candidateClusters

        else:
            for neighborhoodNum, neighborhoodMembers in neighborhoods.items():
                for i in neighborhoodMembers:
                    candidateClusters[neighborhoodNum].addPoint(i)

                if bestSize == -1 or candidateClusters[neighborhoodNum].size() > bestSize:
                    bestSize = candidateClusters[neighborhoodNum].size()
                    largestCluster = neighborhoodNum

            selectedClusters = [candidateClusters[largestCluster]]
            candidateClusters.pop(largestCluster)

            while len(selectedClusters) < k:
                farthestCluster = self.__farthestCluster(selectedClusters, candidateClusters)
                selectedClusters.append(candidateClusters[farthestCluster])
                candidateClusters.pop(farthestCluster)

        return selectedClusters


