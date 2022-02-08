# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Datagen import *
from MLP import *
import matplotlib.pyplot as plt
def getInput():
    pC = int(input("How many portfolios to be assessed?"))
    lC = int(input("How many additional layers in the model? (excluding input [0] and output [end])"))
    oC = int(input("How many outputs in the model?"))
    nC = []
    bias = []
    for i in range(lC):
        nC.append(int(input(f"How many neurons in layer {i}")))
        bias.append(int(input(f"Bias for layer {i}")))
    return pC, lC, oC, nC, bias


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

   pCount, lCount, oCount, nCount, biases = getInput()
   Model = MLP(pCount, oCount, nCount, lCount, biases) #inputD, OutputD, RandomMax, Neurons, Layers
   genrand(pCount)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
