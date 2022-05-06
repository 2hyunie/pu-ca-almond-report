import geopandas as gpd
import pandas as pd

gdf = gpd.read_file('/Users/shen/Desktop/01Spring_2022/Points Unknown/Assignment8/extra/almonds_map.geojson')

gdf_kern = gdf[gdf.COUNTY == 'Kern']

gdf_kern['ACRES'] = gdf_kern['ACRES'].apply(pd.to_numeric)

gdf_kern.to_file('/Users/shen/Desktop/01Spring_2022/Points Unknown/almond_kern.geojson')