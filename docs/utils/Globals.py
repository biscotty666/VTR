import geopandas as gpd

DATA_PATH = "../../data/"
abq_shp = gpd.read_file(DATA_PATH + "local/abq_shp.gpkg")
vtr_shp = gpd.read_file(DATA_PATH + "local/vtr_shp.gpkg")
