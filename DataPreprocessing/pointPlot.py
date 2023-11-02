import pandas as pd 
import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gpd 
import random
import math

df = pd.read_csv('D:\MajorProject\Customized-Bus-System\dataset\plotForm.csv')
# print(df)
finalDF = []

def getGeometryPoints(lat,longi,totalPassengers):
    res = ox.features_from_point( (lat, longi), tags = {'building': True}, dist=200 )
    polygons_list = []
    randomPolys=[]
    for j in res['geometry']:
        polygons_list.append(j)
    if(totalPassengers <= len(polygons_list)):
        randomPolys = random.sample(polygons_list, totalPassengers)
    else:
        quotient = totalPassengers/len(polygons_list)
        remainder = totalPassengers%len(polygons_list)
        for i in range(math.floor(quotient)):
            randomPolys = randomPolys + polygons_list
        randomPolys = randomPolys + random.sample(polygons_list, remainder)
    return randomPolys

def createDataframe(startPloy,endPoly,fromStopName,fromLat,fromLong,toStopName,toLat,toLong):
    df=[]
    columns = ['start_Lat','start_long','from_stop_name','from_lat','from_long','to_stop_name','to_lat','to_long','end_lat','end_long']
    for startPloy, endPoly in zip(startPloy, endPoly):
        df.append([startPloy.centroid.x,startPloy.centroid.y,fromStopName,fromLat,fromLong,toStopName,toLat,toLong,endPoly.centroid.x,endPoly.centroid.y])
        # print("centroid ",i.centroid)
        # print("centroid loc ",i.centroid.x,i.centroid.y)
    newDf = pd.DataFrame(df, columns=columns)
    # print("newDf ",type(newDf))
    return newDf




for i in df.itertuples():
    fromPloys = getGeometryPoints(i.from_lat,i.from_long,i.total_passenger)
    toPloys = getGeometryPoints(i.to_lat,i.to_long,i.total_passenger)
    newDf = createDataframe(fromPloys,toPloys,i.from_stop_name,i.from_lat,i.from_long,i.to_stop_name,i.to_lat,i.to_long)
    testDF = pd.DataFrame(finalDF)
    print("newDF",newDf)
    print("testDF",testDF)
    finalDF = pd.concat([testDF,newDf])
    finalDF = finalDF.reset_index(drop=True)
    # finalDF.append(newDf)
    # print(polygons_list)
    # gfd = gpd.GeoDataFrame(res)
    # fig, ax = plt.subplots()
    # # Plot the residential areas
    # gfd.plot(ax=ax, color='lightblue', alpha=0.7, linewidth=0.5, edgecolor='k')
    # ax.set_title("Residential Areas")
    # # Remove axis labels
    # ax.set_axis_off()
    # # Display the plot
    # plt.show()
print("finalDF",finalDF)
finalDF.to_csv('finalDF.csv')

