import pygame

from eduviges.rendering.camera import Camera


class Tile:
    def __init__(
        self,
        grid_x: int,
        grid_y: int,
        size: int,
        color: tuple[int, int, int],
        walkable: bool = True,
    ) -> None:
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.size = size
        self.color = color
        self.walkable = walkable
        self.rect = pygame.Rect(grid_x * size, grid_y * size, size, size)

    def render(self, screen: pygame.Surface, camera: Camera | None = None) -> None:
        rect = camera.apply(self.rect) if camera else self.rect
        pygame.draw.rect(screen, self.color, rect)
