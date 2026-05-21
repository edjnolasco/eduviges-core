import pygame

from eduviges.input.input_manager import InputManager


def test_keydown_marks_key_as_pressed():
    manager = InputManager()

    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    manager.handle_event(event)

    assert manager.is_pressed(pygame.K_SPACE)


def test_keyup_removes_key_from_pressed_keys():
    manager = InputManager()

    down_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    up_event = pygame.event.Event(pygame.KEYUP, key=pygame.K_SPACE)

    manager.handle_event(down_event)
    manager.handle_event(up_event)

    assert not manager.is_pressed(pygame.K_SPACE)
