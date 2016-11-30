from KernelMatrix import KernelMatrix
from Cluster import Cluster
from PointSums import PoinSums
import numpy as np

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
        clusters = [Cluster(gramMatrix) for i in range(0, k)]

        for i in range(0, n):
            clusters[np.random.randint(0, k)].addPoint(i)

        return clusters

    def __initClusterMap(self, clusters):
        clusterMap = {}

        for i in range(0, k):
            for assignment in cluster[i].clusterPoints:
                clusterMap[assignment] = i

        return clusterMap

    def __converged(self, clusterMap):
        if clusterMap != self.lastClusterMap:
            self.lastClusterMap = clusterMap
            return True
        else:
            return False

    def __iterate(self, gramMatrix, clusterMap, clusters, pointSums, n, maxIter):
        t = 0
        distCalcAgent = DistanceCalc(gramMatrix)
        
        while (not __converged(clusterMap)) and t < maxIter:
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

        clusterAssignments = [clusterMap[i] for i in range(0, n)]
        return clusterAssignments

    def cluster(self, data, k, maxIter, clusters = None):
        self.lastClusterMap = None
        gramMatrix = KernelMatrix(data, self.kernelType, self.paramVal)
        if clusters == None:
            clusters = __initClusters(k)

        clusterMap = __initClusterMap(clusters)
        pointSums = PointSums(gramMatrix, clusters, data.shape[0])

        return __iterate(gramMatrix, clusterMap, clusters, pointSums, maxIter)


         

