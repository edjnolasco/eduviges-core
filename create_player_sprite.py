import pygame

pygame.init()

surface = pygame.Surface((32, 32), pygame.SRCALPHA)

surface.fill((0, 0, 0, 0))

pygame.draw.rect(surface, (80, 180, 120), (4, 4, 24, 24))
pygame.draw.rect(surface, (40, 90, 60), (8, 8, 16, 16))

pygame.image.save(surface, "assets/sprites/player.png")

pygame.quit()
