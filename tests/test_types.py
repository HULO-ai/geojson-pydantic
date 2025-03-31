import pytest

from geojson_pydantic.types import Position2D, Position3D


@pytest.mark.parametrize("coordinates", [(1, 2), (1.0, 2.0), (1.01, 2.01)])
def test_position2d_valid_coordinates(coordinates):
    """
    Two number elements as coordinates should be okay
    """
    p = Position2D(longitude=coordinates[0], latitude=coordinates[1])
    assert p[0] == coordinates[0]
    assert p[1] == coordinates[1]
    assert p.longitude == coordinates[0]
    assert p.latitude == coordinates[1]
    assert p == coordinates

    p = Position2D(*coordinates)
    assert p[0] == coordinates[0]
    assert p[1] == coordinates[1]
    assert p.longitude == coordinates[0]
    assert p.latitude == coordinates[1]
    assert p == coordinates


@pytest.mark.parametrize(
    "coordinates", [(1, 2, 3), (1.0, 2.0, 3.0), (1.01, 2.01, 3.01)]
)
def test_position3d_valid_coordinates(coordinates):
    """
    Three number elements as coordinates should be okay
    """
    p = Position3D(
        longitude=coordinates[0], latitude=coordinates[1], altitude=coordinates[2]
    )
    assert p[0] == coordinates[0]
    assert p[1] == coordinates[1]
    assert p[2] == coordinates[2]
    assert p.longitude == coordinates[0]
    assert p.latitude == coordinates[1]
    assert p.altitude == coordinates[2]
    assert p == coordinates

    p = Position3D(*coordinates)
    assert p[0] == coordinates[0]
    assert p[1] == coordinates[1]
    assert p[2] == coordinates[2]
    assert p.longitude == coordinates[0]
    assert p.latitude == coordinates[1]
    assert p.altitude == coordinates[2]


@pytest.mark.parametrize(
    "coordinates", [(-181, 0, 0), (181, 0, 0), (-200, 0, 0), (200, 0, 0)]
)
def test_position3d_invalid_longitude(coordinates):
    """
    Longitude outside of -180 to 180 degrees should raise a validation error
    """
    Position3D(
        longitude=coordinates[0],
        latitude=coordinates[1],
        altitude=coordinates[2],
    )
