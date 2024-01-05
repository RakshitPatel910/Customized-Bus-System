import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import osmnx as ox
import geopandas as gpd
import numpy.random as rnd

data = pd.read_csv("dataset\ request700.csv")

data = data.loc[data['shortest_travel_time'] > 5]
print(len(data))



# Optional: Scale the data if features have different scales
# scaler = StandardScaler()
# data_scaled = scaler.fit_transform(data)

data = data.loc[data['shortest_travel_time'] > 5]

data = data[['start_lat', 'start_long']]
# data =
dbscan = DBSCAN(eps=0.5/6371., min_samples=10, algorithm='ball_tree', metric='haversine')



# Create a DBSCAN object with appropriate parameters
# dbscan = DBSCAN(eps=0.5, min_samples=10)  # Adjust eps and min_samples as needed

# Perform clustering
clusters = dbscan.fit_predict(np.radians(data))

# Analyze results
print("Cluster labels:", clusters)
data['clusterLabel1'] = clusters
# pickUpClusteredData = data
print(data.head(1000))


labels = clusters

# Count occurrences of each unique label
unique_labels, counts = np.unique(labels, return_counts=True)

# Print the counts for each cluster label
for label, count in zip(unique_labels, counts):
    print(f"Cluster {label}: {count} data points")


# Visualize clusters (optional, using dimensionality reduction)
# from sklearn.manifold import TSNE
# tsne = TSNE(n_components=2)
# data_2d = tsne.fit_transform(data)

# # Plot clusters in 2D space
# import matplotlib.pyplot as plt
# plt.scatter(data_2d[:, 0], data_2d[:, 1], c=clusters)
# plt.show()

unique_nodes = []

unique_start_nodes = []

# data = data.values.tolist()

for node in data[['start_lat', 'start_long']].values.tolist():
    if node in unique_nodes:
        unique_nodes.append([node[0]+rnd.normal(0,0.00005), node[1]+rnd.normal(0,0.00005)])
        unique_start_nodes.append([node[0]+rnd.normal(0,0.00005), node[1]+rnd.normal(0,0.00005)])
    else :
        unique_nodes.append(node)
        unique_start_nodes.append(node)
unique_start_nodes = pd.DataFrame(unique_start_nodes, columns=['start_lat', 'start_long'])
print(unique_start_nodes[0:5])

pickUpClusteredData = unique_start_nodes
pickUpClusteredData['clusterLabel1'] = clusters

passengerPickupNodes = gpd.GeoDataFrame(unique_start_nodes, crs='EPSG:4326', geometry=gpd.points_from_xy(unique_start_nodes['start_lat'], unique_start_nodes['start_long']))
print(passengerPickupNodes.head())

# res = ox.features_from_point( (19.295233, 72.854393), tags = { 'highway':True, 'building': True }, dist=15000 )
# residential_highway_gdf = gpd.GeoDataFrame.from_features(res, crs='EPSG:4326')

fig, ax = plt.subplots()

