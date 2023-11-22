import pandas as pd
import geopandas as gpd
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

def calcAvgTime(graph, row):
# def calcAvgTime(graph, row, ax):
    start_location = [row.start_lat, row.start_long]
    end_location = [row.end_lat, row.end_long]

    start_node = ox.nearest_nodes(graph, start_location[0], start_location[1])
    end_node = ox.nearest_nodes(graph, end_location[0], end_location[1])

    shortest_path = nx.shortest_path(graph, start_node, end_node, weight='travel_time')

    travel_time = nx.shortest_path_length(graph, start_node, end_node, weight='travel_time')
    # time = sum(ox.utils_graph.get_route_edge_attributes(graph, shortest_path, 'travel_time'))
    print(travel_time)

    # shortestRouteVisualize(graph, shortest_path, ax)

    return travel_time


def addAvgTime():
    df = pd.read_csv('../dataset/passengerRequests/request700.csv')
    df = df.head()
    # df = df[350:351]
    # df = pd.read_csv('../dataset/finalDF700.csv')
    # df = df[0:155]
    # print(df)

    graph = ox.graph_from_point((19.26542, 72.96664), dist=20000)

    graph = ox.add_edge_speeds(graph)
    graph = ox.add_edge_travel_times(graph)

    # print(ox.graph_to_gdfs(graph))

    shortest_travel_time_list = []
    iter = 0

    # fig, ax = ox.plot_graph(graph, node_size=0, show=False, close=False)

    for row in df.itertuples():
        try:
            travel_time = calcAvgTime(graph, row)
            # travel_time = calcAvgTime(graph, row, ax)
            shortest_travel_time_list.append(int(travel_time)/60)
            iter = iter+1
            print(iter)
        except:
            shortest_travel_time_list.append('NULL')
            iter = iter+1
            print(iter)
    # shortestRouteVisualize(graph, shortest_travel_time_list, ax)

    df['shortest_travel_time'] = shortest_travel_time_list
    df = df.drop(['Unnamed: 0'], axis=1)
    # print(df['Unnamed: 0'])

    df.to_csv('../dataset/request700.csv')
    # plt.show()


def shortestRouteVisualize(graph, shortest_path, ax):
    ox.plot_graph_route(graph, shortest_path, ax=ax, node_size=0, show=False, close=False)
    # s = gpd.GeoDataFrame([1,2], geometry=gpd.points_from_xy([72.85512807917517, 72.8559418653558],[19.31069864366639, 19.298457266753697]) )
    # ax.scatter(72.85512807917517,19.31069864366639, c='green')
    # ax.scatter(72.8559418653558,19.298457266753697, c='green')

    # plt.show()

# df = pd.read_csv('../dataset/finalDF700.csv')
# df = df[0:5]
# # print(df)

# graph = ox.graph_from_point((19.26542, 72.96664), dist=15000, network_type='drive')

# graph = ox.add_edge_speeds(graph)
# graph = ox.add_edge_travel_times(graph)

# print(ox.graph_to_gdfs(graph))

# df = pd.read_csv('../dataset/finalDF700.csv')

# for row in df.itertuples():
#     travel_time = calcAvgTime(row)

# fig, ax = plt.subplots()

# fig, ax = ox.plot_graph_route(graph, shortest_path, node_size=0, show=False, close=False)
# s = gpd.GeoDataFrame([1,2], geometry=gpd.points_from_xy([72.85512807917517, 72.8559418653558],[19.31069864366639, 19.298457266753697]) )
# ax.scatter(72.85512807917517,19.31069864366639, c='green')
# ax.scatter(72.8559418653558,19.298457266753697, c='green')

# plt.show()


__all__ = ["addAvgTime"]