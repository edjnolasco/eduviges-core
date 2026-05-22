import pygame

from eduviges.entities.entity import Entity
from eduviges.rendering.camera import Camera


class NPC(Entity):
    def __init__(
        self,
        name: str,
        x: int,
        y: int,
        width: int = 32,
        height: int = 32,
        color: tuple[int, int, int] = (180, 140, 80),
    ) -> None:
        super().__init__(x, y, width, height)
        self.name = name
        self.color = color

    def update(self, delta_time: float) -> None:
        pass

    def render(
        self,
        screen: pygame.Surface,
        camera: Camera | None = None,
    ) -> None:
        rect = camera.apply(self.rect) if camera else self.rect
        pygame.draw.rect(screen, self.color, rect)
