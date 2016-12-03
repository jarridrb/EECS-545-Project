import numpy as np
import math

class DataGen:
    @staticmethod
    def GenerateCircle(xCenter, yCenter, radius, size, sigma = .1):
        points = np.zeros((size, 2))
        sample = np.random.normal(0, sigma, size)

        for i in range(0, size):
            # Random angle
            theta = 2 * math.pi * np.random.random()

            r = radius + sample[i]
            x = r * math.cos(theta) + xCenter
            y = r * math.sin(theta) + yCenter

            points[i,0] = x
            points[i,1] = y

        return points

    @staticmethod
    def __findPointClass(point, classRanges):
        for i in range(len(classRanges)):
            if point >= classRanges[0] and point < classRanges[1]:
                return i

    @staticmethod
    def GenerateConstraintMatrix(classRanges, numConstraints, numPoints, k):
        weightMatrix = np.zeros((numPoints, numPoints))
        weightVal = numPoints / float(numConstraints * k)

        currNumConstraints = 0
        while currNumConstraints < numConstraints:
            i = np.random.randint(0, numPoints)
            j = np.random.randint(0, numPoints)

            if weightMatrix[i][j] == 0:
                if DataGen.__findPointClass(i, classRanges) != DataGen.__findPointClass(i, classRanges):
                    weightMatrix[i][j] = -weightVal
                    weightMatrix[j][i] = -weightVal
                else:
                    weightMatrix[i][j] = weightVal
                    weightMatrix[j][i] = weightVal

            currNumConstraints += 1

        return weightMatrix


