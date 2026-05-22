import pygame


class InteractionPrompt:
    def __init__(self) -> None:
        self.font: pygame.font.Font | None = None

    def render(
        self,
        screen: pygame.Surface,
        text: str = "E - Interactuar",
    ) -> None:
        if self.font is None:
            self.font = pygame.font.SysFont("arial", 20)

        surface = self.font.render(
            text,
            True,
            (255, 255, 255),
        )

        rect = surface.get_rect(
            center=(
                screen.get_width() // 2,
                screen.get_height() - 40,
            )
        )

        pygame.draw.rect(
            screen,
            (20, 20, 20),
            rect.inflate(20, 10),
        )

        screen.blit(surface, rect)
