import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gpd 
# fig, ax = plt.subplots()


# residential_areas = ox.graph_from_bbox(19.3196,19.0826,73.0711,72.6639, tags={'landuse': 'residential'})
res = ox.features_from_point( (19.295233, 72.854393), tags = { 'highway':True}, dist=20000 )
# res = ox.graph_from_point( (19.275002, 72.861955),  dist=200 )

print(res)

gfd = gpd.GeoDataFrame(res)

fig, ax = plt.subplots()

# Plot the residential areas
gfd.plot(ax=ax, color='lightblue', alpha=0.7, linewidth=0.5, edgecolor='k')
# ox.plot_graph(res, node_color='gray', node_size=5, edge_color='white', edge_alpha=0.5)
# ox.plot_graph(res, node_color='gray', node_size=5, edge_color='white', edge_alpha=0.5)
# Set a title
# ax.set_title("Residential Areas")

# Remove axis labels
ax.set_axis_off()

# Display the plot
plt.show()