from GenCircularData import *
import numpy as np
import matplotlib.pyplot as plt
from pdb import set_trace as st
import sys
sys.path.insert(0, '/home/jrectorb/eecs/545/EECS-545-Project/KernelKMeans')
from KernelKMeans import *

if __name__ == "__main__":
    data = np.zeros((200, 2))
    data[0:100, :] = CircularDataGen.GenerateCircle(0, 0, 2, 100)
    data[100:200, :] = CircularDataGen.GenerateCircle(0, 0, 5, 100)

    st()
    kMeansAgent = KernelKMeans("gaussian", 1)
    clusterAssignments = kMeansAgent.cluster(data, 2, 100)

    plt.scatter(data[:,0], data[:,1], clusterAssignments)
    plt.show()
