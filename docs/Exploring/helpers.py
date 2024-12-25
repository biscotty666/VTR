import geopandas as gpd
from shapely.geometry import box, Point
from contextily import Place
import contextily as ctx
import numpy as np
from matplotlib import pyplot as plt

def reg_plot(data, column, scheme, title,
             xlim=(-106.75,-106.45), 
             ylim=(35.025,35.225),
             alpha=0.3,
             names=True):
    pois = gpd.read_file("../../data/local/poi.gpkg")
    rois = gpd.read_file("../../data/local/rois.gpkg")
    ax = data.plot(
        figsize=(12,12),
        column=column,
        cmap='viridis',
        legend=True, 
        scheme=scheme, 
        alpha=alpha
    )
    rois.plot(ax=ax, color='red')
    pois.plot(ax=ax, markersize=30, color='red')
    if names:
        texts = []
        for x, y, label in zip(pois.geometry.x, pois.geometry.y, pois['name']): 
            if x > xlim[0] and x < xlim[1] and y > ylim[0] and y < ylim[1]:
                texts.append(plt.text(x, y+.002, label, fontsize=12, color='purple'))
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    plt.title(title, fontsize=20)
    ctx.add_basemap(ax, crs=data.crs, source=ctx.providers.Esri.WorldStreetMap)