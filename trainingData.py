import pandas as pd
import numpy as np
from util import Function

class TrainingData: 
    def showPredicted(reqScaleWeightHiddenToOutput,reqScaleWeightInputToHidden,reqInput):
        tmpHiddenValue = []
        tmpHiddenValue.append(1.0)
        errorValue = 0.0
        # delta0Value = 0.0
        tmpCount=0
        for j in range(len(reqScaleWeightInputToHidden)):
            tmpInputToHidden = reqScaleWeightInputToHidden[j]      
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
        for l in range(len(reqScaleWeightHiddenToOutput)):
            tmpHiddenToOutput = reqScaleWeightHiddenToOutput[l]
            tmpHiddenValue2 = tmpHiddenValue[l]
            tmpOActivation = Function.activation(tmpHiddenToOutput,tmpHiddenValue2)
            oActivation = oActivation+ tmpOActivation
        oTransferACtivation = Function.transferActivation(oActivation)
        return oTransferACtivation
          