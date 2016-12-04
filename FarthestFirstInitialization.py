from Graph import Graph
import numpy as np

class FarthestFirstInitialization:
    def __init__(self, similarityMatrix):
        self.similarityMatrix = similarityMatrix

    def __distFromSelectedCluster(self, selectedClusters, candidateCluster):
        distance = 0

        for selectedCluster in selectedClusters:
            firstTerm = selectedCluster.thirdTermVal()

            secondTerm = 0
            for i in selectedCluster.clusterPoints:
                for j in candidateCluster.clusterPoints:
                    secondTerm += self.similarityMatrix[i][j]
            secondTerm = (-2 * secondTerm) / (selectedCluster.size() * candidateCluster.size())

            thirdTerm = candidateCluster.thirdTermVal()
            distance += firstTerm + secondTerm + thirdTerm

        return distance


    def __farthestCluster(self, selectedClusters, candidateClusters):
        farthestCluster = -1
        farthestDist = -1

        for i in range(len(candidateClusters)):
            thisDist = 0
            for selectedCluster in selectedClusters:
                thisDist += self.__distFromSelectedCluster(selectedCluster, candidateCluster)

            if farthestDist == -1 or thisDist > farthestDist:
                farthestDist = thisDist
                farthestCluster = i

        return farthestCluster

    def InitializeClusters(self, neighborhoods, k):
        candidateClusters = [Cluster(similarityMatrix) for i in range(neihborhoods.keys())]
        bestSize = -1
        largestCluster = -1

        for neigborhoodNum, neighborhoodMembers:
            for i in neighborhoodMembers:
                candidateClusters[neighborhoodNum].addPoint(i)

            if bestSize == -1 or candidateClusters[neighborhoodNum].size() < bestSize:
                bestSize = candidateClusters[neighborhoodNum].size()
                largestCluster = neighborhoodNum

        # Clean this up
        if k == len(initialClusters):
            return candidateClusters

        selectedClusters = [candidateClusters[largestCluster]]
        candidateClusters.pop(largestCluster)

        while len(initialClusters) < k:
            farthestCluster = self.__farthestCluster(selectedClusters, candidateClusters)
            selectedClusters.append(candidateClusters[farthestCluster])
            candidateClusters.pop(farthestCluster)

        return selectedClusters


