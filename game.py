import pygame
import time

pygame.init()

screen = pygame.display.set_mode((516*2, 389*2))
done = False
x = 500
y = 335
clock = pygame.time.Clock()
walk_anim = 0
f = 0
score_counter = 0
facing_west = False
at_western_edge = False
at_eastern_edge = False
at_northern_edge = False
at_southern_edge = False
bullet_on_screen = False
backround = pygame.image.load('west.jpg')
backround2 = pygame.image.load('west_2.jpg')
backround3 = pygame.image.load('west_3.jpg')
backround4 = pygame.image.load('west_4.jpg')
idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0.png')
r_idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0_reverse.png')
font =  pygame.font.SysFont("comicsansms",20)

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
    shooting = False
    screen.blit(backround,(0,0))
    screen.blit(backround2, (516,0))
    screen.blit(backround3, (0,389))
    screen.blit(backround4, (516,389))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    text = font.render(f"Score: {score_counter}",True,(0,0,0))
    screen.blit(text,(900,0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
        if pressed[pygame.K_LEFT]:
            f += .20
            facing_west = True
            shooting = True
            shoot_anim = int(f) 
            screen.blit(r_shooting_images[shoot_anim%4],(x,y))
            bullet_on_screen = True
            screen.blit(bullet_image,(x+10,y+10))

        else:
            f += .20
            facing_west = False
            shooting = True
            shoot_anim = int(f) 
            screen.blit(shooting_images[shoot_anim%4],(x,y))
            bullet_on_screen = True
            screen.blit(bullet_image,(x+10,y+10))

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
        shooting = False
        if facing_west:
            screen.blit(r_idle_image,(x,y))
        else:
            screen.blit(idle_image,(x,y))
    if pressed[pygame.K_w] and not shooting: 
        if y < 0:
            at_northern_edge = True
        else:
            if not at_northern_edge:
                y -= 3
                at_southern_edge = False
    if pressed[pygame.K_s] and not shooting: 
        if y > 715:
            at_southern_edge = True
        else:
            if not at_southern_edge:
                y += 3 
                at_northern_edge = False
    if pressed[pygame.K_a] and not shooting: 
        if x < 0:
            facing_west = True
            at_western_edge = True
        else:
            if not at_western_edge:
                x -= 3
                at_eastern_edge = False
            facing_west = True
    if pressed[pygame.K_d] and not shooting: 
        if x > 990:
            at_eastern_edge = True
        else:
            if not at_eastern_edge:
                x += 3
                at_western_edge = False
            facing_west = False
    pygame.display.flip()
    clock.tick(60)