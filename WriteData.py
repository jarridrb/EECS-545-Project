import csv
import numpy as np

class DataWrite:
    @staticmethod
    def WriteLabels(labels):
        with open('labels.data', 'w') as labelsFile:
            labelWriter = csv.writer(labelsFile)

            labelWriter.writerow(labels)

    @staticmethod
    def WriteData(data):
        with open('points.data', 'w') as pointsFile:
            pointsWriter = csv.writer(pointsFile)

            for i in range(data.shape[0]):
                pointsWriter.writerow(data[i,:])

    @staticmethod
    def ReadLabels():
        with open('labels.data', 'r') as labelsFile:
            labelReader = csv.reader(labelsFile)

            for row in labelReader:
                return [int(i) for i in row]

    #@staticmethod
    #def ReadPoints():
    #    points = np.zeros((200,2))
    #    with open('points.data', 'r') as pointsFile:
    #        pointsReader = csv.reader(pointsFile)

    #        for row in pointsReader:
    #
