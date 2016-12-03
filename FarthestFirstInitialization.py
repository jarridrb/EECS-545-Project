from Graph import Graph
import numpy as np

class FarthestFirstInitialization:
    def __init__(self):
        pass

    def __farthestCluster(self, selectedClusters, candidateClusters):
        farthestCluster = -1
        farthestDist = -1

        for candidateCluster in candidateClusters:
            thisDist = 0
            for selectedCluster in selectedClusters:
                thisDist +=

    def InitializeClusters(self, similarityMatrix, neighborhoods, k):
        candidateClusters = [Cluster(similarityMatrix) for i in range(neihborhoods.keys())]
        bestSize = -1
        largestCluster = -1

        for neigborhoodNum, neighborhoodMembers:
            for i in neighborhoodMembers:
                candidateClusters[neighborhoodNum].addPoint(i)

            if bestSize == -1 or candidateClusters[neighborhoodNum].size() < bestSize:
                bestSize = candidateClusters[neighborhoodNum].size()
                largestCluster = neighborhoodNum

        selectedClusters = candidateClusters[largestCluster]
        candidateClusters.pop(largestCluster)

        while len(initialClusters) < k:
            farthestCluster = self.__farthestCluster(selectedClusters, candidateClusters)
            selectedClusters = candidateClusters[farthestCluster]
            candidateClusters.pop(farthestCluster)


