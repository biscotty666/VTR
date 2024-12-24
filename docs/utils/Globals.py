import geopandas as gpd

DATA_PATH = "../../data/"
abq_shp = gpd.read_file(DATA_PATH + "local/abq_base.shp")
vtr_shp = gpd.read_file(DATA_PATH + "shp/vtr_shp.gpkg")