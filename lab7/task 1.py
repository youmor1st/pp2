import pygame
import time

def new_sizex(x):
    return x.get_width() / 2

def new_sizey(y):
    return y.get_height() / 2

def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

pygame.init()

pygame.display.set_caption("Mickey Clock")

monitor = pygame.display.set_mode((700, 525))
image1 = pygame.image.load("photo\image1.jpeg")
image2 = pygame.image.load("photo\image2.png")
image3 = pygame.image.load("photo\image3.png")

image1 = pygame.transform.scale(image1, (new_sizex(image1), new_sizey(image1)))
image2 = pygame.transform.scale(image2, (new_sizex(image2), new_sizey(image2)))
image3 = pygame.transform.scale(image3, (new_sizex(image3), new_sizey(image3)))

check = True
while check:

    pygame.display.update()
    monitor.blit(image1, (0, 0))

    current_time = time.localtime()
    min_angle = current_time.tm_min * 6 + current_time.tm_sec / 10.0
    sec_angle = current_time.tm_sec * 6

    pos = (350, 262.5)
    blitRotate(monitor, image2, pos, (0, 0), -min_angle - 220)
    blitRotate(monitor, image3, pos, (0, 0), -sec_angle - 220)

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()

    time.sleep(1)