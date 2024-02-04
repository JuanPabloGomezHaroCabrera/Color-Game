from Resources.Colors import Colors
import random

class Obstaculo:
    def __init__(self, posicionInicial, colorInicial):
        self.posicionInicial = posicionInicial
        self.colorInicial = colorInicial
        self.speed = 6
        self.colors = Colors()
        # self.colors.Color_aleatorio(random.randint(1,3), 1)
        self.obstaculo_rect = {'obs_tamaño0':800, 'obs_tamaño1':20, 'obs_pos0':0, 'obs_pos1':posicionInicial, 'obs_color':colorInicial} 

    def Top(self, nivel):
        self.obstaculo_rect['obs_pos1'] = 0 #Colocar en posición de y=0 (hasta arriba)
        self.obstaculo_rect['obs_color'] = self.colors.Color_aleatorio(random.randint(1,(nivel+2)), nivel)

    def Reset(self):
        self.obstaculo_rect['obs_color'] = self.colorInicial
        self.obstaculo_rect['obs_pos1'] = self.posicionInicial


    def GetColor(self):
        return self.obstaculo_rect['obs_color']

    def Move(self):
        self.obstaculo_rect['obs_pos1'] += self.speed
    
    def SetSpeed(self, speed):
        self.speed = speed
    
    def ResetObstaculo(self):
        self.Reset()
        self.speed = 6
    
    def EnLimite(self, ALTO):
        if self.obstaculo_rect['obs_pos1'] >= ALTO:
            return True
        return False

    def EnPlayer(self):
        # Posición del jugador entre 520-540
        if self.obstaculo_rect['obs_pos1'] >=520 and self.obstaculo_rect['obs_pos1'] <=540:
            return True
        return False