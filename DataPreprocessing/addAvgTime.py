import pandas as pd
import geopandas as gpd
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/finalDF700.csv')
df = df[0:5]
# print(df)

graph = ox.graph_from_point((19.26542, 72.96664), dist=15000, network_type='drive')

graph = ox.add_edge_speeds(graph)
graph = ox.add_edge_travel_times(graph)

print(ox.graph_to_gdfs(graph))
# start_points = gpd.GeoDataFrame( geometry=gpd.points_from_xy(df['start_lat'], df['start_long']))
# end_points = gpd.GeoDataFrame( geometry=gpd.points_from_xy(df['end_lat'], df['end_long']))
# print(start_points)

# start_bus_stop = ox.nearest_edges(graph, df['start_lat'], df['start_long'], return_dist=False)
# end_bus_stop = ox.nearest_edges(graph, df['end_lat'], df['end_long'], return_dist=False)

# print(start_bus_stop)
# print()
# print(end_bus_stop)



# ox.plot_graph(graph)
# plt.show()



# start_location = (72.96939068818419, 19.264081470953254)
# end_location = (72.9524901, 19.282555750000004) 
start_location = (72.85512807917517,19.31069864366639)
end_location = (72.8559418653558,19.298457266753697) 

# start_node = ox.nearest_nodes(graph, 72.96939068818419, 19.264081470953254)
# end_node = ox.nearest_nodes(graph, 72.9524901, 19.282555750000004)
start_node = ox.nearest_nodes(graph, 72.85512807917517,19.31069864366639)
end_node = ox.nearest_nodes(graph, 72.8559418653558,19.298457266753697)

# shortest_path = ox.shortest_path(graph, start_location, end_location, weight='travel_time')
shortest_path = nx.shortest_path(graph, start_node, end_node, weight='travel_time')

travel_time = nx.shortest_path_length(graph, start_node, end_node, weight='travel_time')
time = sum(ox.utils_graph.get_route_edge_attributes(graph, shortest_path, 'travel_time'))
print(travel_time)
print(time)

# fig, ax = plt.subplots()

fig, ax = ox.plot_graph_route(graph, shortest_path, node_size=0, show=False, close=False)
# print(graph[0:5])
# s = gpd.GeoDataFrame([1,2], geometry=gpd.points_from_xy([72.96939068818419, 72.9524901],[19.264081470953254, 19.282555750000004]) )
s = gpd.GeoDataFrame([1,2], geometry=gpd.points_from_xy([72.85512807917517, 72.8559418653558],[19.31069864366639, 19.298457266753697]) )
# sg = ox.graph_from_gdfs(s,[])
# print(s)
# e = gpd.GeoDataFrame( geometry=gpd.points_from_xy(72.9686927009615,19.263435000721955) )
# ox.plot_graph(s, ax=ax, node_color='green', node_size=200 )
# ox.plot_graph(e, node_color='red', node_size=20 )
# plt.show()
# ax.plot(72.96664346073631, 19.265421428900176, 'o', markersize=10, color='green')
# ax.plot(72.9686927009615, 19.263435000721955, 'o', markersize=10, color='green')
# ox.plot_graph(sg, node_color='yellow', node_size=20)
# s.plot()
ax.scatter(72.85512807917517,19.31069864366639, c='green')
ax.scatter(72.8559418653558,19.298457266753697, c='green')

# graph.plot(ax=ax, color='lightblue', alpha=0.7, linewidth=0.5,)
# shortest_path.plot(ax=ax, color='red', linewidth=0.5,)
# s.plot(ax=ax, color='green', marker='o', alpha=0.7, linewidth=0.5)
plt.show()