def activation(weightValue: np.float64,inputValue: np.float64):
    value = float(64)
    value = weightValue*inputValue
    return value

def errorValue(inputScale: np.float64, output: np.float64):
    print(output)
    print(inputScale)
    value =0.0
    value = pow((inputScale-output),2)
    return value

def outputValue(output: np.float64,inputScale: np.float64):
    value= 64.0
    value1=(inputScale-output)*output*(1-output)
    value = value1
    return value

def deltaValue(reqLrate: np.float64,reqDelta: np.float64,reqHiddenValue: np.float64):
    value=0.0
    value=reqLrate*reqDelta*reqHiddenValue
    return value

def deltaNet(reqDelta0: np.float64,reqValue: np.float64):
    value=0.0
    value=reqDelta0*reqValue
    return value

def transferActivation(activationValue: np.float64):
    transferValue=float(64)
    transferValue = 1.0/(1.0+pow(math.exp(1),(activationValue*-1)))
    return transferValue

def chooseColumn(reqCol,reqDataset,index,reqColScale):
    tempInput =[1.0]
    tmpScale =0.0
    for col in reqCol:
        tempInput.append(reqDataset[col][index])
    target = tempInput
    for col2 in reqColScale:
        tmpScale = reqDataset[col2][index]
    # tmpScale = reqDataset[reqColScale][index]
    # print(tmpScale)
    return target,tmpScale

def forwardPropagation(reqWeightInputToHidden,reqWeightHiddentoOutput,reqInput,reqColScaleValue:np.float64):
    tmpHiddenValue = [1.0]
    errorValue = 0.0
    delta0Value = 0.0
    for j in range(len(reqWeightInputToHidden)):
        tmpInputToHidden = reqWeightInputToHidden[j]
        # print("Index ke-",i,", Bagian ke-",j,": ",weightInputToHidden[j])
        yActivation = 0.0
        yTransferActivation = 0.0
        
        # YtransferActivation
        for k in range(len(tmpInputToHidden)):
            tmpInputToHidden2 = tmpInputToHidden[k]
            # print("Index ke-",k,": ",tmpInputToHidden[k])
            tmpInput = reqInput[k]
            tmpYActivation = activation(tmpInputToHidden2,tmpInput)
            yActivation= yActivation+tmpYActivation
        yTransferActivation = transferActivation(yActivation)
        tmpHiddenValue.append(yTransferActivation)
    
    # OtransferActivation
    oActivation =0.0
    oTransferACtivation=0.0
    for l in range(len(reqWeightHiddentoOutput)):
        tmpHiddenToOutput = reqWeightHiddentoOutput[l]
        tmpHiddenValue2 = tmpHiddenValue[l]
        tmpOActivation = activation(tmpHiddenToOutput,tmpHiddenValue2)
        oActivation = oActivation+ tmpOActivation
        oTransferACtivation = transferActivation(oActivation)
    
    errorValue = pow((reqColScaleValue-oTransferACtivation),2)
    delta0Value = outputValue(output=oTransferACtivation,inputScale=reqColScaleValue)
    
    return errorValue,delta0Value,tmpHiddenValue 

def backPropagation(reqTmpHiddenValue,reqHiddenLayer,reqWeightHiddentoOutput,reqWeightInputToHidden,reqTempInputScale,reqLrate,reqDelta0):
    deltaWoha =0.0
    # print("Hidden to Output:",reqWeightHiddentoOutput)
    # print("Hidden to Output:",len(reqWeightHiddentoOutput))
    # print("Hidden Value:",reqTmpHiddenValue)
    # print("Hidden Value:",len(reqTmpHiddenValue))
    newWeightOutputToHidden=[]
    newWeightHiddenToInput=[]
    # print(len(reqTmpHiddenValue))
    for m in range(len(reqTmpHiddenValue)):
        tempHiddenValue = reqTmpHiddenValue[m]
        deltaWoha = deltaValue(reqLrate=reqLrate,reqDelta=reqDelta0,reqHiddenValue=tempHiddenValue)
        # print("Index reqWeightHiddentoOutput ke-",m,":",reqWeightHiddentoOutput[m])
        # print("Index reqTmpHiddenValue ke-",m,":",reqTmpHiddenValue[m])
        tmpHiddenToOutput = reqWeightHiddentoOutput[m]
        tmpNewHiddenToOutput = tmpHiddenToOutput+deltaWoha
        newWeightOutputToHidden.append(tmpNewHiddenToOutput)
        # breakpoint()
            
    for n in range(reqHiddenLayer):
        tmpHiddenToOutput = reqWeightHiddentoOutput[n+1]
        delta0Net = deltaNet(reqDelta0=reqDelta0,reqValue=tmpHiddenToOutput)
        tmpHiddenValue2 = reqTmpHiddenValue[n+1]
        delta02 = delta0Net*tmpHiddenValue2*(1-tmpHiddenValue2)
        tmpInputToHidden = reqWeightInputToHidden[n]
        tempNewWeight = []
        for o in range(len(reqTempInputScale)):
            inputValue = reqTempInputScale[o]
            delta0Wia = deltaValue(reqLrate=reqLrate,reqDelta=delta02,reqHiddenValue=inputValue)
            tempWeightInput = tmpInputToHidden[o]
            newWeightInput = tempWeightInput + delta0Wia
            tempNewWeight.append(newWeightInput)
            breakpoint()
        newWeightHiddenToInput.append(tempNewWeight)
        breakpoint()
    return newWeightHiddenToInput,newWeightOutputToHidden
    