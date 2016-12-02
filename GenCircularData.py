import numpy as np
import math

class CircularDataGen:
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

