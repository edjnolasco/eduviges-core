from eduviges.entities.npc import NPC


def test_npc_has_name_and_rect():
    npc = NPC(name="Amauta", x=10, y=20)

    assert npc.name == "Amauta"
    assert npc.rect.x == 10
    assert npc.rect.y == 20
    assert npc.rect.width == 32
    assert npc.rect.height == 32


def test_npc_accepts_custom_size_and_color():
    npc = NPC(
        name="Guide",
        x=0,
        y=0,
        width=48,
        height=64,
        color=(1, 2, 3),
    )

    assert npc.rect.width == 48
    assert npc.rect.height == 64
    assert npc.color == (1, 2, 3)
