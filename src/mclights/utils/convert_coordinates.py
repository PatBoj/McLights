from shapely.geometry import Point, Polygon, MultiPolygon


def get_xy_coordinates(geometry: Point | Polygon | MultiPolygon | None) -> tuple[float, float] | None:
    """Extract x and y coordinates (longitude, latitude) from a Shapely geometry.

    - If the geometry is a Point, its coordinates are returned directly.
    - If the geometry is a Polygon or MultiPolygon, the centroid coordinates are returned.
    - If the geometry is None or unsupported, None is returned.

    Args:
        geometry: A Shapely Point, Polygon, MultiPolygon, or None.

    Returns:
        A tuple of (x, y) coordinates representing longitude and latitude, or None if the input geometry is None.
    """
    if geometry is None:
        return None

    if isinstance(geometry, Point):
        return geometry.x, geometry.y

    if isinstance(geometry, (Polygon, MultiPolygon)):
        centroid = geometry.centroid
        return centroid.x, centroid.y

    return None


from shapely.geometry import Point, Polygon, MultiPolygon


def convert_to_points(geometry: Point | Polygon | MultiPolygon | None) -> Point | None:
    """Convert a Shapely geometry into a Point.

    - If the geometry is already a Point, it is returned unchanged.
    - If the geometry is a Polygon or MultiPolygon, a Point representing the centroid is returned.
    - If the geometry is None, None is returned.

    Args:
        geometry: A Shapely Point, Polygon, MultiPolygon, or None.

    Returns:
        A Shapely Point representing the geometry location, or None if the input geometry is None.
    """
    if geometry is None:
        return None

    if isinstance(geometry, Point):
        return geometry

    if isinstance(geometry, (Polygon, MultiPolygon)):
        return geometry.centroid

    return None
