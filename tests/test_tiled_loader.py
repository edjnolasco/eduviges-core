import json
from pathlib import Path

import pytest

from eduviges.worlds.loaders.tiled_loader import TiledLoader


def test_tiled_loader_loads_tile_layer(tmp_path: Path):
    map_path = tmp_path / "map.json"
    map_path.write_text(
        json.dumps(
            {
                "tilewidth": 32,
                "tileheight": 32,
                "layers": [
                    {
                        "name": "ground",
                        "type": "tilelayer",
                        "width": 2,
                        "height": 2,
                        "data": [1, 2, 0, 1],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    loader = TiledLoader(base_path=tmp_path)

    data, tile_size = loader.load_tile_layer("map.json")

    assert tile_size == 32
    assert data == [
        [1, 2],
        [0, 1],
    ]


def test_tiled_loader_raises_for_missing_map(tmp_path: Path):
    loader = TiledLoader(base_path=tmp_path)

    with pytest.raises(FileNotFoundError):
        loader.load_tile_layer("missing.json")


def test_tiled_loader_raises_for_missing_layer(tmp_path: Path):
    map_path = tmp_path / "map.json"
    map_path.write_text(
        json.dumps(
            {
                "tilewidth": 32,
                "layers": [
                    {
                        "name": "objects",
                        "type": "objectgroup",
                        "width": 1,
                        "height": 1,
                        "data": [],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    loader = TiledLoader(base_path=tmp_path)

    with pytest.raises(ValueError):
        loader.load_tile_layer("map.json", layer_name="ground")
