import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string
def genrand(pCount):
    indexlist = list(string.ascii_uppercase[:pCount])
    df = pd.DataFrame((450 * abs(np.random.randn(pCount, pCount))+ 200), index=indexlist, columns=[x+2015 for x in range(pCount)])
    df= df.round(2)
    print(df.values.tolist())
    df.to_csv("Data.csv")


def genPos(pCount):
    for j in range(pCount):
        a = 0.05
        b = 10
        y = []
        x = list(range(0, 15))
        for i in range(15):
            y.append(a * i ** 2 + b * i * random.random())
        print(y)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()