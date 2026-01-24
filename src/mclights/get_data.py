from pathlib import Path
import geopandas as gpd
import osmnx as ox
from loguru import logger
import os


ox.settings.use_cache = True
project_dir = Path(os.getcwd()).parent.parent
ox.settings.cache_folder = project_dir / "cache"


def get_data_osmx_or_local(file_path: Path, tags: dict, place: str = "Poland") -> gpd.GeoDataFrame:    
    if file_path.exists():
        logger.info(f"File {file_path} does exists, reading the file...")
        return gpd.read_file(file_path, layer=file_path.stem)
    else:
        logger.info(f"File {file_path} does not exitst, getting data from Open Street Maps, it may take a while...")
        gdf = ox.features_from_place(place, tags=tags).reset_index()
        gdf = gdf.to_crs(epsg=2180)
        
        logger.info(f"Saving data to the {file_path}.")
        gdf.to_file(file_path, layer=file_path.stem, driver="GPKG")

        return gdf
