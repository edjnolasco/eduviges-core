from eduviges.entities.player import Player


def test_player_moves_right():
    player = Player(x=100, y=100, speed=100)

    player.move(
        direction_x=1,
        direction_y=0,
        delta_time=1.0,
        screen_width=800,
        screen_height=600,
    )

    assert player.rect.x == 200
    assert player.rect.y == 100


def test_player_moves_left():
    player = Player(x=100, y=100, speed=100)

    player.move(
        direction_x=-1,
        direction_y=0,
        delta_time=1.0,
        screen_width=800,
        screen_height=600,
    )

    assert player.rect.x == 0
    assert player.rect.y == 100


def test_player_moves_down():
    player = Player(x=100, y=100, speed=100)

    player.move(
        direction_x=0,
        direction_y=1,
        delta_time=1.0,
        screen_width=800,
        screen_height=600,
    )

    assert player.rect.x == 100
    assert player.rect.y == 200


def test_player_stays_inside_screen_left_boundary():
    player = Player(x=10, y=100, speed=100)

    player.move(
        direction_x=-1,
        direction_y=0,
        delta_time=1.0,
        screen_width=800,
        screen_height=600,
    )

    assert player.rect.x == 0


def test_player_stays_inside_screen_right_boundary():
    player = Player(x=790, y=100, width=32, speed=100)

    player.move(
        direction_x=1,
        direction_y=0,
        delta_time=1.0,
        screen_width=800,
        screen_height=600,
    )

    assert player.rect.right == 800
