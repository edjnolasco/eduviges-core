import pygame

from eduviges.entities.entity import Entity
from eduviges.systems.entity_manager import EntityManager


class DummyEntity(Entity):
    def __init__(self) -> None:
        super().__init__(x=0, y=0, width=10, height=10)
        self.updated = False
        self.rendered = False

    def update(self, delta_time: float) -> None:
        self.updated = True

    def render(self, screen: pygame.Surface) -> None:
        self.rendered = True


def test_entity_manager_adds_entity():
    manager = EntityManager()
    entity = DummyEntity()

    manager.add(entity)

    assert entity in manager.entities


def test_entity_manager_removes_entity():
    manager = EntityManager()
    entity = DummyEntity()

    manager.add(entity)
    manager.remove(entity)

    assert entity not in manager.entities


def test_entity_manager_updates_entities():
    manager = EntityManager()
    entity = DummyEntity()

    manager.add(entity)
    manager.update(delta_time=0.016)

    assert entity.updated


def test_entity_manager_clears_entities():
    manager = EntityManager()
    entity = DummyEntity()

    manager.add(entity)
    manager.clear()

    assert manager.entities == ()
