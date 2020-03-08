import pygame
background_colour = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
(width, height) = (300, 300)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Gato')
screen.fill(background_colour)

turn_circle = True

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

def CheckWinning(posiciones):
  posiciones = posiciones

  if posiciones[0] == posiciones[1]  and posiciones[1]== posiciones [2] and posiciones[0] != 0:
    if posiciones[0] == 1:
      print("Gana circulo negro")
    else:
      print("Gana circulo rojo")  

  if posiciones[3] == posiciones[4]  and posiciones[4]== posiciones [5] and posiciones[3] != 0:
    if posiciones[3] == 1:
      print("Gana circulo negro")
    else:
      print("Gana circulo rojo")  


#pygame.draw.circle(screen, black, center_down , 45)
pygame.display.flip()

posiciones = [0,0,0,0,0,0,0,0,0]

while running:
  for event in pygame.event.get():

    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      #Top left
      if (pos[0] > 0 and pos[0] < 90) and (pos[1] > 0 and pos[1] < 90) and posiciones[0] == 0:
        if turn_circle == True:
          pygame.draw.circle(screen, black, left_top , 45)
          posiciones[0] = 1
          turn_circle = False
        elif turn_circle == False:
          pygame.draw.circle(screen, red, left_top , 45)
          posiciones[0] = 2
          turn_circle = True
        pygame.display.flip()
      #top center
      if (pos[0] > 90 and pos[0] < 180) and (pos[1] > 0 and pos[1] < 90) and posiciones[1] == 0:
        if turn_circle == True:
          pygame.draw.circle(screen, black, center_top , 45)
          posiciones[1] = 1
          turn_circle = False
        elif turn_circle == False:
          pygame.draw.circle(screen, red, center_top , 45)
          posiciones[1] = 2
          turn_circle = True
        pygame.display.flip()
      #top right
      if (pos[0] > 180 and pos[0] < 300) and (pos[1] > 0 and pos[1] < 90) and posiciones[2] == 0:
        if turn_circle == True:
          pygame.draw.circle(screen, black, right_top , 45)
          posiciones[2] = 1
          turn_circle = False
        elif turn_circle == False:
          pygame.draw.circle(screen, red, right_top , 45)
          posiciones[2] = 2
          turn_circle = True

        pygame.display.flip()




      #center left
      if (pos[0] > 0 and pos[0] < 90) and (pos[1] > 90 and pos[1] < 180) and posiciones[3] == 0:
        if turn_circle == True:
          pygame.draw.circle(screen, black, left_center , 45)
          posiciones[3] = 1
          turn_circle = False
        elif turn_circle == False:
          pygame.draw.circle(screen, red, left_center , 45)
          posiciones[3] = 2
          turn_circle = True
        pygame.display.flip()
      # center
      if (pos[0] > 90 and pos[0] < 180) and (pos[1] > 90 and pos[1] < 180) and posiciones[4] == 0:
        if turn_circle == True:
          pygame.draw.circle(screen, black, (150,150) , 45)
          posiciones[4] = 1
          turn_circle = False
        elif turn_circle == False:
          pygame.draw.circle(screen, red, (150,150) , 45)
          posiciones[4] = 2
          turn_circle = True
        pygame.display.flip()
      #center right
      if (pos[0] > 180 and pos[0] < 300) and (pos[1] > 90 and pos[1] < 180) and posiciones[5] == 0:
        if turn_circle == True:
          pygame.draw.circle(screen, black, right_center , 45)
          posiciones[5] = 1
          turn_circle = False
        elif turn_circle == False:
          pygame.draw.circle(screen, red, right_center , 45)
          posiciones[5] = 2
          turn_circle = True
        pygame.display.flip()

      


      #center left
      if (pos[0] > 0 and pos[0] < 90) and (pos[1] > 180 and pos[1] < 300) and posiciones[6] == 0:
        if turn_circle == True:
          pygame.draw.circle(screen, black, left_down , 45)
          posiciones[6] = 1
          turn_circle = False
        elif turn_circle == False:
          pygame.draw.circle(screen, red, left_down , 45)
          posiciones[6] = 2
          turn_circle = True
        pygame.display.flip()
      # center
      if (pos[0] > 90 and pos[0] < 180) and (pos[1] > 180 and pos[1] < 300) and posiciones[7] == 0:
        if turn_circle == True:
          pygame.draw.circle(screen, black, center_down , 45)
          posiciones[7] = 1
          turn_circle = False
        elif turn_circle == False:
          pygame.draw.circle(screen, red, center_down, 45)
          posiciones[7] = 2
          turn_circle = True
        pygame.display.flip()
      #center right
      if (pos[0] > 180 and pos[0] < 300) and (pos[1] > 180 and pos[1] < 300) and posiciones[8] == 0:
        if turn_circle == True:
          pygame.draw.circle(screen, black, right_down , 45)
          posiciones[8] = 1
          turn_circle = False
        elif turn_circle == False:
          pygame.draw.circle(screen, red, right_down , 45)
          posiciones[8] = 2
          turn_circle = True
        pygame.display.flip()
        

      print(pos)
      print(posiciones)
      CheckWinning(posiciones)
    if event.type == pygame.QUIT:
      running = False