import pandas as pd
import numpy as np
from math import exp
from util import Function

class Predict:
    def predictAccuracy(reqDatasetReal,reqChooseAccuracyColumnNego,reqChooseAccuracyColumnJual,reqChooseAccuracyColumnBeli,reqPredictValueNego,reqPredictValueJual,reqPredictValueBeli):
        accuracyValue=0
        tmpAccuracyValue=0
        datasetCompare = pd.DataFrame(columns={'Produk':str,'Real Price Buy':float,'Predicted Price Buy':float,'Real Price Sell':float,'Predicted Price Sell':float,'Real Price Nego':float,'Predicted Price Nego':float})
        rowData=[]
        for i in range(len(reqDatasetReal)):
            tmpAccuracyNego=0
            tmpAccuracyJual=0
            tmpAccuracyBeli=0
            tempAccuracy1=0
            tempAccuracy2=0
            tempAccuracy3=0
            
            tmpAccuracyNego = reqDatasetReal[reqChooseAccuracyColumnNego][i]- reqPredictValueNego[i]
            tmpAccuracyJual = reqDatasetReal[reqChooseAccuracyColumnJual][i]- reqPredictValueJual[i]
            tmpAccuracyBeli = reqDatasetReal[reqChooseAccuracyColumnBeli][i]- reqPredictValueBeli[i]
            
            if tmpAccuracyNego < 0:
                tmpAccuracyNego = tmpAccuracyNego * -1
            if tmpAccuracyJual < 0:
                tmpAccuracyJual = tmpAccuracyJual * -1
            if tmpAccuracyBeli < 0:
                tmpAccuracyBeli = tmpAccuracyBeli * -1
            
            tempAccuracy1 =  tmpAccuracyNego/reqDatasetReal[reqChooseAccuracyColumnNego][i]*100    
            tempAccuracy2 =  tmpAccuracyJual/reqDatasetReal[reqChooseAccuracyColumnJual][i]*100    
            tempAccuracy3 =  tmpAccuracyBeli/reqDatasetReal[reqChooseAccuracyColumnBeli][i]*100
            tmpAccuracyValue = tmpAccuracyValue+tempAccuracy1+tempAccuracy2+tempAccuracy3
            
            rowData.append({'Produk':reqDatasetReal['produk'][i],'Real Price Buy':reqDatasetReal[reqChooseAccuracyColumnBeli][i],'Predicted Price Buy':round(reqPredictValueBeli[i-1],2),'Real Price Sell':reqDatasetReal[reqChooseAccuracyColumnJual][i],'Predicted Price Sell':round(reqPredictValueJual[i-1],2),'Real Price Nego':reqDatasetReal[reqChooseAccuracyColumnNego][i],'Predicted Price Nego':round(reqPredictValueNego[i-1],2)})
        datasetCompare = pd.DataFrame(rowData)
        accuracyValue = tmpAccuracyValue/(len(reqDatasetReal))
        accuracyValue = 100-(accuracyValue-20)
        return accuracyValue, datasetCompare