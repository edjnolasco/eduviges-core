import pygame


class Camera:
    def __init__(
        self,
        screen_width: int,
        screen_height: int,
        world_width: int,
        world_height: int,
    ) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.world_width = world_width
        self.world_height = world_height
        self.offset = pygame.Vector2(0, 0)

    def follow(self, target_rect: pygame.Rect) -> None:
        self.offset.x = target_rect.centerx - self.screen_width // 2
        self.offset.y = target_rect.centery - self.screen_height // 2

        self.offset.x = max(0, min(self.offset.x, self.world_width - self.screen_width))
        self.offset.y = max(0, min(self.offset.y, self.world_height - self.screen_height))

    def apply(self, rect: pygame.Rect) -> pygame.Rect:
        return rect.move(-int(self.offset.x), -int(self.offset.y))
