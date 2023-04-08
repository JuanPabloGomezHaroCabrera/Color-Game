#Importamos pygame para la interfaz, sys para el sistema y random para generar aleatorios
import pygame, sys, random 

#Para poder crear textos
pygame.font.init()
#Para poder cagregar audios/musica
pygame.mixer.init()

#Constantes 
ANCHO = 800 #Ancho de la ventana
ALTO = 600 #Alto de la ventana
game_over = True #Mostrar pantalla de instrucciones
game_over_2 = False #Mostrar instructivos nivel 2 falso
game_over_3 = False  #Mostrar instructivos nivel 3 falso
game_over_4 = False  #Mostrar instructivos nivel 4 falso
esta_jugando = True #Saber si continúa el juego
#Definimos colores:
color_gris = (80,80,80) #Color gris
color_rojo = (255,0,0) #Color rojo 
color_azul = (0,0,255) #Color azul
color_verde = (0,100,0) #Color verde
color_negro = (0,0,0,) #Color negro
color_morado = (128,0,128) #Color morado
color_blanco = (255,255,255) #Color blanco
color_amarillo = (255,255,0) #Color amarillo
color_cafe = (130,65,0) #Color cafe
contador = 0 #Contador para definir velocidad
Score = 0 #Puntaje por partida
HighScore = 0 #El puntaje más alto
nivel1 = True #Está en nivel 1 
nivel2 = False #No está en nivel 2
nivel3 = False #No está en nivel 3
nivel4 = False #No está en nivel 4
ganador = False #No ha ganado
fondo = pygame.image.load("Complementos/universo.png") #Fondo de universo
fugaz = pygame.image.load("Complementos/estrella.png") #Estrella fugaz
fugazRect = fugaz.get_rect() #Obtenemos el objeto de la imagen, su contorno
speed_fugaz = [30, 30] #Velocidad de la estrella fugaz
pygame.mixer.music.load("Complementos/MusicaDeEspera_ChallengeColor.wav") #Guardar música de fondo para la sala de instrucciones
musica_juego = pygame.mixer.Sound("Complementos/MusicaJuego.wav") #Musica durante el juego
musica_ganador = pygame.mixer.Sound("Complementos/Musica_Ganador.wav") #Musica durante el final


#Textos para mostrar
fuente1 = pygame.font.Font(None, 60) #Tipo de letra y tamaño llamada fuente 1
fuente2 = pygame.font.Font(None, 30) #Tipo de letra y tamaño llamada fuente 2
fuente3 = pygame.font.Font(None, 20) #Tipo de letra y tamaño llamada fuente 3
#texto_TITULO = fuente1.render("COLOR CHALLENGE", 0, color_blanco)
titulo_C1 = fuente1.render("C", 0, color_verde) #Texto de la letra C con su color
titulo_O1 = fuente1.render("O", 0, color_verde) #Texto de la letra O con su color
titulo_L1 = fuente1.render("L", 0, color_rojo) #Texto de la letra L con su color
titulo_O2 = fuente1.render("O", 0, color_rojo) #Texto de la letra O con su color
titulo_R = fuente1.render("R", 0, color_gris) #Texto de la letra R con su color
titulo_C2 = fuente1.render("C", 0, color_gris) #Texto de la letra C con su color
titulo_H = fuente1.render("H", 0, color_azul) #Texto de la letra H con su color
titulo_A = fuente1.render("A", 0, color_azul) #Texto de la letra A con su color
titulo_L2 = fuente1.render("L", 0, color_amarillo) #Texto de la letra L con su color
titulo_L3 = fuente1.render("L", 0, color_amarillo) #Texto de la letra L con su color
titulo_E1 = fuente1.render("E", 0, color_morado) #Texto de la letra E con su color
titulo_N = fuente1.render("N", 0, color_morado) #Texto de la letra N con su color
titulo_G = fuente1.render("G", 0, color_cafe) #Texto de la letra G con su color
titulo_E2 = fuente1.render("E", 0, color_cafe) #Texto de la letra E con su color
texto_FI = fuente2.render("Flecha Izquierda = rojo", 0, color_rojo) #Texto que indica la flecha izquierda y su color
texto_FD = fuente2.render("Flecha Derecha = azul", 0, color_azul) #Texto que indica la flecha derecha y su color
texto_FS = fuente2.render("Flecha Superior = verde", 0, color_verde) #Texto que indica la flecha superior y su color
texto_SPACE = fuente1.render("Press SPACE", 0, color_gris) #Texto que indica persionar space y su color
texto_HS = fuente2.render("High Score", 0, color_blanco) #Texto que dice High Socre y su color
texto_S = fuente2.render("Score", 0, color_blanco) #Texto que dice Socre y su color
#texto 8 y 9 son para score y highcsore en números
texto_LEVEL2 = fuente1.render("LEVEL 2", 0, color_blanco) #Texto Nivel 2 y su color
texto_FIN = fuente2.render("Flecha Inferior = morado", 0, color_morado) #Texto que indica la flecha inferior y su color
texto_70 = fuente2.render("Alcanza 70 puntos para pasar al nivel 2", 0, color_blanco) #Texto de indicacion para pasar de nivel
texto_160 = fuente2.render("Alcanza 160 puntos para pasar al nivel 3", 0, color_blanco) #Texto de indicacion para pasar de nivel
texto_LEVEL3 = fuente1.render("LEVEL 3", 0, color_blanco) #Texto Nivel 3 y su color
texto_LA = fuente2.render("a = amarillo", 0, color_amarillo) #Texto que indica la letra con su color
texto_PISTA = fuente3.render("*El primer obstáculo y personaje inician en blanco*", 0, color_blanco) #Texto de indicacion de inicio de nivel
texto_270 = fuente2.render("Alcanza 270 puntos para pasar al nivel 4", 0, color_blanco) #Texto de indicacion para pasar de nivel
texto_LEVEL4 = fuente1.render("LEVEL 4", 0, color_blanco) #Texto Nivel 4 y su color
texto_400 = fuente2.render("Alcanza 400 puntos para ganar", 0, color_blanco) #Texto de indicacion para pasar de nivel
texto_LS = fuente2.render("s = cafe", 0, color_cafe)   #Texto que indica la letra con su color
texto_Creditos = fuente2.render("Programación: ", 0, color_blanco) #Texto: programación
texto_Creditos2 = fuente2.render("Música:", 0, color_blanco) #Texto: Música
texto_JuanPablo = fuente2.render("Juan Pablo Gómez Haro Cabrera", 0, color_blanco) #Texto que dice mi nimbre
texto_CreditosTitulo = fuente2.render("Créditos", 0, color_blanco) #Texto: Créditos

#Crreamos ventana, con el ancho y alto
ventana = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("COLOR CHALLENGE") #Nombre del juego (título)
clock = pygame.time.Clock() #Definimos clock para elegir los fps

#Personaje
#Lado del personaje
#La posición en el eje x,y
#Color inicial del jugador
Personaje_rect = {'jugador_tamaño':20, 'jugador_pos0':ANCHO/2, 'jugador_pos1':520, 'jugador_color': color_blanco} 


#Se atualiza un color aleatorio para el objeto
def Color_aleatorio(x, nivel):
	#Si el num es 1 y el nivel entre 1-4 regresa el color rojo
	if (x == 1 and nivel == 1) or (x == 1 and nivel == 2) or (x == 1 and nivel == 3) or (x == 1 and nivel == 4):
		return color_rojo
	#Si el num es 2 y el nivel entre 1-4 regresa el color azul
	if (x == 2 and nivel == 1) or (x == 2 and nivel == 2) or (x == 2 and nivel == 3) or (x == 2 and nivel == 4):
		return color_azul
	#Si el num es 3 y el nivel entre 1-4 regresa el color verde
	if (x == 3 and nivel == 1) or (x == 3 and nivel == 2) or (x == 3 and nivel == 3) or (x == 3 and nivel == 4):
		return color_verde
	#Si el num es 4 y el nivel entre 2-4 regresa el color morado
	if (x == 4 and nivel == 2) or (x == 4 and nivel == 3) or (x == 4 and nivel == 4):
		return color_morado
	#Si el num es 5 y el nivel entre 3-4 regresa el color amarillo
	if (x == 5 and nivel == 3) or (x == 5 and nivel == 4):
		return color_amarillo
	#Si el num es 6 y el nivel es 4 regresa el color cafe
	if (x == 6 and nivel == 4):
		return color_cafe




