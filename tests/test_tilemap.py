from eduviges.worlds.tilemaps.tilemap import TileMap


def test_tilemap_builds_tiles_from_data():
    tilemap = TileMap(
        data=[
            [1, 1],
            [1, 2],
        ],
        tile_size=32,
    )

    assert len(tilemap.tiles) == 4


def test_tilemap_calculates_width_and_height():
    tilemap = TileMap(
        data=[
            [1, 1, 1],
            [1, 1, 1],
        ],
        tile_size=32,
    )

    assert tilemap.width == 96
    assert tilemap.height == 64


def test_tilemap_gets_tile_at_grid_position():
    tilemap = TileMap(
        data=[
            [1, 2],
        ],
        tile_size=32,
    )

    tile = tilemap.get_tile_at_grid(1, 0)

    assert tile is not None
    assert tile.grid_x == 1
    assert tile.grid_y == 0
    assert not tile.walkable


def test_tilemap_returns_none_for_missing_grid_position():
    tilemap = TileMap(
        data=[
            [1],
        ],
        tile_size=32,
    )

    assert tilemap.get_tile_at_grid(99, 99) is None
