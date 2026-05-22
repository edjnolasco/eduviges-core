import pygame


class InteractionBox:
    def __init__(self) -> None:
        self.visible = False
        self.text = ""

        self.font: pygame.font.Font | None = None

    def show(self, text: str) -> None:
        self.text = text
        self.visible = True

    def hide(self) -> None:
        self.visible = False
        self.text = ""

    def render(self, screen: pygame.Surface) -> None:
        if not self.visible:
            return

        if self.font is None:
            self.font = pygame.font.SysFont("arial", 22)

        width, height = screen.get_size()

        box_rect = pygame.Rect(
            40,
            height - 160,
            width - 80,
            120,
        )

        pygame.draw.rect(screen, (20, 20, 30), box_rect)
        pygame.draw.rect(screen, (240, 240, 240), box_rect, 2)

        text_surface = self.font.render(
            self.text,
            True,
            (255, 255, 255),
        )

        screen.blit(
            text_surface,
            (box_rect.x + 16, box_rect.y + 40),
        )
