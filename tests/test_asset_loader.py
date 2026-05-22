from pathlib import Path

import pygame
import pytest

from eduviges.assets.asset_loader import AssetLoader


def test_asset_loader_raises_error_for_missing_image(tmp_path: Path):
    loader = AssetLoader(base_path=tmp_path)

    with pytest.raises(FileNotFoundError):
        loader.load_image("missing", "missing.png")


def test_asset_loader_stores_loaded_image(tmp_path: Path):
    pygame.init()
    pygame.display.set_mode((1, 1))

    image_path = tmp_path / "player.png"
    surface = pygame.Surface((16, 16))
    pygame.image.save(surface, image_path)

    loader = AssetLoader(base_path=tmp_path)
    loaded = loader.load_image("player", "player.png", convert_alpha=False)

    assert loaded.get_width() == 16
    assert loaded.get_height() == 16
    assert loader.has_image("player")
    assert loader.get_image("player") is loaded

    pygame.quit()


def test_asset_loader_clear_removes_images(tmp_path: Path):
    loader = AssetLoader(base_path=tmp_path)
    loader._images["fake"] = pygame.Surface((1, 1))

    loader.clear()

    assert not loader.has_image("fake")
