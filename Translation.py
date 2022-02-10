import math
import numpy as np


class MLP:

    def __init__(self, pCount, sectors, oCount, nCount, lCount, biases):
        self.inputD = pCount
        self.sectors = sectors
        self.outputD = oCount
        self.layers = lCount
        self.bias = biases
        self.LayerWeight = self.randWeights(pCount, oCount, lCount, nCount)

    def randWeights(self, pCount, oCount, lCount, nCount):
        Weights = []
        Weights.append(np.random.randn(pCount + 1, nCount[0]))
        for x in range(lCount - 1):
            Weights.append(np.random.randn((nCount[x] + 1), nCount[x + 1]))
        Weights.append(np.random.randn(nCount[-1], oCount))
        print(f"{Weights=}")
        return (Weights)

    Sig = lambda x: 1 / (1 + math.exp(-x))

    def cfa(self, data):
        print(data)
        layer = []
        curLayer = 0
        for x in range(self.layers):
            temp = data.append(self.bias[curLayer])
