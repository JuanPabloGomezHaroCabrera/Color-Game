class Colors:
    def __init__(self):
        self.color_gray = (80,80,80)
        self.color_red = (255,0,0)
        self.color_blue = (0,0,255)
        self.color_green = (0,100,0)
        self.color_black = (0,0,0,)
        self.color_purple = (128,0,128)
        self.color_white = (255,255,255)
        self.color_yellow = (255,255,0)
        self.color_brown = (130,65,0)
    
    def Color_aleatorio(self, x, nivel):
        if x == 1:
            return self.color_red
        elif x == 2:
            return self.color_blue
        elif x == 3:
            return self.color_green
        # Nivel entre 2-4
        elif x == 4 and nivel > 1:
            return self.color_purple
        # Nivel entre 3-4
        elif x == 5 and nivel > 2:
            return self.color_yellow
        # Nivel 4
        elif x == 6 and nivel == 4:
            return self.color_brown