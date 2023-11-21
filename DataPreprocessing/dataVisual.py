import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gpd 
import pandas as pd
import numpy.random as rnd
# fig, ax = plt.subplots()




passengerNodes = pd.read_csv('../dataset/finalDF700.csv')
passengerNodes = passengerNodes.loc[passengerNodes['from_stop_name'] == 'anand nagar']

startNodes = []
for node in passengerNodes.itertuples():
    startNodes.append([node.start_lat, node.start_long])
# startNodes = pd.DataFrame(startNodes, columns=['start_lat', 'start_long'])
# print(startNodes.head())
endNodes = []
for node in passengerNodes.itertuples():
    endNodes.append([node.end_lat, node.end_long])


unique_nodes = []

unique_start_nodes = []
for node in startNodes:
    if node in unique_nodes:
        unique_nodes.append([node[0]+rnd.normal(0,0.00005), node[1]+rnd.normal(0,0.00005)])
        unique_start_nodes.append([node[0]+rnd.normal(0,0.00005), node[1]+rnd.normal(0,0.00005)])
    else :
        unique_nodes.append(node)
        unique_start_nodes.append(node)
print(len(unique_start_nodes))
unique_start_nodes = pd.DataFrame(unique_start_nodes, columns=['start_lat', 'start_long'])

unique_end_nodes = []
for node in endNodes:
    if node in unique_nodes:
        unique_nodes.append([node[0]+rnd.normal(0,0.00005), node[1]+rnd.normal(0,0.00005)])
        unique_end_nodes.append([node[0]+rnd.normal(0,0.00005), node[1]+rnd.normal(0,0.00005)])
    else :
        unique_nodes.append(node)
        unique_end_nodes.append(node)
print(len(unique_end_nodes))
unique_end_nodes = pd.DataFrame(unique_end_nodes, columns=['end_lat', 'end_long'])

passengerPickupNodes = gpd.GeoDataFrame(unique_start_nodes, crs='EPSG:4326', geometry=gpd.points_from_xy(unique_start_nodes['start_lat'], unique_start_nodes['start_long']))
print(passengerPickupNodes.head())
passengerDropNodes = gpd.GeoDataFrame(unique_end_nodes, crs='EPSG:4326', geometry=gpd.points_from_xy(unique_end_nodes['end_lat'], unique_end_nodes['end_long']))
print(passengerDropNodes.head())

# passengerPickupNodes = gpd.GeoDataFrame(passengerNodes, crs='EPSG:4326', geometry=gpd.points_from_xy(passengerNodes['start_lat'], passengerNodes['start_long']))
# print(passengerPickupNodes.head())
# passengerDropNodes = gpd.GeoDataFrame(passengerNodes, crs='EPSG:4326', geometry=gpd.points_from_xy(passengerNodes['end_lat'], passengerNodes['end_long']))
# print(passengerDropNodes.head())
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

