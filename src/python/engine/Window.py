import pygame

class Window():
      
      def __init__(self, width, height):
            self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            pygame.display.set_caption("Doungeon and Wumpus")

      def update(self):
            pass