LABEL_COLOR_MAP = [
        "#000000", "#FFFF00", "#1CE6FF", "#FF34FF", "#FF4A46", "#008941", "#006FA6", "#A30059",
        "#FFDBE5", "#7A4900", "#0000A6", "#63FFAC", "#B79762", "#004D43", "#8FB0FF", "#997D87",
        "#5A0007", "#809693", "#FEFFE6", "#1B4400", "#4FC601", "#3B5DFF", "#4A3B53", "#FF2F80",
        "#61615A", "#BA0900", "#6B7900", "#00C2A0", "#FFAA92", "#FF90C9", "#B903AA", "#D16100",
        "#DDEFFF", "#000035", "#7B4F4B", "#A1C299", "#300018", "#0AA6D8", "#013349", "#00846F",
        "#372101", "#FFB500", "#C2FFED", "#A079BF", "#CC0744", "#C0B9B2", "#C2FF99", "#001E09",
        "#00489C", "#6F0062", "#0CBD66", "#EEC3FF", "#456D75", "#B77B68", "#7A87A1", "#788D66",
        "#885578", "#FAD09F", "#FF8A9A", "#D157A0", "#BEC459", "#456648", "#0086ED", "#886F4C",

        "#34362D", "#B4A8BD", "#00A6AA", "#452C2C", "#636375", "#A3C8C9", "#FF913F", "#938A81",
        "#575329", "#00FECF", "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00",
        "#7900D7", "#A77500", "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700",
        "#549E79", "#FFF69F", "#201625", "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329",
        "#5B4534", "#FDE8DC", "#404E55", "#0089A3", "#CB7E98", "#A4E804", "#324E72", "#6A3A4C",
        "#83AB58", "#001C1E", "#D1F7CE", "#004B28", "#C8D0F6", "#A3A489", "#806C66", "#222800",
        "#BF5650", "#E83000", "#66796D", "#DA007C", "#FF1A59", "#8ADBB4", "#1E0200", "#5B4E51", 
        "#C895C5", "#320033", "#FF6832", "#66E1D3", "#CFCDAC", "#D0AC94", "#7ED379", "#012C58"
]

label_color = [LABEL_COLOR_MAP[l] for l in clusters]

passengerPickupNodes.plot(ax=ax, color=label_color, marker='o', alpha=0.7, linewidth=0.5,)





# Load your dataset (replace with your data loading method)
data = pd.read_csv("dataset\ request700.csv")

# Optional: Scale the data if features have different scales
# scaler = StandardScaler()
# data_scaled = scaler.fit_transform(data)

data = data.loc[data['shortest_travel_time'] > 5]

data = data[['end_lat', 'end_long']]
dbscan = DBSCAN(eps=0.5/6371., min_samples=10, algorithm='ball_tree', metric='haversine')



# Create a DBSCAN object with appropriate parameters
# dbscan = DBSCAN(eps=0.5, min_samples=10)  # Adjust eps and min_samples as needed

# Perform clustering
clusters = dbscan.fit_predict(np.radians(data))

# Analyze results
print("Cluster labels:", clusters)
data['clusterLabel2'] = clusters
# dropClusteredData = data
print(data.head(1000))


labels = clusters

# Count occurrences of each unique label
unique_labels, counts = np.unique(labels, return_counts=True)

# Print the counts for each cluster label
for label, count in zip(unique_labels, counts):
    print(f"Cluster {label}: {count} data points")


# Visualize clusters (optional, using dimensionality reduction)
# from sklearn.manifold import TSNE
# tsne = TSNE(n_components=2)
# data_2d = tsne.fit_transform(data)

# # Plot clusters in 2D space
# import matplotlib.pyplot as plt
# plt.scatter(data_2d[:, 0], data_2d[:, 1], c=clusters)
# plt.show()

unique_nodes = []

unique_start_nodes2 = []

# data = data.values.tolist()

for node in data[['end_lat', 'end_long']].values.tolist():
    if node in unique_nodes:
        unique_nodes.append([node[0]+rnd.normal(0,0.00005), node[1]+rnd.normal(0,0.00005)])
        unique_start_nodes2.append([node[0]+rnd.normal(0,0.00005), node[1]+rnd.normal(0,0.00005)])
    else :
        unique_nodes.append(node)
        unique_start_nodes2.append(node)
unique_start_nodes2 = pd.DataFrame(unique_start_nodes2, columns=['end_lat', 'end_long'])
dropClusteredData = unique_start_nodes2
dropClusteredData['clusterLabel2'] = clusters
print(unique_start_nodes2[0:5])

passengerDropNodes = gpd.GeoDataFrame(unique_start_nodes2, crs='EPSG:4326', geometry=gpd.points_from_xy(unique_start_nodes2['end_lat'], unique_start_nodes2['end_long']))
print(passengerDropNodes.head())

# res = ox.features_from_point( (19.295233, 72.854393), tags = { 'highway':True, 'building': True }, dist=15000 )
# residential_highway_gdf = gpd.GeoDataFrame.from_features(res, crs='EPSG:4326')

