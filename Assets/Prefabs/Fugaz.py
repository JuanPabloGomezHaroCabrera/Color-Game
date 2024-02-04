import pygame

class Fugaz:
    def __init__(self):
        self.fugaz = pygame.image.load("Assets/Imagenes/estrella.png") #Estrella fugaz
        self.fugazRect = self.fugaz.get_rect() #Obtenemos el objeto de la imagen, su contorno
        self.speed_fugaz = [30, 30] #Velocidad de la estrella fugaz

    def Move(self):
        self.fugazRect = self.fugazRect.move(self.speed_fugaz)
    
    def Check(self):
        if self.fugazRect.left < (-500) or self.fugazRect.right > (800 + 500):
            self.speed_fugaz[0] = -self.speed_fugaz[0] #Velocidad en eje x inversa
		#Si la imagen "estrella fugaz" topa con límite horizontal rebotará con la misma velocidad pero inversa en el eje y
        if self.fugazRect.top < (-500) or self.fugazRect.bottom > (600 + 500):
            self.speed_fugaz[1] = -self.speed_fugaz[1] #Velocidad en eje y inversa
