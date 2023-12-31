from engine.GameContainer import GameContainer
from engine.AbstractGame import AbstractGame

class GameManager(AbstractGame):
    def __init__(self):
        gc = GameContainer(self)
        gc.start()

    def update(self, gc, dt):
        pass

if __name__ == "__main__":
    GameManager()