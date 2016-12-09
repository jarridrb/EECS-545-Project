import numpy as np
import csv

class DataLoad:
    @staticmethod
    def LoadPendigits():
        dataSetDict = {3: [], 8: [], 9: []}
        dataSetList = []
        labels = []
        with open('Digits/pendigits.tes', 'rb') as pendigits:
            loadedDataSet = csv.reader(pendigits)
            for row in loadedDataSet:
                classNum = int(row[16])

                if (classNum == 3 or classNum == 8 or classNum == 9) and np.random.ranf() <= .1:
                    dataSetDict[classNum].append(np.array([int(row[i]) for i in range(16)], dtype=object))

        for classNum, classFeatures in dataSetDict.items():
            for features in classFeatures:
                dataSetList.append(features)
                labels.append(classNum)

        return np.vstack(dataSetList), np.array(labels)
