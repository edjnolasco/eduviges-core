from abc import ABC, abstractmethod

import pygame

from eduviges.entities.entity import Entity


class InteractiveEntity(Entity, ABC):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        interaction_radius: int = 48,
    ) -> None:
        super().__init__(x, y, width, height)

        self.interaction_radius = interaction_radius

    def can_interact(
        self,
        other_rect: pygame.Rect,
    ) -> bool:
        interaction_rect = self.rect.inflate(
            self.interaction_radius,
            self.interaction_radius,
        )

        return interaction_rect.colliderect(other_rect)

    @abstractmethod
    def interact(self) -> str:
        pass
