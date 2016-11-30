class Cluster:
    def __init__(self, pointsInCluster, kernelMatrix):
        self.clusterPoints = pointsInCluster
        self.kernelMatrix = kernelMatrix

        self.sum = 0

        for i in self.clusterPoints:
            for j in self.clusterPoints:
                self.sum += kernelMatrix[i,j]         

    def addPoint(self, idx):
        self.clusterPoints.append(idx)

        for i in self.clusterPoints:
            self.sum += kernelMatrix[idx, i]

    def removePoint(self, idx):
        for i in self.clusterPoints:
            self.sum -= kernelMatrix[idx, i]

        self.clusterPoints.remove(idx)

    def secondTermVal(self):
        return self.sum / (len(self.clusterPoints) ** 2)
        
    def size(self):
        return len(self.clusterPoints)
