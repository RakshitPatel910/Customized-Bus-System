import pandas as pd
import string

filePath='../dataset/clean_data/700.csv'


def timeProbability(filePath):
    newTimeDf = []
    column=['Index','date','day','direction','from_00_to_01','from_01_to_02','from_02_to_03','from_03_to_04','from_04_to_05','from_05_to_06','from_06_to_07','from_07_to_08','from_08_to_09','from_09_to_10','from_10_to_11','from_11_to_12','from_12_to_13','from_13_to_14','from_14_to_15','from_15_to_16','from_16_to_17','from_17_to_18','from_18_to_19','from_19_to_20','from_20_to_21','from_21_to_22','from_22_to_23','from_23_to_24']
    timeData = pd.read_csv(filePath)
    pathName = filePath.rsplit("/")[len(filePath.rsplit("/"))-1].rsplit(".")[0]
    
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
    # print(probabDf)


def calProbab(df):
    upTotal=0
    downTotal = 0
    newDf = df
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
                probabDf.iat[1,j] = (int(i[j])/upTotal)*100
                j+=1
        else:
            while(j<len(i)):
                # setattr(newDf,i[j],(int(i[j])/downTotal)*100)
                probabDf.iat[0,j] = (int(i[j])/downTotal)*100
                j+=1

    # probabDf = pd.DataFrame(newDf,columns=column)
    probabDf = probabDf.drop(["Index"],axis=1)
    return probabDf
        


timeProbability(filePath)

__all__ = ["timeProbability"]