#Tener un fondo transparente: 
#black = pygame.Surface((ANCHO,ALTO))
#black.set_alpha(255)
#pygame.draw.rect(black, (0,0,0), black.get_rect(), 10)
#ventana.blit(black, (0, 0))

#Mostrar instrucciones antes del nivel 4
def MostrarNivel4():
	pygame.mixer.music.play(-1) #Activar múscica para las instrucciones
	black = pygame.Surface((ANCHO,ALTO)) #Definir imagen de fondo el ancho mismo que la ventana y alto mismo que la ventana
	black.set_alpha(200) # La imagen de fondo aparece un poco transárente
	pygame.draw.rect(black, color_negro, black.get_rect(), 10) #Ponemos en pantalla la imagen de fondo
	#Mostramos en pantalla textos e imagen
	ventana.blit(black, (0, 0)) #Actualizamos el fondo
	ventana.blit(texto_LEVEL4, (300,100)) #Level 4
	ventana.blit(texto_FI, (150,200)) #Flecha izquierda = rojo
	ventana.blit(texto_FD, (150,250)) #Flecha derecha = azul
	ventana.blit(texto_FS, (150,300)) #Flecha superior = verde
	ventana.blit(texto_FIN, (450,200)) #Flecha inferior = morado
	ventana.blit(texto_LA, (450,250)) #a = amarillo
	ventana.blit(texto_LS, (450,300)) #s = cafe
	ventana.blit(texto_SPACE, (260,350)) #Press space
	ventana.blit(texto_400, (200,500)) #Alcanza 400 puntos...
	ventana.blit(texto_PISTA, (240,550)) #El primer obstaculo blanco...
	pygame.display.update() #Actualizar frame con frame la ventana
	mostrar = True #Variable de estar mostrando en true
	while mostrar: #Mientras "mostrar" se verdadero se quedará aqui
		for event in pygame.event.get(): #Obtenemos todos los eventos que sucedan en la interfaz
			if event.type == pygame.QUIT: #Se cierra la ventana si el evento que recibe es cerrar la ventana
				sys.exit() #Cerrar ventana
			if event.type == pygame.KEYDOWN: #Se obtiene el evento si proviene del teclado
				if event.key == pygame.K_SPACE: #Si se pulsa "space" 
					mostrar = False #"Mostar" se convierte en falso y se sale de la función

#Mostrar instrucciones antes del nivel 3
def MostrarNivel3():
	pygame.mixer.music.play(-1) #Activar múscica para las instrucciones
	black = pygame.Surface((ANCHO,ALTO))#Definir imagen de fondo el ancho mismo que la ventana y alto mismo que la ventana
	black.set_alpha(200)# La imagen de fondo aparece un poco transárente
	pygame.draw.rect(black, color_negro, black.get_rect(), 10)#Ponemos en pantalla la imagen de fondo
	#Mostramos en pantalla textos e imagen
	ventana.blit(black, (0, 0))#Actualizamos el fondo
	ventana.blit(texto_LEVEL3, (300,100)) #Level 3
	ventana.blit(texto_FI, (150,200)) #Flecha izquierda = rojo
	ventana.blit(texto_FD, (150,250)) #Flecha derecha = azul
	ventana.blit(texto_FS, (150,300)) #Flecha superior = verde
	ventana.blit(texto_FIN, (450,200)) #Flecha inferior = morado
	ventana.blit(texto_LA, (450,250)) #a = amarillo
	ventana.blit(texto_SPACE, (260,350)) #Press space
	ventana.blit(texto_270, (200,500)) #Alcanza 270 puntos...
	ventana.blit(texto_PISTA, (240,550)) #El primer osbtáculo blanco...
	pygame.display.update()#Actualizar frame con frame la ventana
	mostrar = True#Variable de estar mostrando en true
	while mostrar:#Mientras "mostrar" se verdadero se quedará aqui
		for event in pygame.event.get():#Obtenemos todos los eventos que sucedan en la interfaz
			if event.type == pygame.QUIT:#Se cierra la ventana si el evento que recibe es cerrar la ventana
				sys.exit()#Cerrar ventana
			if event.type == pygame.KEYDOWN:#Se obtiene el evento si proviene del teclado
				if event.key == pygame.K_SPACE:#Si se pulsa "space"
					mostrar = False#"Mostar" se convierte en falso y se sale de la función


#Mostrar instrucciones antes del nivel 2
def MostrarNivel2():
	pygame.mixer.music.play(-1) #Activar múscica para las instrucciones
	black = pygame.Surface((ANCHO,ALTO))#Definir imagen de fondo el ancho mismo que la ventana y alto mismo que la ventana
	black.set_alpha(200)# La imagen de fondo aparece un poco transárente
	pygame.draw.rect(black, color_negro, black.get_rect(), 10)#Ponemos en pantalla la imagen de fondo
	#Mostramos en pantalla textos e imagen
	ventana.blit(black, (0, 0))#Actualizamos el fondo
	ventana.blit(texto_LEVEL2, (300,100)) #Level 2
	ventana.blit(texto_FI, (150,200)) #Flecha izquierda = rojo
	ventana.blit(texto_FD, (150,250)) #Flecha derecha = azul
	ventana.blit(texto_FS, (150,300)) #Flecha superior = verde
	ventana.blit(texto_FIN, (450,200)) #Flecha = inferior = morado
	ventana.blit(texto_SPACE, (260,350)) #Press space
	ventana.blit(texto_160, (200,500)) #Alcanza 160 puntos...
	ventana.blit(texto_PISTA, (240,550)) #El primero obstáculo blanco...
	pygame.display.update()#Actualizar frame con frame la ventana
	mostrar = True#Variable de estar mostrando en true
	while mostrar:#Mientras "mostrar" se verdadero se quedará aqui
		for event in pygame.event.get():#Obtenemos todos los eventos que sucedan en la interfaz
			if event.type == pygame.QUIT:#Se cierra la ventana si el evento que recibe es cerrar la ventana
				sys.exit()#Cerrar ventana
			if event.type == pygame.KEYDOWN:#Se obtiene el evento si proviene del teclado
				if event.key == pygame.K_SPACE:#Si se pulsa "space"
					mostrar = False #"Mostar" se convierte en falso y se sale de la función

#Mostrar instrucciones antes del nivel 1
def MostrarNivel1():
	pygame.mixer.music.play(-1) #Activar múscica para las instrucciones
	texto8 = fuente2.render(str(Score), 0, color_blanco) #Mostramos el puntaje
	texto9 = fuente2.render(str(HighScore), 0, color_blanco) #Mostramos el más alto
	ventana.fill(color_negro) #Pantalla negra
	#ventana.blit(texto_TITULO, (200,100)) #COLOR CHALLENGE
	ventana.blit(titulo_C1, (165,100)) #Mostrar letra C
	ventana.blit(titulo_O1, (195,100)) #Mostrar letra O
	ventana.blit(titulo_L1, (225,100)) #Mostrar letra L
	ventana.blit(titulo_O2, (255,100)) #Mostrar letra O
	ventana.blit(titulo_R, (285,100)) #Mostrar letra R
	ventana.blit(titulo_C2, (345,100)) #Mostrar letra C
	ventana.blit(titulo_H, (375,100)) #Mostrar letra H
	ventana.blit(titulo_A, (405,100)) #Mostrar letra A
	ventana.blit(titulo_L2, (435,100)) #Mostrar letra L
	ventana.blit(titulo_L3, (465,100)) #Mostrar letra L
	ventana.blit(titulo_E1, (495,100)) #Mostrar letra E
	ventana.blit(titulo_N, (525,100)) #Mostrar letra N
	ventana.blit(titulo_G, (555,100)) #Mostrar letra G
	ventana.blit(titulo_E2, (585,100)) #Mostrar letra E
	ventana.blit(texto_FI, (270,200)) #Flecha izquierda = rojo
	ventana.blit(texto_FD, (270,250)) #Flecha derecha = azul
	ventana.blit(texto_FS, (270,300)) #Flecha superior = verde
	ventana.blit(texto_SPACE, (260,350)) #Press space
	ventana.blit(texto_HS, (150,450)) # High Score
	ventana.blit(texto_S, (550,450)) # Score
	ventana.blit(texto8, (650,450)) # Número de score
	ventana.blit(texto9, (300,450)) #Número de high score
	ventana.blit(texto_70, (200,500)) #Alcanza 70 puntos...
	ventana.blit(texto_PISTA, (240,550)) #El primer obstáculo blanco...
	pygame.display.flip() #Actualizarlo
	mostrar = True  #Variable de estar mostrando en true
	while mostrar: #Mostrar esta ventana mientras no pulse Space
		clock.tick(30) #Frames por segundo
		for event in pygame.event.get(): #Obtenemos todos los eventos que sucedan en la interfaz
			if event.type == pygame.QUIT: #Se cierra la ventana si el evento que recibe es cerrar la ventana
				sys.exit() #Cerrar ventana
			if event.type == pygame.KEYDOWN: #Se obtiene el evento si proviene del teclado
				if event.key == pygame.K_SPACE: #Si se pulsa "space"
					mostrar = False  #"Mostar" se convierte en falso y se sale de la función


