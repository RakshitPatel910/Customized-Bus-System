import pandas as pd 
import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gpd 
import random

df = pd.read_csv('D:\MajorProject\Customized-Bus-System\dataset\plotForm.csv')
print(df)

for i in df.itertuples():
    print(i.from_lat)
    print(i.from_long)
    res = ox.features_from_point( (i.from_lat, i.from_long), tags = {'building': True}, dist=200 )
    from_polygons_list = []
    for j in res['geometry']:
        from_polygons_list.append(j)
    if(i.total_passenger < len(from_polygons_list)):
        print(len(random.sample(from_polygons_list, i.total_passenger)))
    else:
        quotient = i.total_passenger/len(from_polygons_list)
        remainder = i.total_passenger%len(from_polygons_list)
        print(len(random.sample(from_polygons_list, remainder)))
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
