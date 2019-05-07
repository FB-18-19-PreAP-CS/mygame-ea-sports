import pygame
import time

pygame.init()

class Player():
    def __init__(self):
        self.shooting = False
        self.facing_west = False
        self.at_western_edge = False
        self.at_eastern_edge = False
        self.at_northern_edge = False
        self.at_southern_edge = False
        self.x = 500
        self.y = 335

def main(): 
    screen = pygame.display.set_mode((516*2, 418*2))
    font =  pygame.font.SysFont("Sans-Serif",30)
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
    o_time = time.time()
    c_time = time.time()
    score_counter = 0
    facing_west = False
    at_western_edge = False
    at_eastern_edge = False
    at_northern_edge = False
    at_southern_edge = False
    backround = pygame.image.load('smoothbg.png')
    idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0.png')
    r_idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0_reverse.png')
    r_bullet_image = pygame.image.load('images/r_bullet_image.png')
    bullet_image = pygame.image.load('images/bullet_image.png')

    bullets = []
    bullets2 = []



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
        c_time = time.time()

        p1.shooting = False
        screen.blit(backround,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        seconds = (curr_time - orig_time) // 1
        sec = (c_time - o_time)
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
        timer = font.render(f"Timer: {hour}:{min}:{int(seconds)}",True,(0,0,0))
        text = font.render(f"Score: {score_counter}",True,(0,0,0))
        screen.blit(timer,(475,0))
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
            f += .20
            shooting = True
            shoot_anim = int(f)
            if pressed[pygame.K_q]:
                screen.blit(r_shooting_images[shoot_anim%4],(p1.x,p1.y))
            else:
                screen.blit(shooting_images[shoot_anim%4],(p1.x,p1.y))
            if sec >= .5:
                if pressed[pygame.K_q]:
                    bullets.append(['e',p1.x+10,p1.y+35])
                else:
                    bullets.append(['w',p1.x+30,p1.y+35])
                o_time = time.time()
                c_time = time.time()

        elif pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a] or pressed[pygame.K_d]:
            if pressed[pygame.K_a]:
                f += .20
                walk_anim = int(f)
                screen.blit(r_walk_images[walk_anim%4],(p1.x,p1.y))
            else:
                f += .20
                walk_anim = int(f)
                screen.blit(walk_images[walk_anim%4],(p1.x,p1.y))

        else:
            p1.shooting = False
            if p1.facing_west:
                screen.blit(r_idle_image,(p1.x,p1.y))
            else:
                screen.blit(idle_image,(p1.x,p1.y))
        if pressed[pygame.K_w] and not p1.shooting: 
            if p1.y < 0:
                p1.at_northern_edge = True
            else:
                if not p1.at_northern_edge:
                    p1.y -= 3
                    p1.at_southern_edge = False
        if pressed[pygame.K_s] and not p1.shooting: 
            if p1.y > 715:
                p1.at_southern_edge = True
            else:
                if not p1.at_southern_edge:
                    p1.y += 3 
                    p1.at_northern_edge = False
        if pressed[pygame.K_a] and not p1.shooting: 
            if  p1.x < 0:
                p1.facing_west = True
                p1.at_western_edge = True
            else:
                if not p1.at_western_edge:
                    p1.x -= 3
                    p1.at_eastern_edge = False
                p1.facing_west = True
        if pressed[pygame.K_d] and not p1.shooting: 
            if p1.x > 990:
                p1.at_eastern_edge = True
            else:
                if not p1.at_eastern_edge:
                    p1.x += 3
                    p1.at_western_edge = False
                p1.facing_west = False
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    p1 = Player()
    main()