import pygame

from eduviges.core.scene import Scene
from eduviges.core.settings import BACKGROUND_COLOR, WINDOW_HEIGHT, WINDOW_WIDTH
from eduviges.entities.player import Player


class MainScene(Scene):
    def __init__(self) -> None:
        self.player = Player()

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, delta_time: float) -> None:
        keys = pygame.key.get_pressed()

        direction_x = 0
        direction_y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            direction_x -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            direction_x += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            direction_y -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            direction_y += 1

        self.player.move(
            direction_x=direction_x,
            direction_y=direction_y,
            delta_time=delta_time,
            screen_width=WINDOW_WIDTH,
            screen_height=WINDOW_HEIGHT,
        )

    def render(self, screen: pygame.Surface) -> None:
        screen.fill(BACKGROUND_COLOR)
        self.player.render(screen)
