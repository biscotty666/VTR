import geopandas as gpd

from typing import TypeVar
GeoDF = TypeVar('geopandas.geodataframe.GeoDataFrame')
DATA_PATH = "../../data/"
abq_shp = gpd.read_file(DATA_PATH + "local/abq_base.shp")

def extractOverlay(path_in: str, path_out: str, 
                   overlay: GeoDF = abq_shp, 
                   save_full: str = None
                  ) -> GeoDF:
    """ 
    Applies an overlay to a dataset, saves as gpkg, returns the frame
    """
    name = gpd.read_file(DATA_PATH + path_in)

    assert name.crs == overlay.crs, "CRS don't match"

    overlaid = name.overlay(
        overlay,
        how="intersection"
    )
    overlaid.drop('FID', axis=1, inplace=True)

    print(f"{overlaid.shape=}")
    print(f"{name.shape=}")
    overlaid.to_file(DATA_PATH + path_out, 
                 driver='GPKG', layer='base')

    if save_full:
        name.to_file(DATA_PATH + save_full, 
                 driver='GPKG', layer='base')


    return name