import AbstractGame
import Window
import Renderer
import Input
import Thread
import time

class GameContainer(AbstractGame):

      FPS_PADRAO = 60.0
      UPDATE_CAP = 1.0/FPS_PADRAO
    
      def __init__(self, game):
            self.game = game
      
      """public void start(){
            window = new Window(this);
            renderer = new Renderer(this);
            input = new Input(this);

            thread = new Thread(this);
            thread.run();
      }"""

      def start(self):
            self.window = Window(self)
            self.renderer = Renderer(self)
            self.input = Input(self)
            self.thread = Thread(self)
            self.thread.run() # executa o metodo run() dessa classe em uma thread

      def run(self):
            self.running = True
            render = False
            firstTime = 0
            lastTime = time.time()  # retorna o tempo atual em segundos
            passedTime = 0
            unprocessedTime = 0
            frameTime = 0
            frames = 0
            fps = 0

            while self.running:
                  render = False
                  firstTime = time.time()
                  passedTime = firstTime - lastTime   # tempo que passou desde a ultima vez que o loop foi executado
                  lastTime = firstTime            # atualiza o tempo da ultima vez que o loop foi executado

                  unprocessedTime += passedTime  # tempo nao processado
                  frameTime += passedTime

                  # enquanto nao processou td q deveria (devido a lag em render ou coisas assim)
                  while unprocessedTime >= self.UPDATE_CAP:
                        # Isso garante que o tempo de atualizacao seja constante
                        # e nao dependa do tempo de renderizacao. Igualando o 
                        # jogo para todos os computadores, apenas aumentando o
                        # fps para computadores mais potentes
                        unprocessedTime -= self.UPDATE_CAP  # Tempo comido
                        render = True

                        self.game.tick(self, self.UPDATE_CAP)
                        self.input.tick()

                        if frameTime >= 1.0:
                              frameTime = 0
                              fps = frames
                              frames = 0
                              print("FPS: " + str(fps))

                  # Depois de processar o tempo, renderiza
                  if render:
                        self.renderer.clear()
                        self.game.render(self, self.renderer)
                        self.window.update()
                        frames += 1
                  else:
                        time.sleep(0.001)
                  
            self.dispose()
      
      def dispose(self):      # metodo chamado quando o jogo fecha
            pass

      
    
      