import pygame

from eduviges.rendering.camera import Camera
from eduviges.worlds.loaders.tiled_loader import TiledLoader
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

    @classmethod
    def from_tiled_json(
        cls,
        relative_path: str,
        layer_name: str = "ground",
    ) -> "TileMap":
        loader = TiledLoader()
        data, tile_size = loader.load_tile_layer(
            relative_path=relative_path,
            layer_name=layer_name,
        )

        return cls(data=data, tile_size=tile_size)

    def _build_tiles(self, data: list[list[int]]) -> list[Tile]:
        tiles: list[Tile] = []

        for y, row in enumerate(data):
            for x, value in enumerate(row):
                tiles.append(self._create_tile(x, y, value))

        return tiles

    def _create_tile(self, x: int, y: int, value: int) -> Tile:
        if value == 1:
            return Tile(x, y, self.tile_size, (70, 120, 70), walkable=True)

        if value == 2:
            return Tile(x, y, self.tile_size, (90, 70, 50), walkable=False)

        return Tile(x, y, self.tile_size, (35, 35, 45), walkable=True)

    def render(self, screen: pygame.Surface, camera: Camera | None = None) -> None:
        for tile in self.tiles:
            tile.render(screen, camera)

    @property
    def collision_rects(self) -> list[pygame.Rect]:
        return [tile.rect for tile in self.tiles if not tile.walkable]

    @property
    def width(self) -> int:
        if not self.data:
            return 0

        return len(self.data[0]) * self.tile_size

    @property
    def height(self) -> int:
        return len(self.data) * self.tile_size

    def get_tile_at_grid(self, grid_x: int, grid_y: int) -> Tile | None:
        for tile in self.tiles:
            if tile.grid_x == grid_x and tile.grid_y == grid_y:
                return tile

        return None
