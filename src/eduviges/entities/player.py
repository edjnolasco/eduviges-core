import pygame

from eduviges.entities.entity import Entity
from eduviges.rendering.camera import Camera


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
        collision_rects: list[pygame.Rect],
        screen_width: int,
        screen_height: int,
    ) -> None:
        next_rect = self.rect.copy()
        next_rect.x += int(direction_x * self.speed * delta_time)
        next_rect.y += int(direction_y * self.speed * delta_time)

        if not any(next_rect.colliderect(rect) for rect in collision_rects):
            self.rect = next_rect

        self.rect.clamp_ip(pygame.Rect(0, 0, screen_width, screen_height))

    def update(self, delta_time: float) -> None:
        pass

    def render(
        self,
        screen: pygame.Surface,
        camera: Camera | None = None,
    ) -> None:
        rect = camera.apply(self.rect) if camera else self.rect
        pygame.draw.rect(screen, (80, 180, 120), rect)
