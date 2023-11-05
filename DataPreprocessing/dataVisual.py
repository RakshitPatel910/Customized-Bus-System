import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gpd 
import pandas as pd
import numpy.random as rnd
# fig, ax = plt.subplots()




passengerNodes = pd.read_csv('../dataset/finalDF700.csv')

passengerPickupNodes = gpd.GeoDataFrame(passengerNodes, crs='EPSG:4326', geometry=gpd.points_from_xy(passengerNodes['start_lat'], passengerNodes['start_long']))
print(passengerPickupNodes.head())
passengerDropNodes = gpd.GeoDataFrame(passengerNodes, crs='EPSG:4326', geometry=gpd.points_from_xy(passengerNodes['end_lat'], passengerNodes['end_long']))
print(passengerDropNodes.head())
# passengerPickupNodes = gpd.GeoDataFrame(passengerNodes, crs='EPSG:4326', geometry=gpd.points_from_xy(passengerNodes['start_lat']+rnd.normal(0,0.0001), passengerNodes['start_long']+rnd.normal(0,0.0001)))
# print(passengerPickupNodes.head())
# passengerDropNodes = gpd.GeoDataFrame(passengerNodes, crs='EPSG:4326', geometry=gpd.points_from_xy(passengerNodes['end_lat']+rnd.normal(0,0.0001), passengerNodes['end_long']+rnd.normal(0,0.0001)))
# print(passengerDropNodes.head())

res = ox.features_from_point( (19.295233, 72.854393), tags = { 'highway':True, 'building': True }, dist=15000 )
residential_highway_gdf = gpd.GeoDataFrame.from_features(res, crs='EPSG:4326')

print(res)

# gfd = gpd.GeoDataFrame.from_features(res, crs='EPSG:4326')

# passengerPickupNodes = ox.consolidate_intersections(passengerPickupNodes, tolerance=0.0001)

gdfs = [residential_highway_gdf, passengerPickupNodes, passengerDropNodes]
colors = ['lightblue', 'green', 'red']
markers = ['None', '^', 'o']

fig, ax = plt.subplots()


for i in range(len(gdfs)):
    gdfs[i].plot(ax=ax, color=colors[i], marker=markers[i], alpha=0.7, linewidth=0.5,)

plt.show()

