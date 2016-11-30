class Cluster:
    def __init__(self, kernelMatrix, pointsInCluster = None):
        self.clusterPoints = pointsInCluster if pointsInCluster != None else []
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

    def thirdTermVal(self):
        return self.sum / (len(self.clusterPoints) ** 2)
        
    def size(self):
        return len(self.clusterPoints)

    def center(self):
        return self.sum / float(len(self.clusterPoints))
