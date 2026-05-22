import pygame

from eduviges.core.scene import Scene
from eduviges.entities.player import Player
from eduviges.systems.entity_manager import EntityManager
from eduviges.worlds.tilemaps.tilemap import TileMap


class MainScene(Scene):
    def __init__(self) -> None:
        self.tilemap = TileMap(
            data=[
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 0, 0, 1, 1, 0, 0, 1, 2],
                [2, 1, 0, 1, 1, 1, 1, 0, 1, 2],
                [2, 1, 0, 1, 0, 0, 1, 0, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            ],
            tile_size=64,
        )

        self.entity_manager = EntityManager()
        self.player = Player(x=96, y=96)
        self.entity_manager.add(self.player)

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
            screen_width=self.tilemap.width,
            screen_height=self.tilemap.height,
        )

        self.entity_manager.update(delta_time)

    def render(self, screen: pygame.Surface) -> None:
        self.tilemap.render(screen)
        self.entity_manager.render(screen)
