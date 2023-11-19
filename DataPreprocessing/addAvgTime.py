import pandas as pd
import geopandas as gpd
import osmnx as ox
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/finalDF700.csv')
df = df[0:5]
# print(df)

graph = ox.graph_from_point((19.26542, 72.96664), dist=15000)

# start_points = gpd.GeoDataFrame( geometry=gpd.points_from_xy(df['start_lat'], df['start_long']))
# end_points = gpd.GeoDataFrame( geometry=gpd.points_from_xy(df['end_lat'], df['end_long']))
# print(start_points)

# start_bus_stop = ox.nearest_edges(graph, df['start_lat'], df['start_long'], return_dist=False)
# end_bus_stop = ox.nearest_edges(graph, df['end_lat'], df['end_long'], return_dist=False)

# print(start_bus_stop)
# print()
# print(end_bus_stop)



ox.plot_graph(graph)

plt.show()