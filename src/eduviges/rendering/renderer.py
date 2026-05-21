import pygame


class Renderer:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def clear(self, color: tuple[int, int, int]) -> None:
        self.screen.fill(color)

    def present(self) -> None:
        pygame.display.flip()