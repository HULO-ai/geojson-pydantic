"""Types for geojson_pydantic models"""

from typing import List, NamedTuple, Tuple, Union

from pydantic import Field
from typing_extensions import Annotated

BBox = Union[
    Tuple[float, float, float, float],  # 2D bbox
    Tuple[float, float, float, float, float, float],  # 3D bbox
]

Longitude = Annotated[
    Union[float, int],
    Field(
        title="Coordinate longitude",
        ge=-180,
        le=180,
    ),
]

Latitude = Annotated[
    Union[float, int],
    Field(
        title="Coordinate latitude",
        ge=-90,
        le=90,
    ),
]


class Position2D(NamedTuple):
    """Position without altitude"""

    longitude: Longitude
    latitude: Latitude


class Position3D(NamedTuple):
    """Position with altitude"""

    longitude: Longitude
    latitude: Latitude
    altitude: float


Position = Union[Position2D, Position3D]

# Coordinate arrays
LineStringCoords = Annotated[List[Position], Field(min_length=2)]
LinearRing = Annotated[List[Position], Field(min_length=4)]
MultiPointCoords = List[Position]
MultiLineStringCoords = List[LineStringCoords]
PolygonCoords = List[LinearRing]
MultiPolygonCoords = List[PolygonCoords]
