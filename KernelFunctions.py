import numpy as np

class KernelFunctions:
    def Polynomial(x, y, d):
        return np.dot(x, y) ** d

    def Gaussian(x, y, sigma):
        return np.exp(-1 * (np.linalg.norm(x - y) ** 2) / (2 * (sigma ** 2)))

    def InverseMultiquadratic(x, y, c):
        return 1 / (np.linalg.norm(x - y) ** 2 + c) ** .5

    def __init__(self):
        self.Polynomial = Polynomial
        self.Gaussian = Gaussian
        self.InverseMultiquadratic = InverseMultiquadratic

