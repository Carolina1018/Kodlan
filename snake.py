import pygame, sys
from pygame.math import Vector2
import random, time

pygame.init()


alto = 480
ancho = 720

# Crear ventana
screen = pygame.display.set_mode((ancho,alto))

punt = pygame.font.SysFont("Russo One",20)


class Snake:

	#Crear snake
	def __init__(self):
		self.body = [Vector2(20,200),Vector2(20,120),Vector2(20,120)]
		self.direction = Vector2(0,-20)
		self.add = False

	#Dibujar snake
	def dibujar(self):
		for bloque in self.body:
			pygame.draw.rect(screen,(69,139,0),(bloque.x,bloque.y,20,20))

	#Mover snake
	def mover(self):
		if self.add == True:
			copia = self.body
			copia.insert(0,copia[0] + self.direction)
			self.body = copia[:]
			self.add = False
		else:
			copia = self.body[:-1]
			copia.insert(0,copia[0] + self.direction)
			self.body = copia[:]


	#Move arriba
	def mover_arriba(self):
		self.direction = Vector2(0,-20)

	#Move abajo
	def mover_abajo(self):
		self.direction = Vector2(0,20)

	#Move derecha
	def mover_derecha(self):
		self.direction = Vector2(20,0)

	#Move izquierda
	def mover_izquierda(self):
		self.direction = Vector2(-20,0)

	def muerte(self):

		#Condicion cuando toca los bordes
		if self.body[0].x >= ancho + 20 or self.body[0].y >= alto + 20 or self.body[0].x <= -20 or self.body[0].y <= -20:
			return True

		#Condicion cuando se toca a si misma
		for i in self.body[1:]:
			if self.body[0] == i:
				return True


class Manzana:

	def __init__(self):
		self.generate()


	def dibujar(self):
		pygame.draw.rect(screen,(255,0,0),(self.pos.x,self.pos.y,20,20))

	def generate(self):
		self.x = random.randrange(0,ancho/20)
		self.y = random.randrange(0,alto/20)
		self.pos = Vector2(self.x*20, self.y*20)

	def colision(self,snake):

		if snake.body[0] ==  self.pos:
			self.generate()
			snake.add = True
			return True

		for bloque in snake.body[1:]:
			if bloque == self.pos:
				self.generate()

		return False


class Enemigo:

	def __init__(self):
		self.generate()


	def dibujar(self):
		pygame.draw.rect(screen,(139,20,80),(self.pos.x,self.pos.y,20,20))

	def generate(self):
		self.x = random.randrange(0,ancho/20)
		self.y = random.randrange(0,alto/20)
		self.pos = Vector2(self.x*20, self.y*20)

	def muerte(self,snake):

		if snake.body[0] == self.pos:
			return True

		

def main(): 

	snake = Snake()
	manzana = Manzana()
	enemigo = Enemigo()
	puntaje = 0

	tiempo = pygame.time.Clock()

	while True:

		tiempo.tick(10)

		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				sys.exit()

			#Moviento hacia arriba
			if event.type == pygame.KEYDOWN and snake.direction.y != 20:
				if event.key == pygame.K_UP:
					snake.mover_arriba()

			#Moviento hacia abajo
			if event.type == pygame.KEYDOWN and snake.direction.y != -20:
				if event.key == pygame.K_DOWN:
					snake.mover_abajo()

			#Moviento hacia la derecha
			if event.type == pygame.KEYDOWN and snake.direction.x != -20:
				if event.key == pygame.K_RIGHT:
					snake.mover_derecha()

			#Moviento hacia la izquierda
			if event.type == pygame.KEYDOWN and snake.direction.x != 20:
				if event.key == pygame.K_LEFT:
					snake.mover_izquierda()

		screen.fill((175,215,70))
		snake.dibujar()
		snake.mover()
		manzana.dibujar()
		enemigo.dibujar()

		if manzana.colision(snake):
			puntaje += 1

		if snake.muerte():
			pygame.time.delay
			fuente = pygame.font.Font(None, 40)
			perdio = "GAME OVER"
			screen.blit(fuente.render(perdio,1,(255,255,255)),((ancho/2)-90,(alto/2)-40))
		
		if enemigo.muerte(snake):
			quit()	

		
	


		mensaje = punt.render("Puntaje: {}".format(puntaje),1,(255,255,255))
		screen.blit(mensaje,(ancho-mensaje.get_width()-30,20))

		pygame.display.update()
		 	
main()