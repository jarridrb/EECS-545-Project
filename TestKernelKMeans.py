from DataGen import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pdb import set_trace as st
import sklearn.metrics
import sys
sys.path.insert(0, '/home/jrectorb/eecs/545/EECS-545-Project/KernelKMeans')
#sys.path.insert(0, '/Users/Emily/School/eecs/545/Project/EECS-545-Project/KernelKMeans')
from KernelKMeans import *
from SSKernelKMeans import *

def Test(dataSize, paramVal, constraintStep):
    data = np.zeros((dataSize, 2))
    nmiVals = np.zeros((11))
    trueAssignments = [0 if i < (dataSize / 2) else 1 for i in range(dataSize)]
    numConstraints = np.zeros((11))
    data[0:dataSize / 2, :] = DataGen.GenerateCircle(.5, .5, 2, dataSize / 2)
    data[dataSize / 2:dataSize, :] = DataGen.GenerateCircle(.5, .5, 5, dataSize / 2)
    similarityMatrix = KernelMatrix(data, 1, .5)
    for j in range(11):
        constraintMatrix = DataGen.GenerateConstraintMatrix([(0, dataSize / 2), (dataSize / 2, dataSize)], j * constraintStep, dataSize, 2)
        ssKernelKMeansAgent = SSKernelKMeans()
        clusterAssignments = ssKernelKMeansAgent.Cluster(similarityMatrix, constraintMatrix, 2)

        nmiVals[j] = sklearn.metrics.normalized_mutual_info_score(trueAssignments, clusterAssignments)
        numConstraints[j] = j * constraintStep
        print('NMI with ' + str(numConstraints[j]) + ' constraints = ' + str(nmiVals[j]))

    plt.scatter(data[:,0], data[:,1], c=clusterAssignments, cmap=cm.Set1)
    plt.show()
#plt.plot(numConstraints, nmiVals)
    print('NMI = ' + str(np.average(nmiVals)))

Test(30, .5, 10)
