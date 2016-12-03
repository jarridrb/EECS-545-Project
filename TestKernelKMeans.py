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

data = np.zeros((400, 2))
nmiVals = np.zeros((100))
for j in range(0, 100):
    data[0:200, :] = DataGen.GenerateCircle(.5, .5, 2, 200)
    data[200:400, :] = DataGen.GenerateCircle(.5, .5, 5, 200)
    constraintMatrix = DataGen.GenerateConstraintMatrix([(0, 200), (200, 400)], 50, 400, 2)
    similarityMatrix = KernelMatrix(data, 1, .5)
    SSKernelKMeans.Cluster(similarityMatrix, constraintMatrix, 2)

    kMeansAgent = KernelKMeans("rbf", .5)
    clusterAssignments = kMeansAgent.cluster(data, 2, 100)
    trueAssignments = [0 if i < 200 else 1 for i in range(0, 400)]

    nmiVals[j] = sklearn.metrics.normalized_mutual_info_score(trueAssignments, clusterAssignments)

print('NMI = ' + str(np.average(nmiVals)))
