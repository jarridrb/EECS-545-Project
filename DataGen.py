import numpy as np
import math
from pdb import set_trace as st

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
            if point >= classRanges[i][0] and point < classRanges[i][1]:
                return i

    @staticmethod
    def GenerateConstraintMatrix(classRanges, numConstraints, numPoints, k):
        weightMatrix = np.zeros((numPoints, numPoints))
        if numConstraints == 0:
            return weightMatrix

        weightVal = numPoints / float(numConstraints * k)

        currNumConstraints = 0
        while currNumConstraints < numConstraints:
            i = np.random.randint(0, numPoints)
            j = np.random.randint(0, numPoints)

            if i != j and weightMatrix[i][j] == 0:
                if DataGen.__findPointClass(i, classRanges) != DataGen.__findPointClass(j, classRanges):
                    weightMatrix[i][j] = -weightVal
                    weightMatrix[j][i] = -weightVal
                else:
                    weightMatrix[i][j] = weightVal
                    weightMatrix[j][i] = weightVal

                currNumConstraints += 1

        return weightMatrix

    @staticmethod
    def GenerateTestConstraints():
        constraintMatrix = np.zeros((6,6))
        constraintMatrix[0,1] = 1
        constraintMatrix[1,0] = 1
        constraintMatrix[1,2] = 1
        constraintMatrix[2,1] = 1
        constraintMatrix[3,4] = 1
        constraintMatrix[4,3] = 1
        constraintMatrix[4,5] = 1
        constraintMatrix[5,4] = 1
        constraintMatrix[0,5] = -1

        return constraintMatrix

    @staticmethod
    def TestFFT():
        data = np.zeros((10, 2))
        data[0] = [0,5]
        data[1] = [-1,4]
        data[2] = [1,4]
        data[9] = [0, 4]
        data[3] = [-3,-1]
        data[4] = [-3,-2]
        data[5] = [-1, -8]
        data[6] = [1, -8]
        data[7] = [2, -1]
        data[8] = [2, -2]

        cm = np.zeros((10,10))
        cm[0,1] = 1
        cm[1,2] = 1
        cm[2,9] = 1
        cm[3,4] = 1
        cm[5,6] = 1
        cm[7,8] = 1

        return data, cm

