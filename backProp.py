import pandas as pd
import numpy as np
from math import exp
from util import Function
from preprocessing2 import  datasetMinMaxTraining
from util import Function
from trainingNetwork import TrainingNetwork

class backProp:
    def trainingNetwork(reqCol,reqVar,reqHiddenLayer,reqEpoch,lrate,reqTargetError,reqInput,reqColScale):
        scaleWeightInputToHidden = []
        scaleWeightHiddenToOutput =[]
        totalError =[]
        
        
        count_epoch = 0
        StatusError = 0
        n_fold = 0
        checkerror = 0
        
        weightInputToHidden = Function.inputWeight(reqHiddenLayer,reqVar)
        weightHiddentoOutput =Function.inputWeight(reqHiddenLayer,0)   
    
        # weightInputToHidden = np.array(weightInputToHidden,dtype='float64')
        # weightHiddentoOutput = np.array(weightHiddentoOutput, dtype='float64')

        while count_epoch < reqEpoch and StatusError !=1:
            for i in range(len(datasetMinMaxTraining)):
                # Collect Data from Dataset after normalization
                tempInputSCale,colScale= Function.chooseColumn(reqCol,datasetMinMaxTraining,i,reqColScale)
                breakpoint()
                
                oTransferACtivation,tmpHiddenValue,tmpCount = TrainingNetwork.forwardPropagation(reqWeightInputToHidden=weightInputToHidden,reqWeightHiddentoOutput=weightHiddentoOutput,reqInput=tempInputSCale)
                
                errorValue = ((colScale-oTransferACtivation)**2)
                delta0 = (colScale - oTransferACtivation) * oTransferACtivation * (1 - oTransferACtivation)
                breakpoint()
                
                ## BackPropagation
                #     breakpoint()
                newWeightInputToHidden,newWeightHiddenToOutput=TrainingNetwork.backPropagation(reqTmpHiddenValue=tmpHiddenValue,reqHiddenLayer=reqHiddenLayer,reqWeightHiddentoOutput=weightHiddentoOutput,reqWeightInputToHidden=weightInputToHidden,reqTempInputScale=tempInputSCale,reqLrate=lrate,reqDelta0=delta0,reqJ=tmpCount)


                weightInputToHidden = newWeightInputToHidden
                weightHiddentoOutput = newWeightHiddenToOutput
                breakpoint()
            
            if errorValue > checkerror:
                n_fold += 1
                
            if errorValue < reqTargetError or n_fold > 100 or count_epoch >= reqEpoch:
                currentError = errorValue
                scaleWeightInputToHidden=weightInputToHidden
                scaleWeightHiddenToOutput=weightHiddentoOutput
                StatusError = 1
                totalError.append(currentError)     
            
            checkerror = errorValue
            
            print("Epoch : ",count_epoch,"Errors : ",errorValue,' Status Error:',StatusError,' Fold:',n_fold)

            count_epoch += 1
        return scaleWeightHiddenToOutput,scaleWeightInputToHidden,totalError 