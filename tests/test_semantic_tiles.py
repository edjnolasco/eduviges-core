from eduviges.worlds.tilemaps.tilemap import TILE_DEFINITIONS, TileMap


def test_semantic_tile_definitions_include_taino_village_tiles():
    for tile_id in [0, 1, 2, 3, 4, 5, 6]:
        assert tile_id in TILE_DEFINITIONS


def test_water_tile_is_not_walkable():
    tilemap = TileMap(data=[[3]], tile_size=48)

    tile = tilemap.get_tile_at_grid(0, 0)

    assert tile is not None
    assert not tile.walkable


def test_path_tile_is_walkable():
    tilemap = TileMap(data=[[4]], tile_size=48)

    tile = tilemap.get_tile_at_grid(0, 0)

    assert tile is not None
    assert tile.walkable


def test_bohio_tile_is_not_walkable():
    tilemap = TileMap(data=[[6]], tile_size=48)

    tile = tilemap.get_tile_at_grid(0, 0)

    assert tile is not None
    assert not tile.walkable
