import pygame

from eduviges.worlds.tilemaps.tile import Tile


class TileMap:
    def __init__(
        self,
        data: list[list[int]],
        tile_size: int = 32,
    ) -> None:
        self.data = data
        self.tile_size = tile_size
        self.tiles: list[Tile] = self._build_tiles(data)

    def _build_tiles(self, data: list[list[int]]) -> list[Tile]:
        tiles: list[Tile] = []

        for y, row in enumerate(data):
            for x, value in enumerate(row):
                tile = self._create_tile(x, y, value)
                tiles.append(tile)

        return tiles

    def _create_tile(self, x: int, y: int, value: int) -> Tile:
        if value == 1:
            return Tile(
                grid_x=x,
                grid_y=y,
                size=self.tile_size,
                color=(70, 120, 70),
                walkable=True,
            )

        if value == 2:
            return Tile(
                grid_x=x,
                grid_y=y,
                size=self.tile_size,
                color=(90, 70, 50),
                walkable=False,
            )

        return Tile(
            grid_x=x,
            grid_y=y,
            size=self.tile_size,
            color=(35, 35, 45),
            walkable=True,
        )

    def render(self, screen: pygame.Surface) -> None:
        for tile in self.tiles:
            tile.render(screen)

    @property
    def collision_rects(self) -> list[pygame.Rect]:
        return [
            tile.rect
            for tile in self.tiles
            if not tile.walkable
        ]

    @property
    def width(self) -> int:
        if not self.data:
            return 0

        return len(self.data[0]) * self.tile_size

    @property
    def height(self) -> int:
        return len(self.data) * self.tile_size

    def get_tile_at_grid(
        self,
        grid_x: int,
        grid_y: int,
    ) -> Tile | None:
        for tile in self.tiles:
            if tile.grid_x == grid_x and tile.grid_y == grid_y:
                return tile

        return None