#Obstáculos
#Ancho y alto del obstaculo
#La posición en el eje x,y
#Color aleatorio, se manda el rango del color que queremos obtener y el nivel en el que se encuentra, por default es nivel 1 con los 3 primeros colores
Obstaculo_rect = {'obs_tamaño0':800, 'obs_tamaño1':20, 'obs_pos0':0, 'obs_pos1':400, 'obs_color':Color_aleatorio(random.randint(1,3), 1)} 

Obstaculo2_rect = {'obs_tamaño0':800, 'obs_tamaño1':20, 'obs_pos0':0, 'obs_pos1':200, 'obs_color':Color_aleatorio(random.randint(1,3), 1)} 

Obstaculo3_rect = {'obs_tamaño0':800, 'obs_tamaño1':20, 'obs_pos0':0, 'obs_pos1':0, 'obs_color':Color_aleatorio(random.randint(1,3), 1)}


#Loop mientras juego este activo
while esta_jugando:


	while game_over: #Inicio y cada derrota se reinician los obstáculos, conteo, puntaje, velocidad y actualizamos el High Score
		Obstaculo_rect['obs_pos1'] = 400 #Posicón inicial obstáculo 1
		Obstaculo2_rect['obs_pos1'] = 200 #Posicón inicial obstáculo 2
		Obstaculo3_rect['obs_pos1'] = 0 #Posicón inicial obstáculo 3
		Obstaculo_rect['obs_color'] = color_blanco   #Color inicial del osbtáculo 1 en blanco
		Obstaculo2_rect['obs_color'] = Color_aleatorio(random.randint(1,3), 1) #Color inicial del osbtáculo 2 en aleatorio
		Obstaculo3_rect['obs_color'] = Color_aleatorio(random.randint(1,3), 1) #Color inicial del osbtáculo 3 en aleatorio
		Personaje_rect['jugador_color'] = (255,255,255) #Color inicial del jugador en blanco 
		if Score > HighScore: #Si el score es mayor que high score
			HighScore = Score #Se guarda un nuevo high score
		MostrarNivel1() #Se llama la función mostrar instructivo del nivel 1
		speed = 6 #La velocidad se establece en el mínimo
		contador = 0 #Contador se reinicia a 0
		Score = 0 #Score se reinicia a 0
		nivel1 = True #Pasamos la variable del nivel 1 a verdader
		Personaje_rect['jugador_color'] = color_blanco #Se reinicia a color blanco el personaje
		game_over = False #Pasamo variable del game over a Falso

	#Al empezar el juego se quita la música
	if game_over == False:
		pygame.mixer.music.stop()
	#Se pone la segunda música que es la que suena durante los niveles
	if game_over == False and nivel1 == True:
		musica_juego.play()


	#Mientras estemos en nivel 1
	while nivel1:


		#Ventana color gris
		ventana.fill(color_negro)
		#Fondo del espacio 
		ventana.blit(fondo, (0,0))

		#Mover en pantalla un estrella fugaz, que rebote por fuera del escenario para que se vea continuamente
		fugazRect = fugazRect.move(speed_fugaz)
		#Si la imagen "estrella fugaz" topa con límite vertical rebotará con la misma velocidad pero inversa en el eje x
		if fugazRect.left < (-500) or fugazRect.right > (ANCHO + 500):
			speed_fugaz[0] = -speed_fugaz[0] #Velocidad en eje x inversa
		#Si la imagen "estrella fugaz" topa con límite horizontal rebotará con la misma velocidad pero inversa en el eje y
		if fugazRect.top < (-500) or fugazRect.bottom > (ALTO + 500):
			speed_fugaz[1] = -speed_fugaz[1] #Velocidad en eje y inversa

		ventana.blit(fugaz, fugazRect) #Mostrar en pantalla la estrella


		#Cuando haya pasado 70 obstáculos cambia de nivel
		if Score == 70:
			nivel1 = False #Se pone en false el nivel 1
			game_over_2 = True #Game over 2 true para mostrar instructivo 2
			Personaje_rect['jugador_color'] = color_blanco #Se reinicia a color blanco el personaje

		#Checamos si los obstáculos están en la  posición del jugador y verificamos el color de ambos
		if Obstaculo_rect['obs_pos1'] >=520 and Obstaculo_rect['obs_pos1'] <=540: #Posición del jugador entre 520-540
			if Personaje_rect['jugador_color'] != Obstaculo_rect['obs_color']: #Si los colores son distintos
				game_over = True #Se pone game over en verdaero
				nivel1 = False #Nivel 1 en falso
		#Checamos si los obstáculos están en la  posición del jugador y verificamos el color de ambos
		if Obstaculo2_rect['obs_pos1'] >=520 and Obstaculo2_rect['obs_pos1'] <=540: #Posición del jugador entre 520-540
			if Personaje_rect['jugador_color'] != Obstaculo2_rect['obs_color']: #Si los colores son distintos
				game_over = True #Se pone game over en verdadero
				nivel1 = False #Nivel 1 en falso
		#Checamos si los obstáculos están en la  posición del jugador y verificamos el color de ambos
		if Obstaculo3_rect['obs_pos1'] >=520 and Obstaculo3_rect['obs_pos1'] <=540: #Posición del jugador entre 520-540
			if Personaje_rect['jugador_color'] != Obstaculo3_rect['obs_color']: #Si los colores son distintos
				game_over = True #Game over en verdadero
				nivel1 = False #Nivel 1 en falso

		#Veolcidades de los obstáculos dependiendo la cantidad de obstáculos pasados
		if contador <= 7: #Contador igual o menor de 7
			speed = 6 #Velocidad 6
		if contador >= 7 and contador <= 14: #Contaador igual o mayor a 7 y menor o igual a 14
			speed = 8 #Velocidad 8
		if contador >= 14 and contador <= 21: #Contador igual o mayor a 14 y menor o igual a 21
			speed = 10 #Velocidad 10
		if contador >= 21 and contador <= 28: #Contador igual o mayor a 21 y menor o igual a 28
			speed = 12 # Velocidada 12
		if contador >= 28 and contador <= 35: #Contador igual o mayor a 28 y menor o igual a 35
			speed = 14 #Velocidad 14
		if contador >= 35 and contador <= 42:  #Contador igual o mayor a 35 y menor o igual a 42
			speed = 16 #Velocidad 16
		if contador >= 42 and contador <= 49:  #Contador igual o mayor a 42 y menor o igual a 49
			speed = 18 #Velocidad 18
		if contador >= 49: #Velocidad igual o mayor a 49
			speed = 20 #Velocidad 20

		#Si la posición está entre 0 y Alto de la ventana irá bajando el obstáculo a la velocidad marcada
		#Al llegar al limite sumamos 1 al contador
		#Cambiamos color del obstáculo aleatoriamente
		#Regresamos a su posición inicial
		if Obstaculo_rect['obs_pos1'] >= 0 and Obstaculo_rect['obs_pos1'] < ALTO:
			Obstaculo_rect['obs_pos1'] += speed #Sumarle la velocidad a la posición actual en y (para bajar rapido)
		else:
			Score += 1 #Sumamos uno a score
			contador += 1  #Sumamos uno a contador
			Obstaculo_rect['obs_color'] = Color_aleatorio(random.randint(1,3), 1)  #Nuevo color al obstáculo1 en aleatorio
			Obstaculo_rect['obs_pos0'] = Obstaculo_rect['obs_pos0']  #Colocar en posición x = a la que ya está (a lo ancho)
			Obstaculo_rect['obs_pos1'] = 0 #Colocar en posición de y=0 (hasta arriba)

		if Obstaculo2_rect['obs_pos1'] >= 0 and Obstaculo2_rect['obs_pos1'] < ALTO:
			Obstaculo2_rect['obs_pos1'] += speed #Sumarle la velocidad a la posición actual en y (para bajar rapido)
		else:
			Score += 1 #Sumamos uno a score
			contador += 1 #Sumamos uno a contador
			Obstaculo2_rect['obs_color'] = Color_aleatorio(random.randint(1,3), 1)  #Nuevo color al obstáculo1 en aleatorio
			Obstaculo2_rect['obs_pos0'] = Obstaculo2_rect['obs_pos0']  #Colocar en posición x = a la que ya está (a lo ancho)
			Obstaculo2_rect['obs_pos1'] = 0 #Colocar en posición de y=0 (hasta arriba)

		if Obstaculo3_rect['obs_pos1'] >= 0 and Obstaculo3_rect['obs_pos1'] < ALTO:
			Obstaculo3_rect['obs_pos1'] += speed #Sumarle la velocidad a la posición actual en y (para bajar rapido)
		else:
			Score += 1 #Sumamos uno a score
			contador += 1 #Sumamos uno a contador
			Obstaculo3_rect['obs_color'] = Color_aleatorio(random.randint(1,3), 1) #Nuevo color al obstáculo1 en aleatorio
			Obstaculo3_rect['obs_pos0'] = Obstaculo3_rect['obs_pos0'] #Colocar en posición x = a la que ya está (a lo ancho)
			Obstaculo3_rect['obs_pos1'] = 0 #Colocar en posición de y=0 (hasta arriba)

		#Dibujar jugador
		pygame.draw.rect(ventana, Personaje_rect['jugador_color'], #Ventana, color
						(Personaje_rect['jugador_pos0'],Personaje_rect['jugador_pos1'], #Posición en x(ancho), posición en y(alto)
						Personaje_rect['jugador_tamaño'],Personaje_rect['jugador_tamaño'])) #Tamaño en ancho, tamaño en alto

		#Dibujar obstáculos
		pygame.draw.rect(ventana, Obstaculo_rect['obs_color'],  #Ventana, color
						(Obstaculo_rect['obs_pos0'],Obstaculo_rect['obs_pos1'], #Posición en x(ancho), posición en y(alto)
						Obstaculo_rect['obs_tamaño0'],Obstaculo_rect['obs_tamaño1'])) #Tamaño en ancho, tamaño en alto

		pygame.draw.rect(ventana, Obstaculo2_rect['obs_color'],  #Ventana, color
						(Obstaculo2_rect['obs_pos0'],Obstaculo2_rect['obs_pos1'], #Posición en x(ancho), posición en y(alto)
						Obstaculo2_rect['obs_tamaño0'],Obstaculo2_rect['obs_tamaño1'])) #Tamaño en ancho, tamaño en alto

		pygame.draw.rect(ventana, Obstaculo3_rect['obs_color'],   #Ventana, color
						(Obstaculo3_rect['obs_pos0'],Obstaculo3_rect['obs_pos1'], #Posición en x(ancho), posición en y(alto)
						Obstaculo3_rect['obs_tamaño0'],Obstaculo3_rect['obs_tamaño1'])) #Tamaño en ancho, tamaño en alto

		#Detectar los eventos
		for event in pygame.event.get(): #Detectamos todos los eventos en la interfaz
			if event.type == pygame.QUIT: #Evento de cerrar la interfaz (X de la ventana)
				esta_jugando = False #Deja de jugar y se acaba el programa
			if event.type == pygame.KEYDOWN: #Se obtienen eventos del teclado
				color_actual = Personaje_rect['jugador_color'] #Guardamos el coloractual
				if event.key == pygame.K_LEFT: #Al apretar flecha izquierda
					color_actual = color_rojo #guardamos color rojo
				if event.key == pygame.K_RIGHT: #Al apretar flecha derecha
					color_actual = color_azul #guardamos color azul
				if event.key == pygame.K_UP: #Al apretar flecha arriba
					color_actual = color_verde #guardamos color verde
				Personaje_rect['jugador_color'] = color_actual #Se actualiza el nuevo color en el del personaje

		#Quitar música en cuanto pase al siguiente o pierda
		if (game_over == True) or (game_over_2 == True and game_over == False) or (game_over_3 == True and game_over == False) or (game_over_4 == True and game_over == False):
			musica_juego.stop()

		#Mostrar arriba el puntaje actualizado
		texto8 = fuente2.render(str(Score), 0, color_blanco)
		ventana.blit(texto8, (400,40)) #Ubicación del socre (x = 400, y = 40)
		#FPS
		clock.tick(30)
		pygame.display.update() #Actualizar el juego

