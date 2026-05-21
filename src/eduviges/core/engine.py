import pygame

from eduviges.core.settings import (
    FPS,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)
from eduviges.rendering.renderer import Renderer
from eduviges.worlds.scenes.main_scene import MainScene


class Engine:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        self.renderer = Renderer(self.screen)

        self.scene = MainScene()

        self.running = True

    def run(self) -> None:
        while self.running:
            delta_time = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.scene.handle_event(event)

            self.scene.update(delta_time)

            self.scene.render(self.screen)

            self.renderer.present()

        pygame.quit()