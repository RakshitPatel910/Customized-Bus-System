import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gpd 
import pandas as pd
# fig, ax = plt.subplots()




passengerNodes = pd.read_csv('./finalDF.csv')

passengerPickupNodes = gpd.GeoDataFrame(passengerNodes, crs='EPSG:4326', geometry=gpd.points_from_xy(passengerNodes['start_lat'], passengerNodes['start_long']))
print(passengerPickupNodes.head())
passengerDropNodes = gpd.GeoDataFrame(passengerNodes, crs='EPSG:4326', geometry=gpd.points_from_xy(passengerNodes['end_lat'], passengerNodes['end_long']))
print(passengerDropNodes.head())

# uniqe_pickup = gpd.GeoDataFrame()
# for i in passengerPickupNodes.iterrows():
#     # point = ( i.start_lat, i.start_long )
#     if i not in uniqe_pickup:
#         uniqe_pickup.merge(passengerPickupNodes.loc[i])
# duplicate_points = gpd.GeoDataFrame()
# for i in uniqe_pickup.iterrows():
#     duplicate_points = duplicate_points.merge( passengerPickupNodes.loc[passengerPickupNodes['start_lat'] == i['start_lat'] and passengerPickupNodes['start_long'] == i['start_long']])
# consolidate_points = ox.consolidate_intersections(duplicate_points)
# print(len(uniqe_pickup))
# print(len(duplicate_points))

res = ox.features_from_point( (19.295233, 72.854393), tags = { 'highway':True, 'building': True }, dist=15000 )
residential_highway_gdf = gpd.GeoDataFrame.from_features(res, crs='EPSG:4326')

print(res)

gfd = gpd.GeoDataFrame.from_features(res, crs='EPSG:4326')

gdfs = [residential_highway_gdf, passengerPickupNodes, passengerDropNodes]
colors = ['lightblue', 'green', 'red']
markers = ['None', 'o', 'o']

fig, ax = plt.subplots()


for i in range(len(gdfs)):
    gdfs[i].plot(ax=ax, color=colors[i], marker=markers[i], alpha=0.7, linewidth=0.5,)

plt.show()