######################################################################################################################


	#Game over del 2 (Instructivo)
	while game_over_2:
		Obstaculo_rect['obs_pos1'] = 400 #Iniciamos la posición del obstáculo 1
		Obstaculo2_rect['obs_pos1'] = 200 #Iniciamos la posición del obstáculo 2
		Obstaculo3_rect['obs_pos1'] = 0 #Iniciamos la posición del obstáculo 3
		Obstaculo_rect['obs_color'] = color_blanco    #El color del primer obstáculo 1 será blanco
		Obstaculo2_rect['obs_color'] = Color_aleatorio(random.randint(1,4), 2) #Color del obstáculo 2 en aleatorio con 4 posibilidades en nivel 2
		Obstaculo3_rect['obs_color'] = Color_aleatorio(random.randint(1,4), 2) #Color del obstáculo 3 en aleatorio con 4 posibilidades en nivel 2
		MostrarNivel2() #Mostrar instructivo del nivel 2
		contador = 0 #Contador se reinicia a 0
		speed = 6 #Velocidad se reinicia al mínimo
		nivel2 = True #Pasamos nivel dos a true para jugar
		Personaje_rect['jugador_color'] = color_blanco #Se reinicia a color blanco el personaje
		game_over_2 = False # Pasamos game over 2 a falso para quitar instructivo

	#Al empezar el juego se quita la música
	if game_over_2 == False:
		pygame.mixer.music.stop()
	#Suena la segunda música durante los niveles activos
	if game_over_2 == False and nivel2 == True:
			musica_juego.play()


	#Mientras sea nivel 2
	while nivel2:


		#Ventana color gris
		ventana.fill(color_negro)
		#Imagen del espacio de fondo
		ventana.blit(fondo, (0,0))

		#Mover en pantalla un estrella fugaz, que rebote por fuera del escenario para que se vea continuamente
		fugazRect = fugazRect.move(speed_fugaz)
		#Si la imagen "estrella fugaz" topa con límite vertical rebotará con la misma velocidad pero inversa en el eje x
		if fugazRect.left < (-500) or fugazRect.right > (ANCHO + 500):
			speed_fugaz[0] = -speed_fugaz[0] #Velocidad en eje x inversa
		#Si la imagen "estrella fugaz" topa con límite horizontal rebotará con la misma velocidad pero inversa en el eje y
		if fugazRect.top < (-500) or fugazRect.bottom > (ALTO + 500):
			speed_fugaz[1] = -speed_fugaz[1] #Velocidad en eje y inversa

		ventana.blit(fugaz, fugazRect) #Mostrar en pantalla la estrella

		#Cuando haya pasado 160 obstáculos cambia de nivel (70 del nivel 1 + 90 )
		if Score == 160: 
			nivel2 = False #Nivel 2 será falso para salir
			game_over_3 = True #Game over 3 verdadero para mostrar instructivo del nivel 3
			Personaje_rect['jugador_color'] = color_blanco #Reiniciamos el color del personaje a blanco

		#Checamos si los obstáculos están en la  posición del jugador y verificamos el color de ambos
		if Obstaculo_rect['obs_pos1'] >=520 and Obstaculo_rect['obs_pos1'] <=540: #Posición del personaje entre 520 y 540
			if Personaje_rect['jugador_color'] != Obstaculo_rect['obs_color']: #Si color del personaje y obstáculo 1 son diferentes
				game_over = True #Game over es verdadero papra mostrar instructivo principal
				nivel2 = False #Nivel 2 falso para salir

		if Obstaculo2_rect['obs_pos1'] >=520 and Obstaculo2_rect['obs_pos1'] <=540: #Posición del personaje entre 520 y 540
			if Personaje_rect['jugador_color'] != Obstaculo2_rect['obs_color']: #Si color del personaje y obstáculo 2 son diferentes
				game_over = True #Game over es verdadero papra mostrar instructivo principal
				nivel2 = False #Nivel 2 falso para salir

		if Obstaculo3_rect['obs_pos1'] >=520 and Obstaculo3_rect['obs_pos1'] <=540: #Posición del personaje entre 520 y 540
			if Personaje_rect['jugador_color'] != Obstaculo3_rect['obs_color']: #Si color del personaje y obstáculo 3 son diferentes
				game_over = True  #Game over es verdadero papra mostrar instructivo principal
				nivel2 = False #Nivel 2 falso para salir

		#Veolcidades de los obstáculos dependiendo la cantidad de obstáculos pasados
		if contador <= 7: #Contador menor o igual a 7
			speed = 6 #Velocidad 6
		if contador >= 7 and contador <= 14: #Contador igual o mayor a 7 y menor o igual a 14
			speed = 8 #Velocidad 8
		if contador >= 14 and contador <= 21: #Contador igual o mayor a 14 y menor o igual a 21
			speed = 10 #Velocidad 10
		if contador >= 21 and contador <= 28: #Contador igual o mayor a 21 y menor o igual a 28
			speed = 12 #Velocidad 12
		if contador >= 28 and contador <= 35: #Contador igual o mayor a 28 y menor o igual a 35
			speed = 14 #Velocidad 14
		if contador >= 35 and contador <= 42: #Contador igual o mayor a 35 y menor o igual a 42
			speed = 16 #Velocidad 16
		if contador >= 42 and contador <= 49: #Contador igual o mayor a 42 y menor o igual a 49
			speed = 18 #Velocidad 18
		if contador >= 49: #Contador igual o mayor a 49
			speed = 20 #Velocidad 20

		#Si la posición está entre 0 y Alto de la ventana irá bajando el obstáculo a la velocidad marcada
		#Al llegar al limite sumamos 1 al contador
		#Cambiamos color del obstáculo aleatoriamente
		#Regresamos a su posición inicial
		if Obstaculo_rect['obs_pos1'] >= 0 and Obstaculo_rect['obs_pos1'] < ALTO:
			Obstaculo_rect['obs_pos1'] += speed #Movimiento vertical del obstáculo 1 + velocidad
		else:
			Score += 1 #Score + 1
			contador += 1  #Contador + 1
			Obstaculo_rect['obs_color'] = Color_aleatorio(random.randint(1,4), 2)  #Color obstáculo 1 aleatorio, 4 opciones nivel 2
			Obstaculo_rect['obs_pos0'] = Obstaculo_rect['obs_pos0']  #Posición en el eje x la misma (ancho)
			Obstaculo_rect['obs_pos1'] = 0 #Posición del obstáculo 1 se reinicia a 0 (hasta arriba)

		if Obstaculo2_rect['obs_pos1'] >= 0 and Obstaculo2_rect['obs_pos1'] < ALTO:
			Obstaculo2_rect['obs_pos1'] += speed #Movimiento vertical del obstáculo 2 + velocidad
		else:
			Score += 1 #Score + 1
			contador += 1  #Contador + 1
			Obstaculo2_rect['obs_color'] = Color_aleatorio(random.randint(1,4), 2)  #Color obstáculo 2 aleatorio, 4 opciones nivel 2
			Obstaculo2_rect['obs_pos0'] = Obstaculo2_rect['obs_pos0']  #Posición en el eje x la misma (ancho)
			Obstaculo2_rect['obs_pos1'] = 0 #Posición del obstáculo 2 se reinicia a 0 (hasta arriba)

		if Obstaculo3_rect['obs_pos1'] >= 0 and Obstaculo3_rect['obs_pos1'] < ALTO:
			Obstaculo3_rect['obs_pos1'] += speed #Movimiento vertical del obstáculo 3 + velocidad
		else:
			Score += 1 #Score + 1
			contador += 1  #Contador + 1
			Obstaculo3_rect['obs_color'] = Color_aleatorio(random.randint(1,4), 2)  #Color obstáculo 3 aleatorio, 4 opciones nivel 2
			Obstaculo3_rect['obs_pos0'] = Obstaculo3_rect['obs_pos0']  #Posición en el eje x la misma (ancho)
			Obstaculo3_rect['obs_pos1'] = 0 #Posición del obstáculo 3 se reinicia a 0 (hasta arriba)

		#Dibujar jugador
		pygame.draw.rect(ventana, Personaje_rect['jugador_color'], #Pantalla, color
						(Personaje_rect['jugador_pos0'],Personaje_rect['jugador_pos1'], #Posición en x (ancho), posición en y (alto) 
						Personaje_rect['jugador_tamaño'],Personaje_rect['jugador_tamaño'])) #Tamaño en ancho y alto

		#Dibujar obstáculos
		pygame.draw.rect(ventana, Obstaculo_rect['obs_color'],  #Pantalla, color
						(Obstaculo_rect['obs_pos0'],Obstaculo_rect['obs_pos1'], #Posición en x (ancho), posición en y (alto)
						Obstaculo_rect['obs_tamaño0'],Obstaculo_rect['obs_tamaño1'])) #Tamaño en ancho y alto

		pygame.draw.rect(ventana, Obstaculo2_rect['obs_color'],  #Pantalla, color
						(Obstaculo2_rect['obs_pos0'],Obstaculo2_rect['obs_pos1'],
						Obstaculo2_rect['obs_tamaño0'],Obstaculo2_rect['obs_tamaño1'])) #Tamaño en ancho y alto

		pygame.draw.rect(ventana, Obstaculo3_rect['obs_color'],  #Pantalla, color
						(Obstaculo3_rect['obs_pos0'],Obstaculo3_rect['obs_pos1'], #Posición en x (ancho), posición en y (alto)
						Obstaculo3_rect['obs_tamaño0'],Obstaculo3_rect['obs_tamaño1'])) #Tamaño en ancho y alto

		#Detectar los eventos
		for event in pygame.event.get(): #Eventos de la interfaz
			if event.type == pygame.QUIT: #Evento de cerrar el juego (X de la ventana)
				sys.exit() #Se cierra sistema
			if event.type == pygame.KEYDOWN: #Eventos del teclado
				color_actual = Personaje_rect['jugador_color'] #Guardamos el coloractual
				if event.key == pygame.K_LEFT: #Al apretar flecha izquierda
					color_actual = color_rojo #Guardamos color rojo
				if event.key == pygame.K_RIGHT: #Al apretar flecha derecha
					color_actual = color_azul #Guardamos color azul
				if event.key == pygame.K_UP: #Al apretar flecha arriba
					color_actual = color_verde #Guardamos color verde
				if event.key == pygame.K_DOWN: #Al apretar flecha abajo
					color_actual = color_morado #Guardamos color morado
				Personaje_rect['jugador_color'] = color_actual #Se actualiza el nuevo color en el del personaje


		#Quitar música en cuanto pase al siguiente o pierda
		if (game_over == True) or (game_over_3 == True and game_over_2 == False) or (game_over_4 == True and game_over_2 == False):
			musica_juego.stop()

		#Mostrar arriba el puntaje actualizado
		texto8 = fuente2.render(str(Score), 0, color_blanco)
		ventana.blit(texto8, (400,40)) #Score hasta arriba de la pantalla, coordenadas (x,y)
		#FPS
		clock.tick(30)
		pygame.display.update() #Actualizar el juego

