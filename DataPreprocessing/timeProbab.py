import pandas as pd
import string
import numpy as np

# filePath='../dataset/clean_data/700.csv'
path ='../dataset/Intermediate/intermediate700.csv'

def timeProbability(filePath):
    newTimeDf = []
    column=['Index','date','day','direction','from_00_to_01','from_01_to_02','from_02_to_03','from_03_to_04','from_04_to_05','from_05_to_06','from_06_to_07','from_07_to_08','from_08_to_09','from_09_to_10','from_10_to_11','from_11_to_12','from_12_to_13','from_13_to_14','from_14_to_15','from_15_to_16','from_16_to_17','from_17_to_18','from_18_to_19','from_19_to_20','from_20_to_21','from_21_to_22','from_22_to_23','from_23_to_24']
    print(filePath)
    pathName = filePath.rsplit("/")[len(filePath.rsplit("/"))-1].rsplit(".")[0].rsplit("te")[2]
    print(pathName)
    timeData = pd.read_csv('../dataset/clean_data/'+pathName+'.csv')
    # print(filePath.rsplit("/")[len(filePath.rsplit("/"))-1].rsplit(".")[0])
    count = 0
    for i in timeData.itertuples():
        if(i.route_name == 'date'):
            # newTimeDf.append(i)
            count=count+1
            # print(i)
        elif(count>0):
            newTimeDf.append(i)
    # print(newTimeDf)
    timeDF = pd.DataFrame(newTimeDf,columns=column,index=None)
    timeDF=timeDF.drop(["Index"],axis=1)
    # print(timeDF)
    probabDf = calProbab(timeDF)
    addDeparture(pathName,probabDf)
    # print(probabDf)


def calProbab(df):
    upTotal=0
    downTotal = 0
    newDf = df
    print(newDf)
    column=['Index','date','day','direction','from_00_to_01','from_01_to_02','from_02_to_03','from_03_to_04','from_04_to_05','from_05_to_06','from_06_to_07','from_07_to_08','from_08_to_09','from_09_to_10','from_10_to_11','from_11_to_12','from_12_to_13','from_13_to_14','from_14_to_15','from_15_to_16','from_16_to_17','from_17_to_18','from_18_to_19','from_19_to_20','from_20_to_21','from_21_to_22','from_22_to_23','from_23_to_24']
    probabDf = pd.DataFrame(newDf,columns=column)
    for i in df.itertuples():
        j=4
        if(i.direction == 'UP'):
            while(j<len(i)):
                upTotal+=int(i[j])
                j+=1
        else:
            while(j<len(i)):
                downTotal+=int(i[j])
                j+=1
    # print(upTotal," ",downTotal)
    # print(df.iat[1,4])
    for i in newDf.itertuples():
        j=4
        if(i.direction == 'UP'):
            while(j<len(i)):
                # setattr(newDf,i[j],(int(i[j])/upTotal)*100)
                probabDf.iat[1,j] = (int(i[j])/upTotal)
                j+=1
        else:
            while(j<len(i)):
                # setattr(newDf,i[j],(int(i[j])/downTotal)*100)
                probabDf.iat[0,j] = (int(i[j])/downTotal)
                j+=1

    # probabDf = pd.DataFrame(newDf,columns=column)
    probabDf = probabDf.drop(["Index"],axis=1)
    # print(probabDf)
    return probabDf
        

def addDeparture(pathName,timeDF):
    reqDF = pd.read_csv('../dataset/passengerRequests/request'+pathName+'.csv')
    time=['from_00_to_01','from_01_to_02','from_02_to_03','from_03_to_04','from_04_to_05','from_05_to_06','from_06_to_07','from_07_to_08','from_08_to_09','from_09_to_10','from_10_to_11','from_11_to_12','from_12_to_13','from_13_to_14','from_14_to_15','from_15_to_16','from_16_to_17','from_17_to_18','from_18_to_19','from_19_to_20','from_20_to_21','from_21_to_22','from_22_to_23','from_23_to_24']
    UP =[]
    DOWN=[]
    
    # print(type(timeDF))
    # print(timeDF.date)
    for i in timeDF.itertuples():
        if(i.direction == 'DOWN'):
            j=3
            while(j<len(i)-1):
                DOWN.append(timeDF.iat[0,j])
                j+=1
        elif(i.direction == 'UP'):
            j=3
            while(j<len(i)-1):
                UP.append(timeDF.iat[1,j])
                j+=1
    # print(UP)
    # print(DOWN)
    print(np.sum(UP))
    print(np.sum(DOWN))
    departureTime = []
    timeDiff = 10
    # reqDF.insert(len(reqDF.columns), 'departureTime', [])
    for i in reqDF.itertuples():
        if(i.direction == 'up'):
            tmp = np.random.choice(time, p=UP)
            hrs = tmp.rsplit("_")[1]
            hrs = hrs+":"+str(np.random.randint(1, 6)*10)
            departureTime.append(hrs)
            # reqDF.iat[i.Index,len(i)] = np.random.choice(time, p=UP)
            # i['departureTime'] = np.random.choice(time, p=UP)
        elif(i.direction == 'down'):
            tmp = np.random.choice(time, p=DOWN)
            hrs = tmp.rsplit("_")[1]
            hrs = hrs+":"+str(np.random.randint(1, 6)*10)
            departureTime.append(hrs)
            # i['departureTime'] = np.random.choice(time, p=DOWN)

    reqDF.insert(len(reqDF.columns), 'departureTime', departureTime)
    reqDF = reqDF.drop(['Unnamed: 0'], axis=1)
    print(reqDF)
    # reqDF = reqDF.drop(['departureTime'], axis=1)
    reqDF.to_csv('../dataset/passengerRequests/request700.csv')

# timeProbability(path)

__all__ = ["timeProbability"]

