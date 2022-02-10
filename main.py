# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Datagen import *
from MLP import *
import matplotlib.pyplot as plt

def validIntInput(data, acc):

    res = not (data in list(range(1,acc)))
    return(res)

def getModel(pC, yC, sC):
    lC = int(input("How many additional layers in the model? (excluding input [0] and output [end])\n"))
    oC = int(input("How many outputs in the model?\n"))
    genData(pC, sC, yC)
    nC = []
    bias = []
    for i in range(lC):
        nC.append(int(input(f"How many neurons in layer {i}\n")))
        bias.append(int(input(f"Bias for layer {i}\n")))
    return pC, sC, yC, lC, oC, nC, bias

def genData(pCount, sCount, yCount):
    dData = int(input("Do you want to \n 1) reuse old data \n 2) generate new data\n"))
    match dData:
        case 1:
            getVals()
        case 2:
            dGen = int(input("Do you want to: \n 1) generate new flat data \n 2) generate new positive data \n 3) generate new negative data \n 4) generate new random data\n"))
            match dGen:
                case 1:
                    genFlat(pCount, sCount, yCount)
                case 2:
                    genPos(pCount, sCount, yCount)
                case 3:
                    genNeg(pCount, sCount, yCount)
                case 4:
                    genRand(pCount, sCount, yCount)
def getInput():

    pC = int(input("How many portfolios to be assessed?:\n"))
    sC = int(input("How many sectors in each portfolio?\n"))
    yC = int(input("How many years to be assessed?\n"))
    dModel=0
    while validIntInput(dModel, 3):
        dModel=int(input("Do you want to generate a new model \n 1) Yes, generate model with new parameters \n 2) No, re-use old data\n"))
    match dModel:
        case 1:
            getModel(pC, yC, sC)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

   pCount, sCount, yCount, lCount, oCount, nCount, biases = getInput()
   Model = MLP(pCount, sCount, yCount, oCount, nCount, lCount, biases) #inputD, OutputD, RandomMax, Neurons, Layers




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
