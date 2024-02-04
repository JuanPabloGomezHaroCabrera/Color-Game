from Resources.Colors import Colors

class Player:
    def __init__(self, ANCHO):
        self.colors = Colors()
        self.coloresCambios = [self.colors.color_red, self.colors.color_blue, self.colors.color_green, self.colors.color_purple, self.colors.color_yellow, self.colors.color_brown]
        self.personaje_rect = {'jugador_tamaño':20, 'jugador_pos0':ANCHO/2, 'jugador_pos1':520, 'jugador_color': self.colors.color_white} 

    def Reset(self):
        self.personaje_rect['jugador_color'] = self.colors.color_white

    def ChangeColor(self, index):
        self.personaje_rect['jugador_color'] = self.coloresCambios[index]

    def GetColor(self):
        return self.personaje_rect['jugador_color']