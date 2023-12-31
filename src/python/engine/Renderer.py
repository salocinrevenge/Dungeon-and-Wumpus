import pygame

class Renderer():
    def __init__(self, screen):
        self.screen = screen

    def clear(self):
        pygame.display.flip()
        self.screen.fill((0, 0, 0))