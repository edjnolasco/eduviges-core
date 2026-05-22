import pygame

from eduviges.entities.player import Player


def test_player_moves_right():
    player = Player(x=100, y=100, speed=100)

    player.move(
        direction_x=1,
        direction_y=0,
        delta_time=1.0,
        collision_rects=[],
        screen_width=800,
        screen_height=600,
    )

    assert player.rect.x == 200
    assert player.rect.y == 100


def test_player_moves_down():
    player = Player(x=100, y=100, speed=100)

    player.move(
        direction_x=0,
        direction_y=1,
        delta_time=1.0,
        collision_rects=[],
        screen_width=800,
        screen_height=600,
    )

    assert player.rect.y == 200


def test_player_cannot_move_through_collision_rect():
    player = Player(
        x=100,
        y=100,
        width=32,
        height=32,
        speed=100,
    )

    wall = pygame.Rect(200, 100, 32, 32)

    player.move(
        direction_x=1,
        direction_y=0,
        delta_time=1.0,
        collision_rects=[wall],
        screen_width=800,
        screen_height=600,
    )

    assert player.rect.x == 100


def test_player_stays_inside_screen():
    player = Player(x=0, y=0, speed=100)

    player.move(
        direction_x=-1,
        direction_y=-1,
        delta_time=1.0,
        collision_rects=[],
        screen_width=800,
        screen_height=600,
    )

    assert player.rect.x == 0
    assert player.rect.y == 0