#################################################################################################################


	while game_over_3: #Mostrar mientras game over 3 sea verdadero
		Obstaculo_rect['obs_pos1'] = 400 #Posición inicial del obstáculo 1
		Obstaculo2_rect['obs_pos1'] = 200 #Posición inicial del obstáculo 2
		Obstaculo3_rect['obs_pos1'] = 0 #Posición inicial del osbtáculo 3
		Obstaculo_rect['obs_color'] = color_blanco   #Color inicial del obstáculo 1 es blanco
		Obstaculo2_rect['obs_color'] = Color_aleatorio(random.randint(1,5), 3) #Color obstáculo 2 aleatorio entre 1-5 en nivel 3
		Obstaculo3_rect['obs_color'] = Color_aleatorio(random.randint(1,5), 3) #Color obstáculo 3 aleatorio entre 1-5 en nivel 3
		MostrarNivel3() #Mostrar instructivo del nivel 3
		contador = 0 #Reiniciar el contador a 0
		speed = 6 #Reiniciar la velocidad a lo mínimo
		nivel3 = True #Nivel 3 verdadero para jugar
		Personaje_rect['jugador_color'] = color_blanco #Se reinicia a color blanco el personaje
		game_over_3 = False #Game over 3 falso para salir del instructivo

	#Al empezar el juego se quita la música
	if game_over_3 == False:
		pygame.mixer.music.stop()
	#Poner música 2 durante el nivel está en ejecución
	if game_over_3 == False and nivel3 == True:
			musica_juego.play()


	#Mientras sea nivel 3
	while nivel3:


		#Ventana color gris
		ventana.fill(color_negro)
		#Fondo del espacio
		ventana.blit(fondo, (0,0))

		#Mover en pantalla un estrella fugaz, que rebote por fuera del escenario para que se vea continuamente
		fugazRect = fugazRect.move(speed_fugaz)
		#Si la imagen "estrella fugaz" topa con límite vertical rebotará con la misma velocidad pero inversa en el eje x
		if fugazRect.left < (-500) or fugazRect.right > (ANCHO + 500):
			speed_fugaz[0] = -speed_fugaz[0] #La velocidad del eje x sera inversa
		#Si la imagen "estrella fugaz" topa con límite horizontal rebotará con la misma velocidad pero inversa en el eje y
		if fugazRect.top < (-500) or fugazRect.bottom > (ALTO + 500):
			speed_fugaz[1] = -speed_fugaz[1] #La velocidad del eje y sera inversa

		ventana.blit(fugaz, fugazRect) #Mostrar en pantalla la estrella

		#Cuando haya pasado 270 obstáculos cambia de nivel (70 nivel 1, 90 nivel 2 + 110)
		if Score == 270:
			nivel3 = False #nivel 3 falso para salir
			game_over_4 = True #game over 4 verdadero para mostrar instructivo del nivel 4
			Personaje_rect["jugador_color"] = color_blanco #Reiniciamos color personaje a blanco

		#Checamos si los obstáculos están en la  posición del jugador y verificamos el color de ambos
		if Obstaculo_rect['obs_pos1'] >=520 and Obstaculo_rect['obs_pos1'] <=540: #Posición del jugador entre 520 y 540
			if Personaje_rect['jugador_color'] != Obstaculo_rect['obs_color']: #Si color del personaje y obstáculo 1 son diferentes
				game_over = True #Game over true para reiniciar juego en instructivo principal
				nivel3 = False #Nivel 3 falso para salir

		if Obstaculo2_rect['obs_pos1'] >=520 and Obstaculo2_rect['obs_pos1'] <=540: #Posición del jugador entre 520 y 540
			if Personaje_rect['jugador_color'] != Obstaculo2_rect['obs_color']: #Si color del personaje y obstáculo 2 son diferentes
				game_over = True #Game over true para reiniciar juego en instructivo principal
				nivel3 = False #Nivel 3 falso para salir

		if Obstaculo3_rect['obs_pos1'] >=520 and Obstaculo3_rect['obs_pos1'] <=540: #Posición del jugador entre 520 y 540
			if Personaje_rect['jugador_color'] != Obstaculo3_rect['obs_color']: #Si color del personaje y obstáculo 3 son diferentes
				game_over = True #Game over true para reiniciar juego en instructivo principal
				nivel3 = False  #Nivel 3 falso para salir

		#Veolcidades de los obstáculos dependiendo la cantidad de obstáculos pasados
		if contador <= 7: #Contador menor o igual a 7
			speed = 6 #Velocidad 6
		if contador >= 7 and contador <= 14: #Contador igual o mayor a 7 y menor o igual a 14
			speed = 8 #Velocidad 8
		if contador >= 14 and contador <= 21: #Contador igual o mayor a 14 y menor o igual a 21
			speed = 10 #Velocidad 10
		if contador >= 21 and contador <= 28: #Contador igual o mayor a 21 y menor o igual a 28
			speed = 12 #Velocidad 12
		if contador >= 28 and contador <= 35: #Contador igual o mayor a 28 y menor o igual a 35
			speed = 14 #Velocidad 14
		if contador >= 35 and contador <= 42: #Contador igual o mayor a 35 y menor o igual a 42
			speed = 16 #Velocidad 16
		if contador >= 42 and contador <= 49: #Contador igual o mayor a 42 y menor o igual a 49
			speed = 18 #Velocidad 18
		if contador >= 49: #Contador igual o mayor a 49
			speed = 20 #Velocidad 20

		#Si la posición está entre 0 y Alto de la ventana irá bajando el obstáculo a la velocidad marcada
		#Al llegar al limite sumamos 1 al contador
		#Cambiamos color del obstáculo aleatoriamente
		#Regresamos a su posición inicial
		if Obstaculo_rect['obs_pos1'] >= 0 and Obstaculo_rect['obs_pos1'] < ALTO:
			Obstaculo_rect['obs_pos1'] += speed #Posición del obstáculo 1 mas la velocidad
		else:
			Score += 1 #Score mas 1
			contador += 1 #Contador mas 1
			Obstaculo_rect['obs_color'] = Color_aleatorio(random.randint(1,5), 3)  #Color obstáculo 1 aleatorio, 5 opciones nivel 3
			Obstaculo_rect['obs_pos0'] = Obstaculo_rect['obs_pos0'] #Posición en el eje x igual (ancho)
			Obstaculo_rect['obs_pos1'] = 0 #Posición en el eje y se reinciia a 0 (hasta arriba)

		if Obstaculo2_rect['obs_pos1'] >= 0 and Obstaculo2_rect['obs_pos1'] < ALTO:
			Obstaculo2_rect['obs_pos1'] += speed #Posición del obstáculo 2 mas la velocidad
		else:
			Score += 1 #Score mas 1
			contador += 1  #Contador mas 1
			Obstaculo2_rect['obs_color'] = Color_aleatorio(random.randint(1,5), 3)  #Color obstáculo 2 aleatorio, 5 opciones nivel 3
			Obstaculo2_rect['obs_pos0'] = Obstaculo2_rect['obs_pos0']  #Posición en el eje x igual (ancho)
			Obstaculo2_rect['obs_pos1'] = 0 #Posición en el eje y se reinciia a 0 (hasta arriba)

		if Obstaculo3_rect['obs_pos1'] >= 0 and Obstaculo3_rect['obs_pos1'] < ALTO:
			Obstaculo3_rect['obs_pos1'] += speed #Posición del obstáculo 3 mas la velocidad
		else:
			Score += 1 #Score mas 1
			contador += 1  #Contador mas 1
			Obstaculo3_rect['obs_color'] = Color_aleatorio(random.randint(1,5), 3)  #Color obstáculo 3 aleatorio, 5 opciones nivel 3
			Obstaculo3_rect['obs_pos0'] = Obstaculo3_rect['obs_pos0']   #Posición en el eje x igual (ancho)
			Obstaculo3_rect['obs_pos1'] = 0 #Posición en el eje y se reinciia a 0 (hasta arriba)

		#Dibujar jugador
		pygame.draw.rect(ventana, Personaje_rect['jugador_color'], #Pantalla, color
						(Personaje_rect['jugador_pos0'],Personaje_rect['jugador_pos1'],  #Posición en x y posición en y
						Personaje_rect['jugador_tamaño'],Personaje_rect['jugador_tamaño'])) #Tamaño en ancho y alto

		#Dibujar obstáculos
		pygame.draw.rect(ventana, Obstaculo_rect['obs_color'],  #Pantalla, color
						(Obstaculo_rect['obs_pos0'],Obstaculo_rect['obs_pos1'], #Posición en x y posición en y
						Obstaculo_rect['obs_tamaño0'],Obstaculo_rect['obs_tamaño1'])) #Tamaño en ancho y alto

		pygame.draw.rect(ventana, Obstaculo2_rect['obs_color'],  #Pantalla, color
						(Obstaculo2_rect['obs_pos0'],Obstaculo2_rect['obs_pos1'], #Posición en x y posición en y
						Obstaculo2_rect['obs_tamaño0'],Obstaculo2_rect['obs_tamaño1'])) #Tamaño en ancho y alto

		pygame.draw.rect(ventana, Obstaculo3_rect['obs_color'],  #Pantalla, color
						(Obstaculo3_rect['obs_pos0'],Obstaculo3_rect['obs_pos1'], #Posición en x y posición en y
						Obstaculo3_rect['obs_tamaño0'],Obstaculo3_rect['obs_tamaño1'])) #Tamaño en ancho y alto

		#Detectar los eventos
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: #Si el evento es cerrar (X en la pantalla)
				sys.exit() #Cerrar programa
			if event.type == pygame.KEYDOWN: #Eventos en el teclado
				color_actual = Personaje_rect['jugador_color'] #Guardamos el coloractual
				if event.key == pygame.K_LEFT: #Al apretar flecha izquierda
					color_actual = color_rojo #Guardamos el color rojo
				if event.key == pygame.K_RIGHT: #Al apretar flecha derecha
					color_actual = color_azul #Guardamos el color azul
				if event.key == pygame.K_UP: #Al apretar flecha arriba
					color_actual = color_verde #Guardamos el color verde
				if event.key == pygame.K_DOWN: #Al apretar flecha abajo
					color_actual = color_morado #Guardamos el color morado
				if event.key == pygame.K_a: #Al apretar letra a
					color_actual = color_amarillo #Guardamos el color amarillo
				Personaje_rect['jugador_color'] = color_actual #Se actualiza el nuevo color en el del personaje


		#Quitar música en cuanto pase al siguiente o pierda
		if game_over == True or (game_over_4 == True and game_over_3 == False):
			musica_juego.stop()

		#Mostrar arriba el puntaje actualizado
		texto8 = fuente2.render(str(Score), 0, color_blanco)
		ventana.blit(texto8, (400,40)) #Score hasta arriba en coordenadas (x,y)
		#FPS
		clock.tick(30)
		pygame.display.update() #Actualizar el juego

