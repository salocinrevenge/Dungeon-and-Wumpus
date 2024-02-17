class Dungeon():
      def __init__(self, game):
            self.game = game
            self.mapBuilder = MapBuilder()
            self.rooms = self.mapBuilder.buildRooms(GameMapTokens.getDungeonPATH(), self)
            self.pos = GameBrain.getOrigin()

      
      def update(self, double dt)
            self.getCurrentRoom().update(dt)

      def setState(self, state)
            self.setState(state)

      def getState(self)
            return self.game.getState()

      def renderer(self, r)
            getCurrentRoom().renderer(r)

      def getCurrentRoom(self)
            return self.rooms[self.pos.getFirst()][self.pos.getSecond()]
      

      def getRoom(self, i, j)
            return rooms[i][j]
      

      def setAtual(self, i, j)
            self.pos = (i,j)
      

      def toggleFollow(self):
            self.follow = not self.follow
      

      def getFollow(self):
            return self.follow
      

      def getBag(self):
	      return self.game.getBag()
