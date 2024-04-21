# This is an example use of the script.

from terrain_model_helper import GeoTiffToEsriGrid

# Replace src and dst with you file locations
src = "/home/marcin/model_terenu/jaxa_data/gory_swietokrzyskie/SE_ALPSMLC30_N050E021_DSM.tif"
dst = "/home/marcin/model_terenu/jaxa_data/gory_swietokrzyskie/swietokrz_SE.asc"

GeoTiffToEsriGrid(src, dst, True).convert()
