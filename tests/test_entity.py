import pygame

from eduviges.entities.entity import Entity


class DummyEntity(Entity):
    def update(self, delta_time: float) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        pass


def test_entity_has_rect():
    entity = DummyEntity(x=10, y=20, width=30, height=40)

    assert entity.rect.x == 10
    assert entity.rect.y == 20
    assert entity.rect.width == 30
    assert entity.rect.height == 40
