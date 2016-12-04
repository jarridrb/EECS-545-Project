from pdb import set_trace as st
import scipy.sparse.csgraph as csgraph
import numpy as np

class Graph:
    @staticmethod
    def TransitiveClosure(adjMatrix):
        n = len(adjMatrix)

        newMatrix = np.zeros(adjMatrix.shape)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    newMatrix[i][j] = adjMatrix[i][j] or (adjMatrix[i][k] and adjMatrix[k][j])

        return newMatrix

