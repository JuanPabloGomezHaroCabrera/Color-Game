from Assets.Prefabs.Player import Player
from Assets.Prefabs.Obstaculo import Obstaculo
from Resources.Colors import Colors
from Resources.Ventana import Ventana
from Assets.Prefabs.Fugaz import Fugaz
import pygame

class GameController:
    def __init__(self):
        # Componentes
        pygame.mixer.init()
        self.colors = Colors()
        self.ANCHO = 800
        self.ALTO = 600
        # Objetos
        self.player = Player(self.ANCHO)
        self.obstaculos = [Obstaculo(400, self.colors.color_white), Obstaculo(200, self.colors.color_blue), Obstaculo(0, self.colors.color_red)]
        self.ventana = Ventana()
        self.fugaz = Fugaz()
        self.clock = pygame.time.Clock()
        # Variables
        self.nivel = 1
        self.speed = 6
        self.contador = 0
        self.Score = 0
        self.currentScore = 0
        self.HighScore = 0
        self.scoreRequired = 70
        # Musica
        pygame.mixer.music.load("Assets/Audio/MusicaDeEspera_ChallengeColor.wav") #Guardar música de fondo para la sala de instrucciones
        self.musica_juego = pygame.mixer.Sound("Assets/Audio/MusicaJuego.wav") #Musica durante el juego
        self.musica_ganador = pygame.mixer.Sound("Assets/Audio/Musica_Ganador.wav") #Musica durante el final
        self.fondo = pygame.image.load("Assets/Imagenes/universo.png") #Fondo de universo
        # Booleanos para el flujo del juego
        self.jugando = True
        self.gameOver = False
        self.exit = False
        self.instrucciones = True
        self.ganador = False

        pygame.display.set_caption("Color Game")



    # Restablecer posiciones, colores, puntajes
    def ReinicioJuego(self):
        if self.Score > self.HighScore:
            self.HighScore = self.Score
        self.contador = 0
        self.speed = 6
        self.player.Reset()
        for obs in self.obstaculos:
            obs.Reset()
        self.instrucciones = True

    def Start(self):
        while self.exit == False:
            
            # Niveles Intrucciones
            while self.instrucciones:
                pygame.mixer.music.play(-1)
                if self.nivel == 1:
                    self.ventana.Instructivo1(self.currentScore, self.HighScore)
                    self.scoreRequired = 10 # 70
                elif self.nivel == 2:
                    self.ventana.Instructivo2()
                    self.scoreRequired = 20 # 160
                elif self.nivel == 3:
                    self.ventana.Instructivo3()
                    self.scoreRequired = 30 # 270
                elif self.nivel == 4:
                    self.ventana.Instructivo4()
                    self.scoreRequired = 40 # 400
                pygame.mixer.music.stop()
                self.jugando = True
                self.instrucciones = False
                self.musica_juego.play()


            while self.jugando:
                # FPS
                self.clock.tick(30)
                
                # Fondo imagenes, estrella fugaz
                self.ventana.FondoNegro(self.fondo)
                self.fugaz.Move()
                self.fugaz.Check()
                self.ventana.ventana.blit(self.fugaz.fugaz, self.fugaz.fugazRect)

                # Por cada obstaculo: movimiento, reset de posicion y color, choque con el player
                for obs in self.obstaculos:
                    if obs.EnLimite(self.ALTO) == False:
                        obs.SetSpeed(self.speed)
                        obs.Move()
                        if obs.EnPlayer():
                            # Si los colores son distintos
                            if self.player.GetColor() != obs.GetColor():
                                self.gameOver = True
                                self.jugando = False
                                self.musica_juego.stop()
                    else:
                        self.Score += 1
                        self.contador += 1
                        obs.Top(self.nivel)

                # Cambios de velocidad para mas dificultad
                if self.contador <= 7:
                    self.speed = 6
                elif self.contador <= 14:
                    self.speed = 8
                elif self.contador <= 21:
                    self.speed = 10
                elif self.contador <= 28:
                    self.speed = 12
                elif self.contador <= 35:
                    self.speed = 14
                elif self.contador <= 42:
                    self.speed = 16
                elif self.contador <= 49:
                    self.speed = 18
                elif self.contador > 49:
                    self.speed = 20
                
                # Dibujar jugador
                pygame.draw.rect(self.ventana.ventana, self.player.personaje_rect['jugador_color'],
                                (self.player.personaje_rect['jugador_pos0'],self.player.personaje_rect['jugador_pos1'],
                                self.player.personaje_rect['jugador_tamaño'],self.player.personaje_rect['jugador_tamaño']))
                # Dibujar obstáculos
                for obs in self.obstaculos:
                    pygame.draw.rect(self.ventana.ventana, obs.obstaculo_rect['obs_color'],
                                (obs.obstaculo_rect['obs_pos0'],obs.obstaculo_rect['obs_pos1'],
                                obs.obstaculo_rect['obs_tamaño0'],obs.obstaculo_rect['obs_tamaño1']))

                # Detectar los eventos
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.jugando = False
                        self.exit = True
                    # Se obtienen eventos del teclado
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.player.ChangeColor(0)
                        elif event.key == pygame.K_RIGHT:
                            self.player.ChangeColor(1)
                        elif event.key == pygame.K_UP:
                            self.player.ChangeColor(2)
                        elif event.key == pygame.K_DOWN and self.nivel > 1:
                            self.player.ChangeColor(3)
                        elif event.key == pygame.K_a and self.nivel > 2:
                            self.player.ChangeColor(4)
                        elif event.key == pygame.K_s and self.nivel > 3:
                            self.player.ChangeColor(5)
                
                self.ventana.GetScore(self.Score)
                # Score alcanzado para cambio de nivel
                if self.Score == self.scoreRequired:
                    if self.nivel == 4:
                        self.ganador = True
                    self.nivel += 1
                    self.ReinicioJuego()
                    self.jugando = False
                    self.musica_juego.stop()
                # Actualizar
                pygame.display.update()

            # GAME OVER
            if self.gameOver:
                self.ReinicioJuego()
                self.gameOver = False
                self.nivel = 1
                self.currentScore = self.Score
                self.Score = 0

            # Ganador
            if self.ganador:
                self.ReinicioJuego()
                self.musica_ganador.play()
                self.ventana.Ganador()
                self.musica_ganador.stop()
                self.ganador = False
                self.nivel = 1
                self.Score = 0