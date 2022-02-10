import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string
def genrand(pCount):
    indexlist = list(string.ascii_uppercase[:pCount])
    df = pd.DataFrame((450 * abs(np.random.randn(pCount, pCount))+ 200), index=indexlist, columns=[x+2015 for x in range(pCount)])
    df= df.round(2)
    print(df.values.tolist())#use sqrt
    savevals(df)


def genPos(pCount):
    for j in range(pCount):
        a = 0.9
        b = 50
        pos = []
        x = list(range(0, pCount))
        for j in range(pCount):
            y = []
            for i in range(pCount):
                print(f"{a=} {i=} {b=} {i**2=}")
                y.append((a * i+0.1 ** 2 + b * i+0.1) * random.random()+450)
            print(y)
            pos.append(y)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()
        indexlist = list(string.ascii_uppercase[:pCount])
        df = pd.DataFrame(pos,  index=indexlist, columns=[x+2015 for x in range(pCount)])
        print(df.values.tolist())#use sqrt
        savevals(df)

def savevals(df):
      df.to_csv("Data.csv")
