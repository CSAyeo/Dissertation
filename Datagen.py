import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string
def genRand(pCount, sCount, yCount):
    indexlist = list(string.ascii_uppercase[:pCount])
    df = pd.DataFrame((450 * abs(np.random.randn(pCount, yCount))+ 200), index=indexlist, columns=[x+2015 for x in range(yCount)])
    df= df.round(2)
    print(df.values.tolist())#use sqrt
    setVals(df)

def genTrend(pCount, sCount, yCount):
        a = 0.9
        b = 50
        f = []
        x = list(range(0, yCount))
        for j in range(yCount):
            pos = []
            for k in range (pCount):
                y = []
                for i in range(sCount):
                    print(f"{a=} {i=} {b=} {i**2=}")
                    y.append((a * i + 0.1 ** 2 + b * i + 0.1) * random.random() + 450)
                print(f"{y=}")
                pos.append(y)
            f"{pos=}"
            f.append(pos)
        print(f"{f=}")
        #indexlist = list(string.ascii_uppercase[:pCount])
        #df = pd.DataFrame(pos, index=indexlist, columns=[x + 2015 for x in range(yCount)])
        #print(df.values.tolist())  # use sqrt
        return(f)
        #savevals(df)

def genPos(pCount, sCount, yCount):
    genTrend(pCount,sCount, yCount)

def genNeg(pCount, sCount, yCount):
    genTrend(pCount,sCount, yCount)

def genFlat(pCount, sCount, yCount):
    for j in range(pCount):
        a = 0.9
        b = 50
        neg = []
        x = list(range(0, pCount))
        for j in range(pCount):
            y = []
            for i in range(pCount):
                print(f"{a=} {i=} {b=} {i**2=}")
                y.append((a * i+0.1 ** 2 + b * i+0.1) * random.random()+450)
            print(y)
            neg.append(y)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()
        indexlist = list(string.ascii_uppercase[:pCount])
        df = pd.DataFrame(neg.reverse(),  index=indexlist, columns=[x+2015 for x in range(pCount)])
        print(df.values.tolist())#use sqrt
        setVals(df)

def getVals():
      df = pd.read_csv('file_name.csv')
def setVals(df):
      df.to_csv("Data.csv")
