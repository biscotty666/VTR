import geopandas as gpd

DATA_PATH = "../../data/"
VTR_BB_COORDS = [
         (-106.741404, 35.132374),
         (-106.741404, 35.177111),
         (-106.671340, 35.177111),
         (-106.671340, 35.132374),
]

ABQ_BB_COORDS = [
         (-106.751404, 35.024374),
         (-106.751404, 35.227111),
         (-106.451340, 35.227111),
         (-106.451340, 35.024374),
]


abq_shp = gpd.read_file(DATA_PATH + "local/abq_shp.gpkg")
vtr_shp = gpd.read_file(DATA_PATH + "local/vtr_shp.gpkg")

def add_pois(ax):
    pois = gpd.read_file("../../data/local/poi.gpkg")
    pois.plot(ax=ax, markersize=4, color='red')
    texts = []
    for x, y, label in zip(pois.geometry.x, pois.geometry.y, pois['name']): 
        texts.append(plt.text(x, y, label, fontsize=9))

def poi_add(ax):
    pois = gpd.read_file("../../data/local/poi.gpkg")
    pois.plot(ax=ax, markersize=4, color='red')
    texts = []
    for x, y, label in zip(pois.geometry.x, pois.geometry.y, pois['name']): 
        texts.append(plt.text(x, y, label, fontsize=9))