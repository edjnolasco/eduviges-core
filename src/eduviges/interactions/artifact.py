import pygame

from eduviges.interactions.interactive_entity import InteractiveEntity
from eduviges.rendering.camera import Camera


class Artifact(InteractiveEntity):
    def __init__(
        self,
        title: str,
        description: str,
        x: int,
        y: int,
        width: int = 32,
        height: int = 32,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
        )

        self.title = title
        self.description = description

    def interact(self) -> str:
        return self.description

    def update(self, delta_time: float) -> None:
        pass

    def render(
        self,
        screen: pygame.Surface,
        camera: Camera | None = None,
    ) -> None:
        rect = camera.apply(self.rect) if camera else self.rect

        pygame.draw.rect(
            screen,
            (220, 180, 90),
            rect,
        )
