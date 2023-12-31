from game.GameManager import GameManager
from engine.GameContainer import GameContainer

if __name__ == "__main__":
    gc = GameContainer(GameManager());
    gc.start()
    