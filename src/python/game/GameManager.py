from engine.GameContainer import GameContainer
from engine.AbstractGame import AbstractGame

class GameManager(AbstractGame):
    def __init__(self):
        gc = GameContainer(self)
        gc.start()


if __name__ == "__main__":
    GameManager()