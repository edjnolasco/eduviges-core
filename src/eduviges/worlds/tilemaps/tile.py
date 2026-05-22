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
        sprite: pygame.Surface | None = None,
    ) -> None:
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.size = size
        self.walkable = walkable
        self.color = color
        self.sprite = sprite

        self.rect = pygame.Rect(
            grid_x * size,
            grid_y * size,
            size,
            size,
        )

    def render(
        self,
        screen: pygame.Surface,
        camera: Camera | None = None,
    ) -> None:
        render_rect = (
            camera.apply(self.rect)
            if camera
            else self.rect
        )

        if self.sprite:
            screen.blit(self.sprite, render_rect)
            return

        pygame.draw.rect(
            screen,
            self.color,
            render_rect,
        )
