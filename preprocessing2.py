### Package
import pandas as pd
import numpy as np

columnToDrop = ['Unnamed: 0']
dataset = pd.read_csv("NewDataTransactionV2.csv")
dataset = dataset.drop(columnToDrop,axis=1)

datasetMinMax = dataset

indexTraining = (75*len(datasetMinMax))/100
datasetMinMaxTraining = datasetMinMax
# datasetMinMaxTraining = datasetMinMax[:int(indexTraining)]
# datasetTraining =dataset[:int(indexTraining)]
datasetTraining =dataset
kategoriScale=0
beliScale=0
jualScale=0
negoScale=0
qtyScale=0
suhuScale=0

maxKategoriScale=max(datasetMinMaxTraining['kategori'])
maxBeliScale=max(datasetMinMaxTraining['beli'])
maxJualScale=max(datasetMinMaxTraining['jual'])
maxNegoScale=max(datasetMinMaxTraining['nego'])
maxQtyScale=max(datasetMinMaxTraining['qty'])
maxSuhuScale=max(datasetMinMaxTraining['Suhu'])

minKategoriScale=min(datasetMinMaxTraining['kategori'])
minBeliScale=min(datasetMinMaxTraining['beli'])
minJualScale=min(datasetMinMaxTraining['jual'])
minNegoScale=min(datasetMinMaxTraining['nego'])
minQtyScale=min(datasetMinMaxTraining['qty'])
minSuhuScale=min(datasetMinMaxTraining['Suhu'])
# datasetMinMax['kdScale']=kdScale
datasetMinMaxTraining['kategoriScale']=kategoriScale
datasetMinMaxTraining['beliScale']=beliScale
datasetMinMaxTraining['jualScale']=jualScale
datasetMinMaxTraining['negoScale']=negoScale
datasetMinMaxTraining['qtyScale']=qtyScale
datasetMinMaxTraining['suhuScale']=suhuScale
for i in range(len(datasetMinMaxTraining)):
    # kdScale = (datasetMinMax['kd'][i]-min(datasetMinMax['kd']))/(max(datasetMinMax['kd'])-min(datasetMinMax['kd']))
    kategoriScale = (datasetMinMaxTraining['kategori'][i]-minKategoriScale)/(maxKategoriScale-minKategoriScale)
    beliScale = (datasetMinMaxTraining['beli'][i]-minBeliScale)/(maxBeliScale-minBeliScale)
    jualScale = (datasetMinMaxTraining['jual'][i]-minJualScale)/(maxJualScale-minJualScale)
    negoScale = (datasetMinMaxTraining['nego'][i]-minNegoScale)/(maxNegoScale-minNegoScale)
    qtyScale = (datasetMinMaxTraining['qty'][i]-minQtyScale)/(maxQtyScale-minQtyScale)
    suhuScale = (datasetMinMaxTraining['Suhu'][i]-minSuhuScale)/(maxSuhuScale-minSuhuScale)
    # datasetMinMax['kdScale'][i]=kdScale
    datasetMinMaxTraining['kategoriScale'][i]=kategoriScale
    datasetMinMaxTraining['beliScale'][i]=beliScale
    datasetMinMaxTraining['jualScale'][i]=jualScale
    datasetMinMaxTraining['negoScale'][i]=negoScale
    datasetMinMaxTraining['qtyScale'][i]=qtyScale
    datasetMinMaxTraining['suhuScale'][i]=suhuScale
    
datasetMinMaxTesting = datasetMinMax[int(indexTraining):]
datasetMinMaxTesting.index = datasetMinMaxTesting.reset_index(drop=True)
datasetTesting = dataset[int(indexTraining):]
datasetTesting= datasetTesting.reset_index(drop=True)

kategoriScale=0
beliScale=0
jualScale=0
negoScale=0
qtyScale=0
suhuScale=0

maxKategoriScale=max(datasetMinMaxTesting['kategori'])
maxBeliScale=max(datasetMinMaxTesting['beli'])
maxJualScale=max(datasetMinMaxTesting['jual'])
maxNegoScale=max(datasetMinMaxTesting['nego'])
maxQtyScale=max(datasetMinMaxTesting['qty'])
maxSuhuScale=max(datasetMinMaxTesting['Suhu'])

minKategoriScale=min(datasetMinMaxTesting['kategori'])
minBeliScale=min(datasetMinMaxTesting['beli'])
minJualScale=min(datasetMinMaxTesting['jual'])
minNegoScale=min(datasetMinMaxTesting['nego'])
minQtyScale=min(datasetMinMaxTesting['qty'])
minSuhuScale=min(datasetMinMaxTesting['Suhu'])
# datasetMinMax['kdScale']=kdScale
datasetMinMaxTesting['kategoriScale']=kategoriScale
datasetMinMaxTesting['beliScale']=beliScale
datasetMinMaxTesting['jualScale']=jualScale
datasetMinMaxTesting['negoScale']=negoScale
datasetMinMaxTesting['qtyScale']=qtyScale
datasetMinMaxTesting['suhuScale']=suhuScale
for i in range(1,len(datasetMinMaxTesting)):
    kategoriScale = (datasetMinMaxTesting['kategori'][i]-minKategoriScale)/(maxKategoriScale-minKategoriScale)
    beliScale = (datasetMinMaxTesting['beli'][i]-minBeliScale)/(maxBeliScale-minBeliScale)
    jualScale = (datasetMinMaxTesting['jual'][i]-minJualScale)/(maxJualScale-minJualScale)
    negoScale = (datasetMinMaxTesting['nego'][i]-minNegoScale)/(maxNegoScale-minNegoScale)
    qtyScale = (datasetMinMaxTesting['qty'][i]-minQtyScale)/(maxQtyScale-minQtyScale)
    suhuScale = (datasetMinMaxTesting['Suhu'][i]-minSuhuScale)/(maxSuhuScale-minSuhuScale)
    
    datasetMinMaxTesting['kategoriScale'][i]=kategoriScale
    datasetMinMaxTesting['beliScale'][i]=beliScale
    datasetMinMaxTesting['jualScale'][i]=jualScale
    datasetMinMaxTesting['negoScale'][i]=negoScale
    datasetMinMaxTesting['qtyScale'][i]=qtyScale
    datasetMinMaxTesting['suhuScale'][i]=suhuScale
    
columnToDrop =['kategori','beli','jual','nego','qty','Suhu']
datasetMinMaxTesting= datasetMinMaxTesting.drop(columnToDrop,axis=1)
datasetMinMaxTraining= datasetMinMaxTraining.drop(columnToDrop,axis=1)
    