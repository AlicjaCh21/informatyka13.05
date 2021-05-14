import geopandas 
import shapely
import numpy as np
import  matplotlib.pyplot  as  plt 

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
ax.axis("off")
#tu

merged = geopandas.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

cell.loc[dissolve.index, 'TOT'] = dissolve.TOT.values
plt.figure(2)
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
ax1 = gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_0_14', cmap='jet')
plt.autoscale(False)

cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax1.axis("on")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_0_14'] = dissolve.TOT_0_14.values
ax1 = cell.plot(column='TOT_0_14', figsize=(12, 8), cmap='viridis', edgecolor="grey", legend = True)
plt.autoscale(True)
ax1.set_axis_on()
plt.axis('equal')
plt.title('Liczba ludności w powiatach wiek 0-14')
