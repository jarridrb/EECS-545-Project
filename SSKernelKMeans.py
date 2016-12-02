class SSKernelKMeans:
    def __findSigma(self, k):
        minEigVal = np.amin(np.linalg.eigvals(k))
        if minEigVal < 0:
            return abs(minEigVal)
        else:
            return 0

    @staticmethod
    def Cluster(similarityMatrix, weightMatrix, k, maxIt = 100):
        initKMatrix = similarityMatrix + weightMatrix
        kMatrix = (self.__findSigma(initKMatrix) * np.identity(initKMatrix.shape[0])) + initKMatrix

        initializationAgent = FarthestFirstInitialization()
        initialClusters = initializationAgent(InitializeClusters)

        return KernelKMeans.Cluster(kMatrix, k, np.ones(kMatrix.shape[0]), initialClusters)
