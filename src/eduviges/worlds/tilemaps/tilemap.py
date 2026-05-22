from pathlib import Path

import pygame

from eduviges.rendering.camera import Camera
from eduviges.worlds.loaders.tiled_loader import TiledLoader
from eduviges.worlds.tilemaps.tile import Tile


TILE_DEFINITIONS = {
    0: {
        "sprite": "forest.png",
        "walkable": True,
        "color": (25, 35, 30),
    },
    1: {
        "sprite": "grass.png",
        "walkable": True,
        "color": (72, 132, 72),
    },
    2: {
        "sprite": "forest.png",
        "walkable": False,
        "color": (70, 52, 36),
    },
    3: {
        "sprite": "water.png",
        "walkable": False,
        "color": (45, 105, 150),
    },
    4: {
        "sprite": "path.png",
        "walkable": True,
        "color": (160, 125, 75),
    },
    5: {
        "sprite": "plaza.png",
        "walkable": True,
        "color": (185, 145, 85),
    },
    6: {
        "sprite": "bohio.png",
        "walkable": False,
        "color": (120, 82, 46),
    },
}


class TileMap:
    def __init__(
        self,
        data: list[list[int]],
        tile_size: int = 32,
    ) -> None:
        self.data = data
        self.tile_size = tile_size

        self.sprite_cache = self._load_tile_sprites()

        self.tiles: list[Tile] = self._build_tiles(data)

    @classmethod
    def from_tiled_json(
        cls,
        relative_path: str,
        layer_name: str = "ground",
    ) -> "TileMap":
        loader = TiledLoader()

        data, tile_size = loader.load_tile_layer(
            relative_path,
            layer_name,
        )

        return cls(
            data=data,
            tile_size=tile_size,
        )

    def _load_tile_sprites(
        self,
    ) -> dict[str, pygame.Surface]:
        sprite_dir = Path(
            "assets/sprites/tiles"
        )

        cache: dict[str, pygame.Surface] = {}

        for definition in TILE_DEFINITIONS.values():
            sprite_name = definition["sprite"]

            if sprite_name in cache:
                continue

            path = sprite_dir / sprite_name

            sprite = pygame.image.load(
                str(path)
            )

            if pygame.display.get_init():
                sprite = sprite.convert()

            sprite = pygame.transform.scale(
                sprite,
                (
                    self.tile_size,
                    self.tile_size,
                ),
            )

            cache[sprite_name] = sprite

        return cache

    def _build_tiles(
        self,
        data: list[list[int]],
    ) -> list[Tile]:
        return [
            self._create_tile(x, y, value)
            for y, row in enumerate(data)
            for x, value in enumerate(row)
        ]

    def _create_tile(
        self,
        x: int,
        y: int,
        value: int,
    ) -> Tile:
        definition = TILE_DEFINITIONS.get(
            value,
            TILE_DEFINITIONS[0],
        )

        sprite_name = definition["sprite"]

        return Tile(
            grid_x=x,
            grid_y=y,
            size=self.tile_size,
            color=definition["color"],
            walkable=definition["walkable"],
            sprite=self.sprite_cache[
                sprite_name
            ],
        )

    def render(
        self,
        screen: pygame.Surface,
        camera: Camera | None = None,
    ) -> None:
        for tile in self.tiles:
            tile.render(screen, camera)

    @property
    def collision_rects(
        self,
    ) -> list[pygame.Rect]:
        return [
            tile.rect
            for tile in self.tiles
            if not tile.walkable
        ]

    @property
    def width(self) -> int:
        if not self.data:
            return 0

        return (
            len(self.data[0])
            * self.tile_size
        )

    @property
    def height(self) -> int:
        return (
            len(self.data)
            * self.tile_size
        )

    def get_tile_at_grid(
        self,
        grid_x: int,
        grid_y: int,
    ) -> Tile | None:
        for tile in self.tiles:
            if (
                tile.grid_x == grid_x
                and tile.grid_y == grid_y
            ):
                return tile

        return None
