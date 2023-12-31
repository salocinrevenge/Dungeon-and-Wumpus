import pygame

class Input():
    def __init__(self):
        ...

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()