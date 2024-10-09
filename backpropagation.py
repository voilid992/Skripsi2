from preprocessing import kategoriScale as categoryScale
from preprocessing import suhuScale as temperatureScale
from preprocessing import qtyScale as qtyScale
from preprocessing import hargaBeliScale as buyScale
from preprocessing import hargaJualScale as sellScale
from preprocessing import hargaNegoScale as negoScale
from math import exp
import math
import random
import numpy as np
import pdb

scaleWeightInputToHidden = []
scaleWeightHiddenToOutput =[]
totalError =[]


def trainingNetwork(reqVar,reqHiddenLayer,reqEpoch,lrate,reqTargetError,reqCol,reqInput):
    count_epoch = 0
    StatusError = 0
    n_fold = 0
    checkerror = 0
    
    weightInputToHidden=[]
    weightHiddentoOutput = []
    
    for i in range(reqHiddenLayer+1):
        tempWeight = random.random()
        weightHiddentoOutput.append(tempWeight)
        
    for i in range(reqHiddenLayer):
        tmpWeight=[]
        for j in range(reqVar+1):
            tempWeight = random.random()
            tmpWeight.append(tempWeight)
        weightInputToHidden.append(tmpWeight)   
   
    weightInputToHidden = np.array(weightInputToHidden,dtype='float64')
    weightHiddentoOutput = np.array(weightHiddentoOutput, dtype='float64')

    while count_epoch < reqEpoch and StatusError !=1:
        for i in range(reqInput):
            # Collect Data from Dataset after normalization
            input1 = negoScale[i]
            input2 = sellScale[i]
            input3 = buyScale[i]
            input4 = qtyScale[i]
            input5 = temperatureScale[i]
            input6 = categoryScale[i]
            tempInputSCale =[]
            tempInputSCale.append(1.0)
            tempInputSCale.append(input1)
            tempInputSCale.append(input2)
            tempInputSCale.append(input3)
            tempInputSCale.append(input4)
            tempInputSCale.append(input5)
            tempInputSCale.append(input6)
            # print(len(tempInputSCale))
            tempHiddenValue =[]
            tempHiddenValue.append(1.0)
    
            #Forward Propagation   
            for j in range(len(weightInputToHidden)):
                tmpInputToHidden = weightInputToHidden[j]
                yActivation = 0.0
                yTransferActivation = 0.0
        
                # YtransferActivation
                for k in range(len(tmpInputToHidden)):
                    tmpInputToHidden2 = tmpInputToHidden[k]
                    # print("Index ke-",k,": ",tmpInputToHidden2)
                    tmpInput = tempInputSCale[k]
                    # print("Index ke-",k,": ",tmpInput)
                    tmpYActivation = tmpInputToHidden2*tmpInput
                    yActivation= yActivation+tmpYActivation
                yTransferActivation = 1.0/(1.0+pow(exp(1),(yActivation*-1)))
                tempHiddenValue.append(yTransferActivation)
            # OtransferActivation
            oActivation =0.0
            oTransferACtivation=0.0
            for l in range(len(weightHiddentoOutput)):
                tmpHiddenToOutput = weightHiddentoOutput[l]
                tmpHiddenValue2 = tempHiddenValue[l]
                tmpOActivation = tmpHiddenToOutput*tmpHiddenValue2
                oActivation = oActivation+ tmpOActivation
            oTransferACtivation = 1.0/(1.0+pow(exp(1),(oActivation*-1)))
            tmpErrorValue = ((input3-oTransferACtivation)**2)
            delta0 = (input3 - oTransferACtivation) * oTransferACtivation * (1 - oTransferACtivation)
            
            ## BackPropagation
            newWeightInputToHidden=[]
            newWeightHiddenToOutput=[]
            
            for p in range(len(tempHiddenValue)):
                tmpHiddenValue2 = tempHiddenValue[p]
                deltaWoha = lrate * delta0 * tmpHiddenValue2
                tmpHiddenToOutput = weightHiddentoOutput[p]
                tmpNewHiddenToOutput = tmpHiddenToOutput + deltaWoha
                newWeightHiddenToOutput.append(tmpNewHiddenToOutput) 
            for q in range(reqHiddenLayer):
                tmpHiddenToOutput = weightHiddentoOutput[q+1]
                delta0Net = delta0 * tmpHiddenToOutput
                tmphiddenValue = tempHiddenValue[q+1]
                delta02 = delta0Net * tmphiddenValue * ( 1 -tmphiddenValue)
                tmpInputToHidden = weightInputToHidden[j]
                tempNewWeightInputToHidden = []
                for r in range(len(tempInputSCale)):
                    inputValue = tempInputSCale[r]
                    delta0Wia = lrate * delta02 * inputValue
                    currWeight = tmpInputToHidden[r]
                    newWeight = currWeight + delta0Wia
                    tempNewWeightInputToHidden.append(newWeight)
                newWeightInputToHidden.append(tempNewWeightInputToHidden)
            
            weightInputToHidden = newWeightInputToHidden
            weightHiddentoOutput = newWeightHiddenToOutput
            breakpoint()
        
        if tmpErrorValue < targetError and count_epoch > 100 or n_fold >100 or count_epoch == epoch:
            currentError = tmpErrorValue
            scaleWeightInputToHidden.append(weightInputToHidden)
            scaleWeightHiddenToOutput.append(weightHiddentoOutput)
            StatusError = 1
            totalError.append(currentError)
        if tmpErrorValue > checkerror:
            n_fold += 1
        checkerror = tmpErrorValue
        print("Epoch : ",count_epoch,"Errors : ",tmpErrorValue)
        count_epoch += 1
        
reqColumn = ['kategoriScale', 'beliScale', 'jualScale', 'negoScale', 'qtyScale','suhuScale']
targetError = 0.001
lrate =0.9
epoch =1000
inputValue = 6911

# scaleWeightHiddenToOutput,scaleWeightInputToHidden= trainingNetwork(6,7,10,0.5,0.05)
trainingNetwork(reqInput=inputValue,reqCol=reqColumn,reqEpoch=epoch,reqHiddenLayer=len(reqColumn)+1,reqTargetError=targetError,reqVar=len(reqColumn),lrate=lrate)
        
                
                    
                