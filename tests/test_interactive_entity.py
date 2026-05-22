import pygame

from eduviges.interactions.artifact import Artifact


def test_artifact_can_interact_when_near():
    artifact = Artifact(
        title="Cemí",
        description="Objeto ceremonial",
        x=100,
        y=100,
    )

    player_rect = pygame.Rect(
        110,
        110,
        32,
        32,
    )

    assert artifact.can_interact(
        player_rect
    )


def test_artifact_cannot_interact_when_far():
    artifact = Artifact(
        title="Cemí",
        description="Objeto ceremonial",
        x=100,
        y=100,
    )

    player_rect = pygame.Rect(
        500,
        500,
        32,
        32,
    )

    assert not artifact.can_interact(
        player_rect
    )


def test_artifact_returns_description():
    artifact = Artifact(
        title="Cemí",
        description="Descripción histórica",
        x=0,
        y=0,
    )

    assert (
        artifact.interact()
        == "Descripción histórica"
    )
