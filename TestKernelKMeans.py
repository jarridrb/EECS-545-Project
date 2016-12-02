from GenCircularData import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pdb import set_trace as st
import sys
sys.path.insert(0, '/home/jrectorb/eecs/545/EECS-545-Project/KernelKMeans')
from KernelKMeans import *

if __name__ == "__main__":
    data = np.zeros((200, 2))
    data[0:100, :] = CircularDataGen.GenerateCircle(0, 0, 2, 600)
    data[100:200, :] = CircularDataGen.GenerateCircle(0, 0, 5, 600)

    kMeansAgent = KernelKMeans("rbf", 1.15)
    clusterAssignments = kMeansAgent.cluster(data, 2, 100)

    plt.scatter(data[:,0], data[:,1], c=clusterAssignments, cmap=cm.Set1)
    plt.show()