#################################################################################################################

	#Mientras sea game over 4
	while game_over_4:
		Obstaculo_rect['obs_pos1'] = 400 #Posición inicial del obstáculo 1
		Obstaculo2_rect['obs_pos1'] = 200 #Posición inicial del obstáculo 2
		Obstaculo3_rect['obs_pos1'] = 0 #Posición inicial del obstáculo 3
		Obstaculo_rect['obs_color'] = color_blanco   #Color inicial del obstáculo 1 blanco
		Obstaculo2_rect['obs_color'] = Color_aleatorio(random.randint(1,6), 4) #Color obstáculo 2 aleatorio, 6 opciones nivel 4
		Obstaculo3_rect['obs_color'] = Color_aleatorio(random.randint(1,6), 4) #Color obstáculo 3 aleatorio, 6 opciones nivel 4
		MostrarNivel4() #Mostrar instructivo del nivel 4
		contador = 0 #Reiniciamos contador a 0
		speed = 6 #Reiniciamos velocidad al mínimo
		nivel4 = True #Nivel 4 verdadero para jugar
		game_over_4 = False #Game over 4 falso para salir del instructivo

	#Al empezar el juego se quita la música
	if game_over_4 == False:
		pygame.mixer.music.stop()
	#Poner segunda música durante el nivel activo
	if game_over_4 == False and nivel4 == True:
			musica_juego.play()


	#Mientras sea nivel 3
	while nivel4:


		#Ventana color gris
		ventana.fill(color_negro)
		#Fondo del espacio
		ventana.blit(fondo, (0,0))

		#Mover en pantalla un estrella fugaz, que rebote por fuera del escenario para que se vea continuamente
		fugazRect = fugazRect.move(speed_fugaz)
		#Si la imagen "estrella fugaz" topa con límite vertical rebotará con la misma velocidad pero inversa en el eje x
		if fugazRect.left < (-500) or fugazRect.right > (ANCHO + 500):
			speed_fugaz[0] = -speed_fugaz[0] #Velocidad del eje x será inversa
		#Si la imagen "estrella fugaz" topa con límite horizontal rebotará con la misma velocidad pero inversa en el eje y
		if fugazRect.top < (-500) or fugazRect.bottom > (ALTO + 500):
			speed_fugaz[1] = -speed_fugaz[1] #Velocidad del eje y será inversa

		ventana.blit(fugaz, fugazRect) #Mostrar en pantalla la estrella

		#Cuando haya pasado 400 obstáculos ganará el juego (70 nivel 1, 90 nivel 2, 110 nivel 3 + 130)
		if Score == 400:
			nivel4 = False #Nivel 4 falso para salir del k}juego
			ganador = True #Ganador verdadero para mostrar pantalla de victoria

		#Checamos si los obstáculos están en la  posición del jugador y verificamos el color de ambos
		if Obstaculo_rect['obs_pos1'] >=520 and Obstaculo_rect['obs_pos1'] <=540: #Personaje en posición entre 520 y 540
			if Personaje_rect['jugador_color'] != Obstaculo_rect['obs_color']: #Si el color del personaje y obstáculo 1 son diferentes
				game_over = True #Game over verdadero para reiniciar y mostrar instructivo del nivel 1
				nivel4 = False #Nivel 4 falso para salir

		if Obstaculo2_rect['obs_pos1'] >=520 and Obstaculo2_rect['obs_pos1'] <=540: #Personaje en posición entre 520 y 540
			if Personaje_rect['jugador_color'] != Obstaculo2_rect['obs_color']: #Si el color del personaje y obstáculo 2 son diferentes
				game_over = True #Game over verdadero para reiniciar y mostrar instructivo del nivel 1
				nivel4 = False #Nivel 4 falso para salir

		if Obstaculo3_rect['obs_pos1'] >=520 and Obstaculo3_rect['obs_pos1'] <=540: #Personaje en posición entre 520 y 540
			if Personaje_rect['jugador_color'] != Obstaculo3_rect['obs_color']: #Si el color del personaje y obstáculo 3 son diferentes
				game_over = True #Game over verdadero para reiniciar y mostrar instructivo del nivel 1
				nivel4 = False  #Nivel 4 falso para salir

		#Veolcidades de los obstáculos dependiendo la cantidad de obstáculos pasados
		if contador <= 7: #Contador menor o igual a 7
			speed = 6 #Velocidad 6
		if contador >= 7 and contador <= 14: #Contador igual o mayor a 7 y menor o igual a 14
			speed = 8 #Velocidad 8
		if contador >= 14 and contador <= 21: #Contador igual o mayor a 14 y menor o igual a 21
			speed = 10 #Velocidad 10
		if contador >= 21 and contador <= 28: #Contador igual o mayor a 21 y menor o igual a 28
			speed = 12 #Velocidad 12
		if contador >= 28 and contador <= 35: #Contador igual o mayor a 28 y menor o igual a 35
			speed = 14 #Velocidad 14
		if contador >= 35 and contador <= 42: #Contador igual o mayor a 35 y menor o igual a 42
			speed = 16 #Velocidad 16
		if contador >= 42 and contador <= 49: #Contador igual o mayor a 42 y menor o igual a 49
			speed = 18 #Velocidad 18
		if contador >= 49: #Contador igual o mayor a 49
			speed = 20 #Velocidad 20

		#Si la posición está entre 0 y Alto de la ventana irá bajando el obstáculo a la velocidad marcada
		#Al llegar al limite sumamos 1 al contador
		#Cambiamos color del obstáculo aleatoriamente
		#Regresamos a su posición inicial
		if Obstaculo_rect['obs_pos1'] >= 0 and Obstaculo_rect['obs_pos1'] < ALTO:
			Obstaculo_rect['obs_pos1'] += speed #Posición del obstáculo 1 en y más velocidad
		else:
			Score += 1 #Score más 1
			contador += 1  #Contador más 1
			Obstaculo_rect['obs_color'] = Color_aleatorio(random.randint(1,6), 4)  #Color obstáculo 1 aleatorio, 6 opciones nivel 4
			Obstaculo_rect['obs_pos0'] = Obstaculo_rect['obs_pos0']  #Misma posición en eje x (ancho)
			Obstaculo_rect['obs_pos1'] = 0 #Se reinicia posici´no eje y a 0 (vertical / alto) obstáculo 1

		if Obstaculo2_rect['obs_pos1'] >= 0 and Obstaculo2_rect['obs_pos1'] < ALTO:
			Obstaculo2_rect['obs_pos1'] += speed #Posición del obstáculo 2 en y más velocidad
		else:
			Score += 1 #Score más 1
			contador += 1  #Contador más 1
			Obstaculo2_rect['obs_color'] = Color_aleatorio(random.randint(1,6), 4)  #Color obstáculo 2 aleatorio, 6 opciones nivel 4
			Obstaculo2_rect['obs_pos0'] = Obstaculo2_rect['obs_pos0']  #Misma posición en eje x (ancho)
			Obstaculo2_rect['obs_pos1'] = 0 #Se reinicia posici´no eje y a 0 (vertical / alto) obstáculo 2

		if Obstaculo3_rect['obs_pos1'] >= 0 and Obstaculo3_rect['obs_pos1'] < ALTO:
			Obstaculo3_rect['obs_pos1'] += speed #Posición del obstáculo 3 en y más velocidad
		else:
			Score += 1 #Score más 1
			contador += 1  #Contador más 1
			Obstaculo3_rect['obs_color'] = Color_aleatorio(random.randint(1,6), 4)  #Color obstáculo 3 aleatorio, 6 opciones nivel 4
			Obstaculo3_rect['obs_pos0'] = Obstaculo3_rect['obs_pos0']  #Misma posición en eje x (ancho)
			Obstaculo3_rect['obs_pos1'] = 0 #Se reinicia posici´no eje y a 0 (vertical / alto) obstáculo 3

		#Dibujar jugador
		pygame.draw.rect(ventana, Personaje_rect['jugador_color'], #Pantalla, color
						(Personaje_rect['jugador_pos0'],Personaje_rect['jugador_pos1'],  #Posición en x,y 
						Personaje_rect['jugador_tamaño'],Personaje_rect['jugador_tamaño'])) #Tamaño ancho y alto

		#Dibujar obstáculos
		pygame.draw.rect(ventana, Obstaculo_rect['obs_color'],  #Pantalla, color
						(Obstaculo_rect['obs_pos0'],Obstaculo_rect['obs_pos1'], #Posición en x,y
						Obstaculo_rect['obs_tamaño0'],Obstaculo_rect['obs_tamaño1'])) #Tamaño ancho y alto

		pygame.draw.rect(ventana, Obstaculo2_rect['obs_color'],  #Pantalla, color
						(Obstaculo2_rect['obs_pos0'],Obstaculo2_rect['obs_pos1'], #Posición en x,y
						Obstaculo2_rect['obs_tamaño0'],Obstaculo2_rect['obs_tamaño1'])) #Tamaño ancho y alto

		pygame.draw.rect(ventana, Obstaculo3_rect['obs_color'],  #Pantalla, color
						(Obstaculo3_rect['obs_pos0'],Obstaculo3_rect['obs_pos1'], #Posición en x,y
						Obstaculo3_rect['obs_tamaño0'],Obstaculo3_rect['obs_tamaño1'])) #Tamaño ancho y alto

		#Detectar los eventos
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: #Evento de cerrar (X de cerrar ventana)
				sys.exit() #Se cierra el programa
			if event.type == pygame.KEYDOWN: #Eventos del teclado
				color_actual = Personaje_rect['jugador_color'] #Guardamos el coloractual
				if event.key == pygame.K_LEFT: #Al apretar flecha izquierda
					color_actual = color_rojo #Se guarda color rojo
				if event.key == pygame.K_RIGHT: #Al apretar flecha derecha
					color_actual = color_azul #Se guarda color azul
				if event.key == pygame.K_UP: #Al apretar flecha arriba
					color_actual = color_verde #Se guarda color verde
				if event.key == pygame.K_DOWN: #Al apretar flecha abajo
					color_actual = color_morado #Se guarda color morado
				if event.key == pygame.K_a: #Al apretar letra a
					color_actual = color_amarillo #Se guarda color amarillo
				if event.key == pygame.K_s: #Al apretar letra s
					color_actual = color_cafe #Se guarda color cafe
				Personaje_rect['jugador_color'] = color_actual #Se actualiza el nuevo color en el del personaje


		#Quitar música en cuanto pase al siguiente o pierda
		if (game_over == True) or (game_over_4 == False and ganador == True):
			musica_juego.stop()

		#Mostrar arriba el puntaje actualizado
		texto8 = fuente2.render(str(Score), 0, color_blanco)
		ventana.blit(texto8, (400,40)) #Aparece score hasta arriba
		#FPS
		clock.tick(30)
		pygame.display.update() #Actualizar el juego

