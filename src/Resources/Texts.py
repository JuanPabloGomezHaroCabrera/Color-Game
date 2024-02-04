from Resources.Fonts import Fonts
from Resources.Colors import Colors

class Texts:
    def __init__(self):
        self.fonts = Fonts()
        self.colors = Colors()
        # Titulo COLOR CHALLENGE
        self.titulo_C1 = self.fonts.fuente1.render("C", 0, self.colors.color_green)
        self.titulo_O1 = self.fonts.fuente1.render("O", 0, self.colors.color_green)
        self.titulo_L1 = self.fonts.fuente1.render("L", 0, self.colors.color_red)
        self.titulo_O2 = self.fonts.fuente1.render("O", 0, self.colors.color_red)
        self.titulo_R = self.fonts.fuente1.render("R", 0, self.colors.color_gray)
        self.titulo_C2 = self.fonts.fuente1.render("C", 0, self.colors.color_gray)
        self.titulo_H = self.fonts.fuente1.render("H", 0, self.colors.color_blue)
        self.titulo_A = self.fonts.fuente1.render("A", 0, self.colors.color_blue)
        self.titulo_L2 = self.fonts.fuente1.render("L", 0, self.colors.color_yellow)
        self.titulo_L3 = self.fonts.fuente1.render("L", 0, self.colors.color_yellow)
        self.titulo_E1 = self.fonts.fuente1.render("E", 0, self.colors.color_purple)
        self.titulo_N = self.fonts.fuente1.render("N", 0, self.colors.color_purple)
        self.titulo_G = self.fonts.fuente1.render("G", 0, self.colors.color_brown)
        self.titulo_E2 = self.fonts.fuente1.render("E", 0, self.colors.color_brown)
        # Controles
        self.texto_FI = self.fonts.fuente2.render("Flecha Izquierda = rojo", 0, self.colors.color_red)
        self.texto_FD = self.fonts.fuente2.render("Flecha Derecha = azul", 0, self.colors.color_blue)
        self.texto_FS = self.fonts.fuente2.render("Flecha Superior = verde", 0, self.colors.color_green)
        self.texto_FIN = self.fonts.fuente2.render("Flecha Inferior = morado", 0, self.colors.color_purple)
        self.texto_LA = self.fonts.fuente2.render("a = amarillo", 0, self.colors.color_yellow)
        self.texto_LS = self.fonts.fuente2.render("s = cafe", 0, self.colors.color_brown)
        # Titulos de cada nivel
        self.texto_LEVEL2 = self.fonts.fuente1.render("LEVEL 2", 0, self.colors.color_white)
        self.texto_LEVEL3 = self.fonts.fuente1.render("LEVEL 3", 0, self.colors.color_white)
        self.texto_LEVEL4 = self.fonts.fuente1.render("LEVEL 4", 0, self.colors.color_white)
        # Requerimientos
        self.texto_70 = self.fonts.fuente2.render("Alcanza 70 puntos para pasar al nivel 2", 0, self.colors.color_white)
        self.texto_160 = self.fonts.fuente2.render("Alcanza 160 puntos para pasar al nivel 3", 0, self.colors.color_white)
        self.texto_270 = self.fonts.fuente2.render("Alcanza 270 puntos para pasar al nivel 4", 0, self.colors.color_white)
        self.texto_400 = self.fonts.fuente2.render("Alcanza 400 puntos para ganar", 0, self.colors.color_white)
        # Puntaje y demas indicaciones
        self.texto_SPACE = self.fonts.fuente1.render("Press SPACE", 0, self.colors.color_gray)
        self.texto_HS = self.fonts.fuente2.render("High Score", 0, self.colors.color_white)
        self.texto_S = self.fonts.fuente2.render("Score", 0, self.colors.color_white)
        self.texto_PISTA = self.fonts.fuente3.render("*El primer obstáculo y personaje inician en blanco*", 0, self.colors.color_white)
        # Creditos
        self.texto_CreditosTitulo = self.fonts.fuente2.render("Créditos", 0, self.colors.color_white)
        self.texto_Creditos = self.fonts.fuente2.render("Programación: ", 0, self.colors.color_white)
        self.texto_Creditos2 = self.fonts.fuente2.render("Música:", 0, self.colors.color_white)
        self.texto_JuanPablo = self.fonts.fuente2.render("Juan Pablo Gómez Haro Cabrera", 0, self.colors.color_white)

    def GetScore(self, score):
        texto8 = self.fonts.fuente2.render(str(score), 0, self.colors.color_white)
        return texto8
    def GetHighScore(self, highscore):
        texto9 = self.fonts.fuente2.render(str(highscore), 0, self.colors.color_white)
        return texto9