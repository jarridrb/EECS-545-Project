from Graph import Graph
import numpy as np

class FarthestFirstInitialization:
    def __init__(self):
        pass

    def __getMustLinkMatrix(self, weightMatrix):
        n = weightMatrix.shape[0]
        newMatrix = np.zeros(weightMatrix.shape)

        for i in range(n):
            for j in range(n):
                if weightMatrix[i][j] > 0:
                    newMatrix[i][j] = 1

        return newMatrix

    def InitializeClusters(self, similarityMatrix, weightMatrix, k):
        mustLinkMatrix = self.__getMustLinkMatrix(weightMatrix)
        mustLinkConnectedComponents = Graph.ConnectedComponents(mustLinkMatrix)


