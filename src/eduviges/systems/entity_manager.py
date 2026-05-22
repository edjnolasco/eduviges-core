import pygame

from eduviges.entities.entity import Entity
from eduviges.rendering.camera import Camera


class EntityManager:
    def __init__(self) -> None:
        self._entities: list[Entity] = []

    def add(self, entity: Entity) -> None:
        self._entities.append(entity)

    def remove(self, entity: Entity) -> None:
        if entity in self._entities:
            self._entities.remove(entity)

    def update(self, delta_time: float) -> None:
        for entity in self._entities:
            entity.update(delta_time)

    def render(
        self,
        screen: pygame.Surface,
        camera: Camera | None = None,
    ) -> None:
        for entity in self._entities:
            entity.render(screen, camera)

    @property
    def entities(self) -> tuple[Entity, ...]:
        return tuple(self._entities)

    def clear(self) -> None:
        self._entities.clear()
