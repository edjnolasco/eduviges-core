import pygame


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
        self.rect = pygame.Rect(
            grid_x * size,
            grid_y * size,
            size,
            size,
        )

    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
