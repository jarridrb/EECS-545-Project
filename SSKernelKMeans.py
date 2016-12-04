from FarthestFirstInitialization import *
import numpy as np
from pdb import set_trace as st

class SSKernelKMeans:
    def __init__(self):
        pass

    def __findSigma(self, k):
        minEigVal = np.amin(np.linalg.eigvals(k))
        if minEigVal < 0:
            return abs(minEigVal)
        else:
            return 0

    def __getMustLinkMatrix(self, weightMatrix):
        n = weightMatrix.shape[0]
        newMatrix = np.zeros(weightMatrix.shape)

        for i in range(n):
            for j in range(n):
                if weightMatrix[i][j] > 0:
                    newMatrix[i][j] = 1

        return newMatrix


    def __formNeighborhoods(self, closure):
        numComponents, componentLabels = csgraph.connected_components(csgraph.csgraph_from_dense(closure), directe=False)

        neighborhoods = {}
        newConstraints = 0
        for i in range(closure.shape[0]):
            if componentLabels[i] in neighborhoods:
                neighborhoods[componentLabels[i]].append(i)
            else:
                neighborhoods[componentLabels[i]] = [i]

        return neighborhoods

    # For both augmentations, if optimizations are needed, many computations are unnecessary
    def __augmentMustLinkConstraints(self, constraintMatrix, neighborhoods):
        for neighborhoodNum, neighborhoodMembers in neighborhoods.items():
            for i in neighborhoodMembers:
                for j in neighborhoodMembers:
                    if constraintMatrix[i][j] == 0:
                        constraintMatrix[i][j] = 1
                        constraintMatrix[j][i] = 1

        return constraintMatrix

    def __augmentCannotLinkConstraint(self, constraintMatrix, neighborhoods):
        for neighborhoodNumI, neighborhoodMembersI in neighborhoods.items():
            for neighborhoodNumJ, neighborhoodMembersJ in neighborhoods.items():
                if neighborhoodNumI != neighborhoodNumJ:
                    for i in neighborhoodMembersI:
                        for j in neighborhoodMembersJ:
                            constraintMatrix[i][j] = -1
                            constraintMatrix[j][i] = -1

        return constraintMatrix

    def __reweightConstraintMatrix(self, constraintMatrix, k):
        alreadySeen = {}
        numConstraints = 0

        for i in range(constraintMatrix.shape[0]):
            for j in range(constraintMatrix.shape[0]):
                if not ((i, j) in alreadySeen or (j, i) in alreadySeen):
                    alreadySeen[(i, j)] = True
                    alreadySeen[(j, i)] = True

                    numConstraints += 1

        # Ensure float division
        weightVal = constraintMatrix.shape[0] / float(k * numConstraints)

        for i in range(constraintMatrix.shape[0]):
            for j in range(constraintMatrix.shape[0]):
                if constraintMatrix[i][j] > 0:
                    constraintMatrix[i][j] = weightVal
                elif constraintMatrix[i][j] < 0:
                    constraintMatrix[i][j] = -weightVal

        return constraintMatrix

    def __augmentConstraintMatrix(self, constraintMatrix, neighborhoods, k):
        constraintMatrix = self.__augmentMustLinkConstraints(constraintMatrix, neighborhoods)
        constraintMatrix = self.__augmentCannotLinkConstraints(constraintMatrix, neighborhoods)
        constraintMatrix = self.__reweightConstraintMatrix(constraintMatrix, k)

        return constraintMatrix

    def Cluster(self, similarityMatrix, constraintMatrix, k, maxIt = 100):
        transClosure = Graph.TransitiveClosure(self.__getMustLinkMatrix(constraintMatrix))
        neighborhoods = self.__formNeighborhoods(transClosure)
        constraintMatrix = self.__augmentConstraintMatrix(constraintMatrix, neighborhoods, k)

        initKMatrix = similarityMatrix.raw() + weightMatrix
        # If things are faulty, check here. Min eigval != 0 after diagonal shift right now.
        kMatrix = (self.__findSigma(initKMatrix) * np.identity(initKMatrix.shape[0])) + initKMatrix

        initializationAgent = FarthestFirstInitialization()
        initialClusters = initializationAgent.InitializeClusters(similarityMatrix, weightMatrix, k)

        return KernelKMeans.Cluster(kMatrix, k, np.ones(kMatrix.shape[0]), initialClusters)

