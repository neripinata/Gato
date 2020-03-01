import pygame
background_colour = (255,255,255)
black = (0,0,0)
(width, height) = (300, 300)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Gato')
screen.fill(background_colour)

#Dibujar tablero
pygame.draw.line(screen, black, (25,100), (275,100), 4)
pygame.draw.line(screen, black, (25,200), (275,200), 4)
pygame.draw.line(screen, black, (100,25), (100,275), 4)
pygame.draw.line(screen, black, (200 ,25), (200,275), 4)
pygame.display.flip()

#posiciones 
center = (150, 150)
left_top = (50, 50)
center_top = (150, 50)
right_top = (250, 50)
left_center = (50, 150)
right_center = (250, 150)
left_down = (50, 250)
right_down = (250, 250)
center_down = center = (150, 250)

running = True


pygame.draw.circle(screen, black, center_down , 45)
pygame.display.flip()

posiciones = [0,0,0,0,0,0,0,0,0]

while running:
  for event in pygame.event.get():

    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      if (pos[0] > 0 and pos[0] < 90) and (pos[1] > 0 and pos[1] < 90) and posiciones[0] == 0:
        pygame.draw.circle(screen, black, left_top , 45)
        pygame.display.flip()
        posiciones[0] = 1
      if (pos[0] > 90 and pos[0] < 180) and (pos[1] > 0 and pos[1] < 90) and posiciones[1] == 0:
        pygame.draw.circle(screen, black, center_top , 45)
        pygame.display.flip()
        posiciones[1] = 1

      print(pos)

    if event.type == pygame.QUIT:
      running = False