fig, ax = plt.subplots()

LABEL_COLOR_MAP = [
        "#000000", "#FFFF00", "#1CE6FF", "#FF34FF", "#FF4A46", "#008941", "#006FA6", "#A30059",
        "#FFDBE5", "#7A4900", "#0000A6", "#63FFAC", "#B79762", "#004D43", "#8FB0FF", "#997D87",
        "#5A0007", "#809693", "#FEFFE6", "#1B4400", "#4FC601", "#3B5DFF", "#4A3B53", "#FF2F80",
        "#61615A", "#BA0900", "#6B7900", "#00C2A0", "#FFAA92", "#FF90C9", "#B903AA", "#D16100",
        "#DDEFFF", "#000035", "#7B4F4B", "#A1C299", "#300018", "#0AA6D8", "#013349", "#00846F",
        "#372101", "#FFB500", "#C2FFED", "#A079BF", "#CC0744", "#C0B9B2", "#C2FF99", "#001E09",
        "#00489C", "#6F0062", "#0CBD66", "#EEC3FF", "#456D75", "#B77B68", "#7A87A1", "#788D66",
        "#885578", "#FAD09F", "#FF8A9A", "#D157A0", "#BEC459", "#456648", "#0086ED", "#886F4C",

        "#34362D", "#B4A8BD", "#00A6AA", "#452C2C", "#636375", "#A3C8C9", "#FF913F", "#938A81",
        "#575329", "#00FECF", "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00",
        "#7900D7", "#A77500", "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700",
        "#549E79", "#FFF69F", "#201625", "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329",
        "#5B4534", "#FDE8DC", "#404E55", "#0089A3", "#CB7E98", "#A4E804", "#324E72", "#6A3A4C",
        "#83AB58", "#001C1E", "#D1F7CE", "#004B28", "#C8D0F6", "#A3A489", "#806C66", "#222800",
        "#BF5650", "#E83000", "#66796D", "#DA007C", "#FF1A59", "#8ADBB4", "#1E0200", "#5B4E51",
        "#C895C5", "#320033", "#FF6832", "#66E1D3", "#CFCDAC", "#D0AC94", "#7ED379", "#012C58"
]

label_color = [LABEL_COLOR_MAP[l] for l in clusters]

passengerDropNodes.plot(ax=ax, color=label_color, marker='o', alpha=0.7, linewidth=0.5,)

newData = pd.read_csv("dataset\ request700.csv")

newData = pd.concat([pickUpClusteredData, dropClusteredData], axis=1)

indexList = []
for i in range(0,len(newData)):
  indexList.append(i)

newData['index'] = indexList

print(newData[['clusterLabel1', 'clusterLabel2']])

dbscan = DBSCAN(eps=0.01, min_samples=10, algorithm='ball_tree', metric='euclidean')

# Create a DBSCAN object with appropriate parameters
# dbscan = DBSCAN(eps=0.5, min_samples=10)  # Adjust eps and min_samples as needed

# Perform clustering
clusters = dbscan.fit_predict(newData[['clusterLabel1', 'clusterLabel2']])
newData['clusterLabel3'] = clusters
newData = newData.sort_values('clusterLabel3')
print(newData.head())

labels = clusters

# Count occurrences of each unique label
unique_labels, counts = np.unique(labels, return_counts=True)

# Print the counts for each cluster label
for label, count in zip(unique_labels, counts):
    print(f"Cluster {label}: {count} data points")

# Analyze results
# print("Cluster labels:", clusters)
# data['clusterLabel'] = clusters
# dropClusteredData = data
# print(data.head(1000))

fig, ax = plt.subplots()

