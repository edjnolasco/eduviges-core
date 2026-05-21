import pygame

from eduviges.entities.entity import Entity


class Player(Entity):
    def __init__(
        self,
        x: int = 100,
        y: int = 100,
        width: int = 32,
        height: int = 32,
        speed: int = 220,
    ) -> None:
        super().__init__(x, y, width, height)
        self.speed = speed

    def move(
        self,
        direction_x: int,
        direction_y: int,
        delta_time: float,
        screen_width: int,
        screen_height: int,
    ) -> None:
        self.rect.x += int(direction_x * self.speed * delta_time)
        self.rect.y += int(direction_y * self.speed * delta_time)

        self.rect.clamp_ip(pygame.Rect(0, 0, screen_width, screen_height))

    def update(self, delta_time: float) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (80, 180, 120), self.rect)
