import pygame
import time

pygame.init()

screen = pygame.display.set_mode((700, 600))
done = False
x = 30
y = 30
clock = pygame.time.Clock()
walk_anim = 0

while not done:
    screen.fill((255, 255, 255))
    idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0.png')
    walk_image1 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_0.png')
    walk_image2 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_1.png')
    walk_image3 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_2.png')
    walk_image4 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_3.png')
    walk_images = [walk_image1, walk_image1, walk_image1, walk_image1, walk_image2, walk_image2, walk_image2, walk_image2, walk_image3, walk_image3, walk_image3, walk_image3, walk_image4, walk_image4, walk_image4, walk_image4]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] or pressed[pygame.K_DOWN] or pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
        screen.blit(walk_images[walk_anim%16],(x,y))
        walk_anim += 1
    else:
        screen.blit(idle_image,(x,y))
    if pressed[pygame.K_UP]: 
        y -= 3
    if pressed[pygame.K_DOWN]: 
        y += 3
    if pressed[pygame.K_LEFT]: 
        x -= 3
    if pressed[pygame.K_RIGHT]: 
        x += 3
    pygame.display.flip()
    clock.tick(60)