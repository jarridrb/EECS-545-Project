from KernelMatrix import KernelMatrix
from Cluster import Cluster
from PointSums import PointSums
from DistanceCalc import DistanceCalc
from pdb import set_trace as st
import numpy as np
import copy

class KernelKMeans:
    def __init__(self, kernelType, paramVal):
        if kernelType == "polynomial":
            self.kernelType = 0
        elif kernelType == "rbf":
            self.kernelType = 1
        else:
            self.kernelType = 2

        self.paramVal = paramVal

    def __initClusters(self, k, n):
        clusters = [Cluster(self.gramMatrix) for i in range(0, k)]

        for i in range(0, n):
            clusters[np.random.randint(0, k)].addPoint(i)

        return clusters

    def __initClusterMap(self, clusters):
        clusterMap = {}

        for i in range(0, len(clusters)):
            for assignment in clusters[i].clusterPoints:
                clusterMap[assignment] = i

        return clusterMap

    def __converged(self, clusterMap):
        if clusterMap != self.lastClusterMap:
            self.lastClusterMap = copy.deepcopy(clusterMap)
            return False
        else:
            return True

    def __iterate(self, clusterMap, clusters, pointSums, n, maxIter):
        t = 0
        distCalcAgent = DistanceCalc(self.gramMatrix)

        while (not self.__converged(clusterMap)) and t < maxIter:
            clusterAssignmentChanges = []
            # Determine whether any assignments change
            for i in range(0, n):
                newAssignment = distCalcAgent.minDist(i, clusters, pointSums)
                if newAssignment != clusterMap[i]:
                    clusterAssignmentChanges.append((i, clusterMap[i]))
                    clusterMap[i] = newAssignment

            for dataPointIdx, oldCluster in clusterAssignmentChanges:
                clusters[oldCluster].removePoint(dataPointIdx)
                clusters[clusterMap[dataPointIdx]].addPoint(dataPointIdx)
                pointSums.changeClusterAssignment(dataPointIdx, oldCluster, clusterMap[dataPointIdx])

            t += 1

        print(t)
        clusterAssignments = [clusterMap[i] for i in range(0, n)]
        return clusterAssignments

    def cluster(self, data, k, maxIter, clusters = None):
        self.lastClusterMap = None
        self.gramMatrix = KernelMatrix(data, self.kernelType, self.paramVal)
        if clusters == None:
            clusters = self.__initClusters(k, data.shape[0])

        clusterMap = self.__initClusterMap(clusters)
        pointSums = PointSums(self.gramMatrix, clusters, data.shape[0])

        return self.__iterate(clusterMap, clusters, pointSums, data.shape[0], maxIter)
