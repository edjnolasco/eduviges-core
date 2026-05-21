import pygame

from eduviges.core.scene import Scene
from eduviges.core.settings import BACKGROUND_COLOR


class MainScene(Scene):
    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, delta_time: float) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        screen.fill(BACKGROUND_COLOR)