LABEL_COLOR_MAP = [
        "#000000", "#FFFF00", "#1CE6FF", "#FF34FF", "#FF4A46", "#008941", "#006FA6", "#A30059",
        "#FFDBE5", "#7A4900", "#0000A6", "#63FFAC", "#B79762", "#004D43", "#8FB0FF", "#997D87",
        "#5A0007", "#809693", "#FEFFE6", "#1B4400", "#4FC601", "#3B5DFF", "#4A3B53", "#FF2F80",
        "#61615A", "#BA0900", "#6B7900", "#00C2A0", "#FFAA92", "#FF90C9", "#B903AA", "#D16100",
        "#DDEFFF", "#000035", "#7B4F4B", "#A1C299", "#300018", "#0AA6D8", "#013349", "#00846F",
        "#372101", "#FFB500", "#C2FFED", "#A079BF", "#CC0744", "#C0B9B2", "#C2FF99", "#001E09",
        "#00489C", "#6F0062", "#0CBD66", "#EEC3FF", "#456D75", "#B77B68", "#7A87A1", "#788D66",
        "#885578", "#FAD09F", "#FF8A9A", "#D157A0", "#BEC459", "#456648", "#0086ED", "#886F4C",

        "#34362D", "#B4A8BD", "#00A6AA", "#452C2C", "#636375", "#A3C8C9", "#FF913F", "#938A81",
        "#575329", "#00FECF", "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00",
        "#7900D7", "#A77500", "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700",
        "#549E79", "#FFF69F", "#201625", "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329",
        "#5B4534", "#FDE8DC", "#404E55", "#0089A3", "#CB7E98", "#A4E804", "#324E72", "#6A3A4C",
        "#83AB58", "#001C1E", "#D1F7CE", "#004B28", "#C8D0F6", "#A3A489", "#806C66", "#222800",
        "#BF5650", "#E83000", "#66796D", "#DA007C", "#FF1A59", "#8ADBB4", "#1E0200", "#5B4E51",
        "#C895C5", "#320033", "#FF6832", "#66E1D3", "#CFCDAC", "#D0AC94", "#7ED379", "#012C58"
]

label_color = [LABEL_COLOR_MAP[l+20] for l in newData['clusterLabel3'].values.tolist()]
# label_color = [LABEL_COLOR_MAP[l+20] for l in clusters[clusters == 9]]

passengerDropNodes = gpd.GeoDataFrame(newData, crs='EPSG:4326', geometry=gpd.points_from_xy(newData['start_lat'], newData['start_long']))
passengerDropNodes1 = gpd.GeoDataFrame(newData, crs='EPSG:4326', geometry=gpd.points_from_xy(newData['end_lat'], newData['end_long']))

res = ox.features_from_point( (19.257118, 72.912941), tags = { 'highway':True }, dist=8000 )
residential_highway_gdf = gpd.GeoDataFrame.from_features(res, crs='EPSG:4326')


residential_highway_gdf.plot(ax=ax, color='lightblue',alpha = 0.7,linewidth=0.5,marker='None' )
# passengerDropNodes[5000:8000].plot(ax=ax, color=label_color, marker='o', alpha=0.7, linewidth=0.5,)
passengerDropNodes.loc[passengerDropNodes['clusterLabel3'] == 22].plot(ax=ax, color=label_color, marker='o', alpha=0.7, linewidth=0.5,)
# passengerDropNodes1[5000:8000].plot(ax=ax, color=label_color, marker='^', alpha=0.7, linewidth=0.5,)
passengerDropNodes1.loc[passengerDropNodes1['clusterLabel3'] == 22].plot(ax=ax, color=label_color, marker='^', alpha=0.7, linewidth=0.5,)



print(len(passengerDropNodes), len(passengerDropNodes1))

newData.to_csv('newData.csv')

data = newData
cluster_labels = data['clusterLabel3']

cluster_dict = {}
for cluster_label in cluster_labels.unique():
    cluster_dict[cluster_label] = data[data['clusterLabel3'] == cluster_label].values.tolist()


# points_in_cluster_3 = cluster_dict[3]

for cluster_label, points in cluster_dict.items():
    print(f"Data points in cluster {cluster_label}: {points}")
# print(cluster_dict[-1])