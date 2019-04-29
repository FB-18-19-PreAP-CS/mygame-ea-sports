import pygame
import time

pygame.init()

screen = pygame.display.set_mode((516, 389))
done = False
x = 30
y = 30
clock = pygame.time.Clock()
walk_anim = 0
f = 0
facing_west = False
backround = pygame.image.load('west.jpg')
idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0.png')
r_idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0_reverse.png')

walk_images = []
r_walk_images = []
r_shooting_images = []
shooting_images = []
for i in range(4):
    r_walk_images.append(pygame.image.load(f'images/Cowboy 4 HiRes/Cowboy4_walk with gun_{i}_reverse.png'))
for i in range(4):
     r_shooting_images.append(pygame.image.load(f'images/Cowboy 4 HiRes/Cowboy4_shoot_{i}_reverse.png'))
for i in range(4):
    walk_images.append(pygame.image.load(f'images/Cowboy 4 HiRes/Cowboy4_walk with gun_{i}.png'))
for i in range(4):
    shooting_images.append(pygame.image.load(f'images/Cowboy 4 HiRes/Cowboy4_shoot_{i}.png'))
    

while not done:
    screen.blit(backround,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] or pressed[pygame.K_DOWN] or pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
        if pressed[pygame.K_LEFT]:
            f += .20
            facing_west = True
            shoot_anim = int(f) 
            screen.blit(r_shooting_images[shoot_anim%4],(x,y))
        else:
            f += .20
            facing_west = False
            shoot_anim = int(f) 
            screen.blit(shooting_images[shoot_anim%4],(x,y))

    elif pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a] or pressed[pygame.K_d]:
        if pressed[pygame.K_a]:
            f += .20
            walk_anim = int(f)
            screen.blit(r_walk_images[walk_anim%4],(x,y))
        else:
            if facing_west:
                f += .20
                walk_anim = int(f)
                screen.blit(r_walk_images[walk_anim%4],(x,y))
            else:
                f += .20
                walk_anim = int(f)
                screen.blit(walk_images[walk_anim%4],(x,y))
        
    else:
        if facing_west:
            screen.blit(r_idle_image,(x,y))
        else:
            screen.blit(idle_image,(x,y))
    if pressed[pygame.K_w]: 
        if y == 300:
            continue
        else:
            y -= 3
    if pressed[pygame.K_s]: 
        if y == 0:
            continue
        else:
            y += 3
    if pressed[pygame.K_a]: 
        if x == 0:
            facing_west = True
        else:
            x -= 3
            facing_west = True
    if pressed[pygame.K_d]: 
        x += 3
        facing_west = False
    pygame.display.flip()
    clock.tick(60)
