import pandas as pd
import numpy as np
from math import exp
from util import Function

class TrainingNetwork:
    def forwardPropagation(reqWeightInputToHidden,reqWeightHiddentoOutput,reqInput):
        tmpHiddenValue = []
        tmpHiddenValue.append(1.0)
        errorValue = 0.0
        # delta0Value = 0.0
        tmpCount=0
        for j in range(len(reqWeightInputToHidden)):
            tmpInputToHidden = reqWeightInputToHidden[j]      
            tmpCount=j
            yActivation = 0.0
            yTransferActivation = 0.0
            # YtransferActivation
            for k in range(len(tmpInputToHidden)):
                tmpInputToHidden2 = tmpInputToHidden[k]
                tmpInput = reqInput[k]
                tmpYActivation = Function.activation(tmpInputToHidden2,tmpInput)
                yActivation= yActivation+tmpYActivation
            yTransferActivation = Function.transferActivation(yActivation)
            tmpHiddenValue.append(yTransferActivation)

        
        # OtransferActivation
        oActivation=0.0
        for l in range(len(reqWeightHiddentoOutput)):
            tmpHiddenToOutput = reqWeightHiddentoOutput[l]
            tmpHiddenValue2 = tmpHiddenValue[l]
            tmpOActivation = Function.activation(tmpHiddenToOutput,tmpHiddenValue2)
            oActivation = oActivation+ tmpOActivation
        oTransferACtivation = Function.transferActivation(oActivation)
        
        # errorValue = (reqColScaleValue-oTransferACtivation)**2
        # # tmpErrorValue = errorValue(inputScale=reqColScaleValue,output=oTransferACtivation)
        # delta0Value = outputValue(output=oTransferACtivation,inputScale=reqColScaleValue)
        # print("Value Error:",tmpErrorValue)
        # print("Value Delta:",delta0Value)
        # print("List Hidden Value:",tmpHiddenValue)
        
        return oTransferACtivation,tmpHiddenValue,tmpCount
    
    def backPropagation(reqTmpHiddenValue,reqHiddenLayer,reqWeightHiddentoOutput,reqWeightInputToHidden,reqTempInputScale,reqLrate,reqDelta0,reqJ):
        newWeightOutputToHidden=[]
        newWeightHiddenToInput=[]
        
        for m in range(len(reqTmpHiddenValue)):
            tempHiddenValue = reqTmpHiddenValue[m]
            deltaWoha = Function.deltaValue(reqLrate=reqLrate,reqDelta=reqDelta0,reqHiddenValue=tempHiddenValue)
            tmpHiddenToOutput = reqWeightHiddentoOutput[m]
            tmpNewHiddenToOutput = tmpHiddenToOutput+deltaWoha
            newWeightOutputToHidden.append(tmpNewHiddenToOutput)
            # breakpoint()
                
        for n in range(reqHiddenLayer):
            tmpHiddenToOutput = reqWeightHiddentoOutput[n+1]
            delta0Net = Function.deltaNet(reqDelta0=reqDelta0,reqValue=tmpHiddenToOutput)
            tmpHiddenValue2 = reqTmpHiddenValue[n+1]
            delta02 = delta0Net*tmpHiddenValue2*(1-tmpHiddenValue2)
            tmpInputToHidden = reqWeightInputToHidden[reqJ]
            tempNewWeight = []
            for o in range(len(tmpInputToHidden)):
                inputValue = tmpInputToHidden[o]
                delta0Wia = Function.deltaValue(reqLrate=reqLrate,reqDelta=delta02,reqHiddenValue=inputValue)
                tempWeightInput = tmpInputToHidden[o]
                newWeightInput = tempWeightInput + delta0Wia
                tempNewWeight.append(newWeightInput)
                breakpoint()
            newWeightHiddenToInput.append(tempNewWeight)
            breakpoint()
        return newWeightHiddenToInput,newWeightOutputToHidden 
            