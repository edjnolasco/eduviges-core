import pygame


class InputManager:
    def __init__(self) -> None:
        self._pressed_keys: set[int] = set()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            self._pressed_keys.add(event.key)

        if event.type == pygame.KEYUP:
            self._pressed_keys.discard(event.key)

    def is_pressed(self, key: int) -> bool:
        return key in self._pressed_keys
