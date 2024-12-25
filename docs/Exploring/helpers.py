import geopandas as gpd
import pandas as pd
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

def unit_summary():
    housing_nm = gpd.read_file("../../data/local/housing_nm.gpkg")
    housing_abq = gpd.read_file("../../data/local/housing_abq.gpkg")
    housing_vtr = gpd.read_file("../../data/local/housing_vtr.gpkg")
    
    unit_summary = pd.DataFrame()
    unit_summary['Location'] = ['New Mexico', 'Albuquerque', 'VTR']

    unit_summary['Total'] = [
        housing_nm.HOUSING_UN.sum(), 
    housing_abq.HOUSING_UN.sum(), 
    housing_vtr.HOUSING_UN.sum()
    ] 
    unit_summary['Owned'] = [
        housing_nm.OWNED.sum(), 
        housing_abq.OWNED.sum(), 
        housing_vtr.OWNED.sum()
    ]
    unit_summary['Rented'] = [
        housing_nm.RENTED.sum(), 
        housing_abq.RENTED.sum(), 
        housing_vtr.RENTED.sum()
    ]
    unit_summary['Occupied'] = [
        housing_nm.OCC_HU.sum(), 
        housing_abq.OCC_HU.sum(), 
        housing_vtr.OCC_HU.sum()
    ]
    unit_summary['Vacant'] = [
        housing_nm.VAC_HU.sum(), 
        housing_abq.VAC_HU.sum(), 
        housing_vtr.VAC_HU.sum()
    ]
    unit_summary["Ownership_est"] = [
        housing_nm.OWNED_P.mean(), 
        housing_abq.OWNED_P.mean(), 
        housing_vtr.OWNED_P.mean()
    ]
    unit_summary["Available"] = [
        housing_nm.AVAILABILITY.mean(), 
        housing_abq.AVAILABILITY.mean(), 
        housing_vtr.AVAILABILITY.mean()
    ]
    return unit_summary