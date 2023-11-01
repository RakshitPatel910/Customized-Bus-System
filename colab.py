import osmnx as ox

G = ox.graph_from_place("Mumbai, Maharashtra, India", network_type="drive")
fig, ax = ox.plot_graph(G)

gdf_nodes, gdf_relationships = ox.graph_to_gdfs(G)
gdf_nodes.reset_index(inplace=True)
gdf_relationships.reset_index(inplace=True)
print(gdf_nodes)
print(gdf_relationships)

import matplotlib.pyplot as plt
import geopandas as gpd 


residential_areas = ox.geometries_from_place("Mumbai, Maharashtra, India", tags={'landuse': 'residential'})
gfd = gpd.GeoDataFrame(residential_areas)

fig, ax = plt.subplots()

# Plot the residential areas
gfd.plot(ax=ax, color='lightblue', alpha=0.7, linewidth=0.5, edgecolor='k')

# Set a title
ax.set_title("Residential Areas")

# Remove axis labels
ax.set_axis_off()

# Display the plot
plt.show()


res = ox.features_from_point( (19.275002, 72.861955), tags = {'building': True, 'highway':True}, dist=200 )

print(res)

gfd = gpd.GeoDataFrame(res)

fig, ax = plt.subplots()

# Plot the residential areas
gfd.plot(ax=ax, color='lightblue', alpha=0.7, linewidth=0.5, edgecolor='k')

# Set a title
ax.set_title("Residential Areas")

# Remove axis labels
ax.set_axis_off()

# Display the plot
plt.show()


import pandas as pd

# df = pd.read_csv('Data Excel.xlsx - Route Latlong.csv')

# df.head()


# newData = []
# columns = ['name', 'stop no.', 'lat', 'long']


# for frame in df.iterrows():
#   if(frame[1][0] == 'UP'):
#     if [frame[1][2], frame[1][5], frame[1][7], frame[1][8]] not in newData:
#       newData.append([frame[1][2].lower(), frame[1][5], frame[1][7], frame[1][8]])
#     # print(frame[1][2])

# # len(newData)

# newDF = pd.DataFrame(newData, columns = columns)
# newDF

# newDF.to_csv('interDF.csv', index=False)



# r700 = pd.read_csv('700.csv')
# finalData = []

# for row in r700.iterrows():
#   print(newDF[newDF['name'] == row[1][1].lower()])
#   # for i in newDF.iterrows():
#     # print(i[1][0], row[1][1])    

#     # if(i[1][0].lower() == row[1][1].lower()):
#     #   print([row[1], i[1][2], i[1][3]])
#     #   finalData.append([row[1], i[1][2], i[1][3]])

#   # print(row[1][1])
#   # value = newDF[newDF['name']==row[1][1]]
#   # print(value)
#   # newDF[row['from_stop_name'][0]]
#     # finalData.append([row, ])
# # len(finalData)



