from Graph import Graph
import numpy as np

class FarthestFirstInitialization:
    def __init__(self):
        pass

    def InitializeClusters(self, similarityMatrix, weightMatrix, k):
        mustLinkMatrix = self.__getMustLinkMatrix(weightMatrix)
        mustLinkConnectedComponents = Graph.ConnectedComponents(mustLinkMatrix)


