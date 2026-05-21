from __future__ import annotations

from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        self.rect = pygame.Rect(x, y, width, height)

    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        pass
