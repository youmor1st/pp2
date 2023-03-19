import pygame

pygame.init()

monitor = pygame.display.set_mode((600, 400))
pos_x = 25
pos_y = 25

def to_right():
    global pos_x
    if pos_x + 25 + 20 < 600:
        pos_x += 20

def to_left():
    global pos_x
    if pos_x - 25 - 20 > 0:
        pos_x -= 20

def down():
    global pos_y
    if pos_y + 25 + 20 < 400:
        pos_y += 20

def up():
    global pos_y
    if pos_y - 25 - 20 > 0:
        pos_y -= 25

check = True
while check:
    pygame.display.update()
    monitor.fill((255, 255, 255))
    pygame.draw.circle(monitor, (255, 0, 0), (pos_x, pos_y), 25)

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()

        elif action.type == pygame.KEYDOWN:
            if action.key == pygame.K_LEFT:
                to_left()
            elif action.key == pygame.K_RIGHT:
                to_right()
            elif action.key == pygame.K_DOWN:
                down()
            elif action.key == pygame.K_UP:
                up()