import pygame, sys
from Resources.Colors import Colors
from Resources.Fonts import Fonts
from Resources.Texts import Texts

class Ventana:
    def __init__(self):
        self.ANCHO = 800
        self.ALTO = 600
        self.ventana = pygame.display.set_mode((self.ANCHO,self.ALTO))
        self.colors = Colors()
        self.fonts = Fonts()
        self.texts = Texts()
        self.clock = pygame.time.Clock()

    def FondoNegro(self, fondo):
        self.ventana.fill(self.colors.color_black)
        self.ventana.blit(fondo, (0,0))

    def PausaInstructiva(self):
        mostrar = True
        while mostrar:
            # self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        mostrar = False
        # return False

    def Instructivo1(self, score, highScore):
        self.ventana.fill(self.colors.color_black)
        self.ventana.blit(self.texts.titulo_C1, (165,100))
        self.ventana.blit(self.texts.titulo_O1, (195,100))
        self.ventana.blit(self.texts.titulo_L1, (225,100))
        self.ventana.blit(self.texts.titulo_O2, (255,100))
        self.ventana.blit(self.texts.titulo_R, (285,100))
        self.ventana.blit(self.texts.titulo_C2, (345,100))
        self.ventana.blit(self.texts.titulo_H, (375,100))
        self.ventana.blit(self.texts.titulo_A, (405,100))
        self.ventana.blit(self.texts.titulo_L2, (435,100))
        self.ventana.blit(self.texts.titulo_L3, (465,100))
        self.ventana.blit(self.texts.titulo_E1, (495,100))
        self.ventana.blit(self.texts.titulo_N, (525,100))
        self.ventana.blit(self.texts.titulo_G, (555,100))
        self.ventana.blit(self.texts.titulo_E2, (585,100))
        self.ventana.blit(self.texts.texto_FI, (270,200))
        self.ventana.blit(self.texts.texto_FD, (270,250))
        self.ventana.blit(self.texts.texto_FS, (270,300))
        self.ventana.blit(self.texts.texto_SPACE, (260,350))
        self.ventana.blit(self.texts.texto_HS, (150,450))
        self.ventana.blit(self.texts.texto_S, (550,450))
        self.ventana.blit(self.texts.GetScore(score), (650,450))
        self.ventana.blit(self.texts.GetHighScore(highScore), (300,450))
        self.ventana.blit(self.texts.texto_70, (200,500))
        self.ventana.blit(self.texts.texto_PISTA, (240,550))
        pygame.display.update()
        # pygame.display.flip()
        self.PausaInstructiva()

    def Instructivo2(self):
        self.InstructivoGeneral()
        #Mostramos en pantalla textos e imagen
        self.ventana.blit(self.texts.texto_LEVEL2, (300,100))
        self.ventana.blit(self.texts.texto_160, (200,500))
        pygame.display.update()#Actualizar frame con frame la ventana
        self.PausaInstructiva()
    
    def Instructivo3(self):
        self.InstructivoGeneral()
        self.ventana.blit(self.texts.texto_LEVEL3, (300,100)) #Level 3
        self.ventana.blit(self.texts.texto_LA, (450,250)) #a = amarillo
        self.ventana.blit(self.texts.texto_270, (200,500)) #Alcanza 270 puntos...
        pygame.display.update()#Actualizar frame con frame la ventana
        self.PausaInstructiva()

    def Instructivo4(self):
        self.InstructivoGeneral()
        #Mostramos en pantalla textos e imagen
        self.ventana.blit(self.texts.texto_LA, (450,250)) #a = amarillo
        self.ventana.blit(self.texts.texto_LS, (450,300)) #s = cafe
        self.ventana.blit(self.texts.texto_400, (200,500)) #Alcanza 400 puntos...
        pygame.display.update() #Actualizar frame con frame la ventana
        self.PausaInstructiva()

    def InstructivoGeneral(self):
        black = pygame.Surface((self.ANCHO,self.ALTO))
        black.set_alpha(200) # Opacidad
        pygame.draw.rect(black, self.colors.color_black, black.get_rect(), 10)#Ponemos en pantalla la imagen de fondo
        #Mostramos en pantalla textos e imagen
        self.ventana.blit(black, (0, 0))#Actualizamos el fondo
        self.ventana.blit(self.texts.texto_FI, (150,200))
        self.ventana.blit(self.texts.texto_FD, (150,250))
        self.ventana.blit(self.texts.texto_FS, (150,300))
        self.ventana.blit(self.texts.texto_FIN, (450,200))
        self.ventana.blit(self.texts.texto_SPACE, (260,350))
        self.ventana.blit(self.texts.texto_PISTA, (240,550))

    def Ganador(self):
        fondo = pygame.image.load("Assets/Imagenes/universo.png")
        fuente4 = pygame.font.Font(None, 100) #Creamos una cuarta fuente para textos
        texto_Victoria = fuente4.render("¡GANADOR!", 0, self.colors.color_white)
		#Ventana color gris
        self.ventana.fill(self.colors.color_black)
        self.ventana.blit(fondo, (0,0))
        self.ventana.blit(texto_Victoria, (200, 100))
        self.ventana.blit(self.texts.texto_CreditosTitulo, (350, 200))
        self.ventana.blit(self.texts.texto_Creditos, (330, 250))
        self.ventana.blit(self.texts.texto_JuanPablo, (250,300))
        self.ventana.blit(self.texts.texto_Creditos2, (360, 350))
        self.ventana.blit(self.texts.texto_JuanPablo, (250,400))
        self.ventana.blit(self.texts.texto_SPACE, (260, 500))
        # Actualizar frame con frame la ventana
        pygame.display.update()
        self.PausaInstructiva()
        
    def GetScore(self, score):
        self.ventana.blit(self.texts.GetScore(score), (400, 40))