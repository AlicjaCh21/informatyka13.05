import geopandas 
import shapely
import numpy as np
import  matplotlib.pyplot  as  plt 
import pandas as pd
import math as m

gdf = geopandas.read_file('PD_STAT_GRID_CELL_2011.shp')

gdf.to_crs("EPSG:4326")
gdf['centroid'] = gdf.centroid

#
xmin, ymin, xmax, ymax=  [13 ,48 , 25, 56]
#
n_cells=30
cell_size = (xmax-xmin)/n_cells
#
grid_cells = []
for x0 in np.arange(xmin, xmax+cell_size, cell_size ):
    for y0 in np.arange(ymin, ymax+cell_size, cell_size):
         #bounds
         x1 = x0-cell_size
         y1 = y0+cell_size
         grid_cells.append( shapely.geometry.box(x0, y0, x1, y1))
cell = geopandas.GeoDataFrame(grid_cells, columns=['geometry'])
ax = gdf.plot(markersize=.1, figsize=(12, 8), column='TOT', cmap='jet')
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
#tu
plt.figure(2)
merged = geopandas.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT'] = dissolve.TOT.values

ax = cell.plot(column='TOT', figsize=(12, 8), cmap='viridis', vmax = 700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal')
plt.title('liczba ludności w siatce')

# liczba ludnosci w wieku 0-14
plt.figure(3)
pwt = geopandas.read_file('Powiaty.shp')
pwt = pwt.to_crs("EPSG:4326")
pwt.plot(legend=True)
cell = geopandas.GeoDataFrame(pwt, columns=['geometry'])
ax = gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_0_14', cmap='jet')
plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_0_14'] = dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_0_14', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal')
plt.title('Liczba ludności w powiatach wiek 0-14')

#liczba ludnosci w wieku 15-64
plt.figure(4)
ax = gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_15_64', cmap='jet')
plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_15_64'] = dissolve.TOT_15_64.values
ax = cell.plot(column='TOT_15_64', figsize=(12, 8), cmap='viridis', edgecolor="red", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal')
plt.title('Liczba ludności w powiatach wiek 15-64')

#liczba ludnosci w wieku 65+
plt.figure(5)
ax = gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_65__', cmap='jet')
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_65__'] = dissolve.TOT_65__.values
ax = cell.plot(column='TOT_65__', figsize=(12, 8), cmap='viridis', edgecolor="green", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal')
plt.title('Liczba ludności w powiatach wiek 65+')

#mezczyzni 0-14
plt.figure(6)
ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_MALE_0_14', cmap='jet')
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_MALE_0_14'] = dissolve.TOT_MALE_0_14.values
ax = cell.plot(column='TOT_MALE_0_14', figsize=(12, 8), cmap='viridis', edgecolor="blue", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('Liczba mężczyzn w wieku 0-14')

#mezczyzni 15-64
plt.figure(7)
ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_MALE_15_64', cmap='jet')
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_MALE_15_64'] = dissolve.TOT_MALE_15_64.values
ax = cell.plot(column='TOT_MALE_15_64', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('Liczba mężczyzn w wieku 15-64')

#mezczyzni 65+
plt.figure(8)
ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_MALE_65__', cmap='jet')
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_MALE_65__'] = dissolve.TOT_MALE_65__.values
ax = cell.plot(column='TOT_MALE_65__', figsize=(12, 8), cmap='viridis', edgecolor="green", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal');
plt.title('Liczba mężczyzn w wieku 65+')

#kobiety 0-14
ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_FEM_0_14', cmap='jet')
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_FEM_0_14'] = dissolve.TOT_FEM_0_14.values
ax = cell.plot(column='TOT_FEM_0_14', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal')
plt.title('Liczba kobiet w wieku 0-14')

#kobiety 15-64
ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_FEM_15_64', cmap='jet')
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_FEM_15_64'] = dissolve.TOT_FEM_15_64.values
ax = cell.plot(column='TOT_FEM_15_64', figsize=(12, 8), cmap='viridis', edgecolor="red", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal')
plt.title('Liczba kobiet w wieku 15-64')

#kobiety 65+
ax=gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_FEM_65__', cmap='jet')
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_FEM_65__'] = dissolve.TOT_FEM_65__.values
ax = cell.plot(column='TOT_FEM_65__', figsize=(12, 8), cmap='viridis', edgecolor="blue", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal')
plt.title('Liczba kobiet w wieku 65+')


#Ratio
woj=geopandas.read_file('Województwa.shp')
woj=woj.to_crs("EPSG:4326")
woj.plot(legend=True)
cell = geopandas.GeoDataFrame(woj, columns=['geometry'])
ax=gdf.plot(markersize=.1, figsize=(12, 8), column='FEM_RATIO', cmap='jet')
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = gpd.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'FEM_RATIO'] = dissolve.FEM_RATIO.values
ax = cell.plot(column='FEM_RATIO', figsize=(12, 8), cmap='viridis', edgecolor="black", legend = True)
plt.autoscale(True)
ax.set_axis_on()
plt.axis('equal')
plt.title('Ratio kobiet w województwach')










