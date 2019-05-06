import pygame
import time

pygame.init()

screen = pygame.display.set_mode((516*2, 418*2))
done = False
x = 500
y = 335
clock = pygame.time.Clock()
walk_anim = 0
f = 0
seconds = 0
min = 0
hour = 0
curr_time = 0
orig_time = time.time()
score_counter = 0
facing_west = False
at_western_edge = False
at_eastern_edge = False
at_northern_edge = False
at_southern_edge = False
bullet_on_screen = False
backround = pygame.image.load('smoothbg.png')
idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0.png')
r_idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0_reverse.png')
r_bullet_image = pygame.image.load('images/r_bullet_image.png')
bullet_image = pygame.image.load('images/bullet_image.png')

bullets = []
bullets2 = []

font =  pygame.font.SysFont("Sans-Serif",30)


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
    # screen.blit(backround2, (516,0))
    # screen.blit(backround3, (0,389))
    # screen.blit(backround4, (516,389))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    seconds = (curr_time - orig_time) // 1

    if min == 60:
        hour += 1
        min = 0
        curr_time = 0
    if seconds == 60:
        min += 1
        seconds = 0
        cur_time = 0
        orig_time = time.time()

    curr_time = time.time()
    timer = font.render(f"{hour}:{min}:{int(seconds)}",True,(0,0,0))
    text = font.render(f"Score: {score_counter}",True,(0,0,0))
    screen.blit(timer,(490,0))
    screen.blit(text,(900,0))

    pressed = pygame.key.get_pressed()

    for i in range(len(bullets)):
        if bullets[i][1] > 1032:
            bullets[i] = [0,0,0]
        if bullets[i][1] < 0:
            bullets[i] = [0,0,0]
        if bullets[i][0] == 'w':
            bullets[i][1] += 20
            screen.blit(bullet_image,(bullets[i][1],bullets[i][2]))
        if bullets[i][0] == 'e':
            bullets[i][1] -= 20
            screen.blit(r_bullet_image,(bullets[i][1],bullets[i][2]))
    for i in range(len(bullets)):
        if bullets[i][1] != 0:
            bullets2.append(bullets[i])
    bullets.clear()
    for i in range(len(bullets2)):
        bullets.append(bullets2[i])
    bullets2.clear()

    if pressed[pygame.K_q] or pressed[pygame.K_e]:
        if pressed[pygame.K_q]:
            f += .20
            facing_west = True
            shooting = True
            shoot_anim = int(f) 
            screen.blit(r_shooting_images[shoot_anim%4],(x,y))
            bullet_on_screen = True
            bullets.append(['e',x+10,y+35])

        else:
            f += .20
            facing_west = False
            shooting = True
            shoot_anim = int(f) 
            screen.blit(shooting_images[shoot_anim%4],(x,y))
            bullet_on_screen = True
            bullets.append(['w',x+30,y+35])

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