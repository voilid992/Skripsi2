import pandas as pd
import numpy as np
from math import exp
import random



class Function:
    def inputWeight(reqLayer, reqVar):
        weight = []
        if reqVar == 0:
            for i in range(reqLayer+1):
                tempWeight = random.random()
                weight.append(tempWeight)
        else:
            for i in range(reqLayer):
                tmpWeight=[]
                for j in range(reqVar+1):
                    tempWeight = random.random()
                    tmpWeight.append(tempWeight)
                weight.append(tmpWeight)
        return weight
    
    def activation(weightValue: np.float64,inputValue: np.float64):
        value = float(64)
        value = weightValue*inputValue
        return value
    
    def errorValue(inputScale: np.float64, output: np.float64):
    # value = pow((inputScale-output),2)
        return pow((inputScale-output),2)
    
    def outputValue(output: np.float64,inputScale: np.float64):
        value=(inputScale-output)*output*(1-output)
        return value
    
    def deltaValue(reqLrate: np.float64,reqDelta: np.float64,reqHiddenValue: np.float64):
    # value=0.0
        value=reqLrate*reqDelta*reqHiddenValue
        return value
    
    def deltaNet(reqDelta0: np.float64,reqValue: np.float64):
        value=0.0
        value=reqDelta0*reqValue
        return value
    
    def transferActivation(activationValue: np.float64):
        transferValue=float(64)
        transferValue = 1.0/(1.0+pow(exp(1),(activationValue*-1)))
        return transferValue
    
    def chooseColumn(reqCol,reqDataset,index,reqColScale):
        tempInput =[1.0]
        tmpScale =0.0
        for col in reqCol:
            tempInput.append(reqDataset[col][index])
        target = tempInput
        if reqColScale == '' :
            tmpScale =0.0
        else:
            tmpScale = reqDataset[reqColScale][index]
        # tmpScale = reqDataset[reqColScale][index]

        return target,tmpScale
    
    def activation2(weightValue,inputValue):
        return weightValue*inputValue
    
    def chooseColumnTrainingData(reqCol,reqDataset,index):
        temp =[1.0]
        for col in reqCol:
            temp.append(reqDataset[col][index])
        target = temp
        return target