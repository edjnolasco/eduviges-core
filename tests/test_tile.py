from eduviges.worlds.tilemaps.tile import Tile


def test_tile_has_grid_position_and_rect():
    tile = Tile(
        grid_x=2,
        grid_y=3,
        size=32,
        color=(255, 255, 255),
    )

    assert tile.grid_x == 2
    assert tile.grid_y == 3
    assert tile.rect.x == 64
    assert tile.rect.y == 96
    assert tile.rect.width == 32
    assert tile.rect.height == 32


def test_tile_can_be_non_walkable():
    tile = Tile(
        grid_x=0,
        grid_y=0,
        size=32,
        color=(255, 255, 255),
        walkable=False,
    )

    assert not tile.walkable
