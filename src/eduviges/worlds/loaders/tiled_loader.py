import json
from pathlib import Path


class TiledLoader:
    def __init__(self, base_path: str | Path = "assets/maps") -> None:
        self.base_path = Path(base_path)

    def load_tile_layer(
        self,
        relative_path: str,
        layer_name: str = "ground",
    ) -> tuple[list[list[int]], int]:
        path = self.base_path / relative_path

        if not path.exists():
            raise FileNotFoundError(f"Tiled map not found: {path}")

        with path.open("r", encoding="utf-8") as file:
            map_data = json.load(file)

        tile_width = int(map_data["tilewidth"])

        for layer in map_data.get("layers", []):
            if layer.get("name") == layer_name and layer.get("type") == "tilelayer":
                width = int(layer["width"])
                raw_data = layer["data"]

                return self._to_matrix(raw_data, width), tile_width

        raise ValueError(f"Tile layer not found: {layer_name}")

    def _to_matrix(
        self,
        raw_data: list[int],
        width: int,
    ) -> list[list[int]]:
        return [
            raw_data[index:index + width]
            for index in range(0, len(raw_data), width)
        ]
