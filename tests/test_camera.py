import pygame

from eduviges.rendering.camera import Camera


def test_camera_applies_offset_to_rect():
    camera = Camera(
        screen_width=800,
        screen_height=600,
        world_width=1600,
        world_height=1200,
    )
    camera.offset.x = 100
    camera.offset.y = 50

    rect = pygame.Rect(200, 100, 32, 32)
    applied = camera.apply(rect)

    assert applied.x == 100
    assert applied.y == 50


def test_camera_follows_target_without_negative_offset():
    camera = Camera(
        screen_width=800,
        screen_height=600,
        world_width=1600,
        world_height=1200,
    )

    target = pygame.Rect(10, 10, 32, 32)
    camera.follow(target)

    assert camera.offset.x == 0
    assert camera.offset.y == 0


def test_camera_clamps_to_world_bounds():
    camera = Camera(
        screen_width=800,
        screen_height=600,
        world_width=1600,
        world_height=1200,
    )

    target = pygame.Rect(1550, 1150, 32, 32)
    camera.follow(target)

    assert camera.offset.x == 800
    assert camera.offset.y == 600
