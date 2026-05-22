from pathlib import Path

import pygame


class AssetLoader:
    def __init__(self, base_path: str | Path = "assets") -> None:
        self.base_path = Path(base_path)
        self._images: dict[str, pygame.Surface] = {}

    def load_image(
        self,
        name: str,
        relative_path: str,
        convert_alpha: bool = True,
    ) -> pygame.Surface:
        if name in self._images:
            return self._images[name]

        path = self.base_path / relative_path

        if not path.exists():
            raise FileNotFoundError(f"Image asset not found: {path}")

        image = pygame.image.load(str(path))

        if convert_alpha:
            image = image.convert_alpha()
        else:
            image = image.convert()

        self._images[name] = image
        return image

    def get_image(self, name: str) -> pygame.Surface:
        if name not in self._images:
            raise KeyError(f"Image asset not loaded: {name}")

        return self._images[name]

    def has_image(self, name: str) -> bool:
        return name in self._images

    def clear(self) -> None:
        self._images.clear()