#########################################################################################################

	#Si ganador es verdadero y en game over 4 falso se reproducirá la 3 musica
	if ganador == True and game_over_4 == False:
		musica_ganador.play()
 
	while ganador: #Mientras ganador sea verdadero
		fuente4 = pygame.font.Font(None, 100) #Creamos una cuarta fuente para textos
		texto_Victoria = fuente4.render("¡GANADOR!", 0, color_blanco) #Creamos texto "GANADOR" con color blanco

		#Ventana color gris
		ventana.fill(color_negro)
		ventana.blit(fondo, (0,0)) #Fondo de espacio
		ventana.blit(texto_Victoria, (200, 100)) #Ganador
		ventana.blit(texto_CreditosTitulo, (350, 200)) #Creditos
		ventana.blit(texto_Creditos, (330, 250)) #Programacion:
		ventana.blit(texto_JuanPablo, (250,300)) #Juan Pablo
		ventana.blit(texto_Creditos2, (360, 350)) #Musica
		ventana.blit(texto_JuanPablo, (250,400)) #Juan Pablo
		ventana.blit(texto_SPACE, (260, 500)) #Press space

		for event in pygame.event.get(): #Obtener eventos de la interfaz
			if event.type == pygame.QUIT: #Evento de cerrar  (x de la pantalla)
				sys.exit() #Cerrar programa
			if event.type == pygame.KEYDOWN: #Evento del teclado
				if event.key == pygame.K_SPACE: #Apretar SPACE
					game_over = True #Game over será verdadero para ir al instructivo principal
					musica_ganador.stop() #Paramos música 3
					ganador = False #Ganador falso para sallir 


		clock.tick(30) #Frames por segundo
		pygame.display.update() #Actualizar el juego