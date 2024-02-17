from engine.GameContainer import GameContainer
from engine.AbstractGame import AbstractGame
from game.Dungeon import Dungeon

class GameManager(AbstractGame):
    def __init__(self):
        self.dungeon = Dungeon(self)

    def update(self, gc, dt):
        self.dungeon.update(gc, dt)

    def reset(self):
        self.dungeon = Dungeon(self)
    
    def render(self, gc, r):
        self.dungeon.render(gc, r)