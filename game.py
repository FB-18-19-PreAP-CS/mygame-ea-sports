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
walk_image1 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_0.png')
walk_image2 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_1.png')
walk_image3 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_2.png')
walk_image4 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_3.png')
r_walk_image1 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_0_reverse.png')
r_walk_image2 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_1_reverse.png')
r_walk_image3 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_2_reverse.png')
r_walk_image4 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_walk with gun_3_reverse.png')
shooting_image1 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_shoot_0.png')
shooting_image2 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_shoot_1.png')
shooting_image3 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_shoot_2.png')
shooting_image4 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_shoot_3.png')
r_shooting_image1 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_shoot_0_reverse.png')
r_shooting_image2 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_shoot_1_reverse.png')
r_shooting_image3 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_shoot_2_reverse.png')
r_shooting_image4 = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_shoot_3_reverse.png')

r_walk_images = [r_walk_image1, r_walk_image2, r_walk_image3, r_walk_image4]
walk_images = [walk_image1, walk_image2, walk_image3, walk_image4]
shooting_images = [shooting_image1, shooting_image2, shooting_image3, shooting_image4]
r_shooting_images = [r_shooting_image1, r_shooting_image2, r_shooting_image3, r_shooting_image4]
    

while not done:
    screen.blit(backround,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        if facing_west:
            f += .20
            shoot_anim = int(f) 
            screen.blit(r_shooting_images[shoot_anim%4],(x,y))
        else:
            f += .20
            shoot_anim = int(f) 
            screen.blit(shooting_images[shoot_anim%4],(x,y))

    elif pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a] or pressed[pygame.K_d]:
        if pressed[pygame.K_a]:
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
        y -= 3
    if pressed[pygame.K_s]: 
        y += 3
    if pressed[pygame.K_a]: 
        x -= 3
        facing_west = True
    if pressed[pygame.K_d]: 
        x += 3
        facing_west = False
    pygame.display.flip()
    clock.tick(60)