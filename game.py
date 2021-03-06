import pygame
import time

pygame.init()


class Player():
    def __init__(self,x,y):
        self.shooting = False
        self.facing_west = False
        self.at_western_edge = False
        self.at_eastern_edge = False
        self.at_northern_edge = False
        self.at_southern_edge = False
        self.x = x
        self.y = y
        self.width = 10
        self.height = 50
        self.health = 3
        self.alive = True

    def check_dead(self):
        if self.health == 0:
            self.alive = False

    def hit(self):
        self.health -= 1

def intro():
    menu_screen = pygame.display.set_mode((900,639))
    menu_background = pygame.image.load('grand_canyon.png')
    done2 = False
    while not done2:
        menu_screen.blit(menu_background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done2 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 324 and x < 561:
                    if y > 206 and y < 288:
                        done2 = False
                        return False
                if x > 329 and x < 563:
                    if y > 421 and y < 492:
                        done2 = False
                        return 'quit'
                if x > 327 and x < 561:
                    if y > 313 and y < 391:
                        done2 = False
                        return 'htp'
        pygame.display.flip()

def how_to_play():
    htp_done = False
    htp_screen = pygame.display.set_mode((978,700))
    htp_background = pygame.image.load('htp_screen.png')
    while not htp_done:
        htp_screen.blit(htp_background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                htp_done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 831 and x < 946:
                    if y > 10 and y < 65:
                        htp_done = True

        pygame.display.flip()


def clear_bullets(bullets):
    bullets2 = []
    for i in range(len(bullets)):
            if bullets[i][1] != 0:
                bullets2.append(bullets[i])
    bullets.clear()
    for i in range(len(bullets2)):
        bullets.append(bullets2[i])
    bullets2.clear()

def check_bullets(bullet_list,hitboxes,p1,p2):
    for i in range(len(bullet_list)):
        for hitbox in hitboxes:
            if bullet_list[i][1] >= hitbox[0] and bullet_list[i][1] <= (hitbox[0] + hitbox[2]):
                if bullet_list[i][2] <= (hitbox[1] + hitbox[3]) and bullet_list[i][2] >= hitbox[1]:
                    if hitbox[4] == 'o':
                        bullet_list[i] = [0,0,0]
                    if 'p' in hitbox[4]:
                        bullet_list[i] = [0,0,0]
                        if hitbox[4] == 'p1':
                            p1.hit()
                            p1.check_dead()
                        if hitbox[4] == 'p2':
                            p2.hit()
                            p2.check_dead()


def main(): 
    p1 = Player(60,400)
    p2 = Player(952,400)
    done = True
    while done:
        if done:
            done = intro()
            if done == False:
                screen = pygame.display.set_mode((1032, 835))        
        if done == 'htp':
            how_to_play()
            done = True
        if done == 'quit':
            return


    screen = pygame.display.set_mode((1032, 835))        
    font =  pygame.font.SysFont("impact",23)
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
    p1_score_counter = 0
    p2_score_counter = 0
    facing_west = False
    at_western_edge = False
    at_eastern_edge = False
    at_northern_edge = False
    at_southern_edge = False
    backround = pygame.image.load('hitbox bg.png')
    idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0.png')
    r_idle_image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0_reverse.png')
    r_bullet_image = pygame.image.load('images/r_bullet_image.png')
    bullet_image = pygame.image.load('images/bullet_image.png')
    hearts = pygame.image.load('hear.png')
    dead_hearts = pygame.image.load('dead.png')
    game_end_time = 10
    is_t1 = False
    is_scored = False
    win = 0
    winner = "No Winner!"
    color = (255,255,255)
    pygame.mixer.music.load('thegbu.ogg')
    pygame.mixer.music.play(-1)
 
    bullets = []
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
        if p1.alive == False:
            win = 2
        if p2.alive == False:
            win = 1
        if win == 1:
            winner = "Player 1 Wins!"
            color = (255,0,0)
        if win == 2:
            winner = "Player 2 Wins!"
            color = (0,0,255)
        hitboxes = [(p1.x,p1.y,p1.width,p1.height,'p1'),(p2.x,p2.y,p2.width,p2.height,'p2'), (168,633,82,75,'o'), (669,170,72,82,'o'), (757,472,66,71,'o'), (500,353,31,103,'o'), (235,170,63,55,'o')]
        c_time = time.time()
        game_end = font.render(f"{game_end_time}",True,(255,255,255))
        winner_text = font.render(f"{winner}",True,color)
        next_round = font.render(f"Next Round Begins in:",True,(255,255,255))

        p1.shooting = False
        p2.shooting = False
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
        timer = font.render(f"Timer: {hour}:{min}:{int(seconds)}",True,(255,255,255))

        p1_score_text = font.render(f"P1 Score: {p1_score_counter}",True,(255,0,0))
        p2_score_text = font.render(f"P2 Score: {p2_score_counter}",True,(0,0,255))
        
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(20, 0, 1000, 30))
        screen.blit(p1_score_text,(40,4))
        screen.blit(p2_score_text,(870,4))
        screen.blit(timer,(475,0))

        for i in range(p1.health):
            screen.blit(hearts,(200-(i*20),0)) #p1

        for i in range(p2.health):
            screen.blit(hearts,(820-(i*20),0)) #p2

        if p1.health != 3:
            for j in range(3-p1.health):
                screen.blit(dead_hearts,(160+(j*20),0))
        if p2.health != 3:
            for j in range(3-p2.health):
                screen.blit(dead_hearts,(780+(j*20),0))
            

        pressed = pygame.key.get_pressed()

        for i in range(len(bullets)):
            if bullets[i][1] > 1032:
                bullets[i] = [0,0,0]
            if bullets[i][1] < 0:
                bullets[i] = [0,0,0]
            if bullets[i][0] == 'w':
                for j in range(20):
                    bullets[i][1] += 1
                    check_bullets(bullets,hitboxes,p1,p2)
                if bullets[i][0] == 'w':
                    screen.blit(bullet_image,(bullets[i][1],bullets[i][2]))
            if bullets[i][0] == 'e':
                for j in range(20):
                    bullets[i][1] -= 1
                    check_bullets(bullets,hitboxes,p1,p2)
                if bullets[i][0] == 'e':
                    screen.blit(r_bullet_image,(bullets[i][1],bullets[i][2]))
        clear_bullets(bullets)
        
        if p1.alive == False or p2.alive == False:
            bullets.clear()
            if p1.alive == False and is_scored == False:
                p2_score_counter += 1
                is_scored = True
            if p2.alive == False and is_scored == False:
                p1_score_counter += 1
                is_scored = True
            if is_t1 == False:
                t1 = time.time()
                is_t1 = True
            t2 = time.time()
            screen.blit(game_end,(590,200))
            screen.blit(winner_text,(450,175))
            screen.blit(next_round,(370,200)) 

            if (t2 - t1) > 1:
                game_end_time -= 1
                is_t1 = False
            if game_end_time == 0:
                p1 = Player(60,400)
                p2 = Player(952,400)
                is_t1 = False
                is_scored = False
                game_end_time = 10
          
        if pressed[pygame.K_q] or pressed[pygame.K_e]:
            f += .20
            p1.shooting = True
            shoot_anim = int(f)
            if pressed[pygame.K_q]:
                screen.blit(r_shooting_images[shoot_anim%4],(p1.x,p1.y))
            else:
                screen.blit(shooting_images[shoot_anim%4],(p1.x,p1.y))
            if sec >= .5:
                if pressed[pygame.K_q]:
                    bullets.append(['e',p1.x,p1.y+35])
                else:
                    bullets.append(['w',p1.x+30,p1.y+35])
                o_time = time.time()
                c_time = time.time()

        elif (pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a] or pressed[pygame.K_d] and p1.alive == True):
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
        if (pressed[pygame.K_w] and not p1.shooting) and p1.alive == True: 
            if p1.y < 0:
                p1.at_northern_edge = True
            else:
                if not p1.at_northern_edge:
                    p1.y -= 3
                    p1.at_southern_edge = False
        elif (pressed[pygame.K_s] and not p1.shooting) and p1.alive == True: 
            if p1.y > 715:
                p1.at_southern_edge = True
            else:
                if not p1.at_southern_edge:
                    p1.y += 3 
                    p1.at_northern_edge = False
        elif (pressed[pygame.K_a] and not p1.shooting) and p1.alive == True: 
            if  p1.x < 0:
                p1.facing_west = True
                p1.at_western_edge = True
            else:
                if not p1.at_western_edge:
                    p1.x -= 3
                    p1.at_eastern_edge = False
                p1.facing_west = True
        elif (pressed[pygame.K_d] and not p1.shooting) and p1.alive == True: 
            if p1.x > 990:
                p1.at_eastern_edge = True
            else:
                if not p1.at_eastern_edge:
                    p1.x += 3
                    p1.at_western_edge = False
                p1.facing_west = False
                
        if (pressed[pygame.K_KP7] or pressed[pygame.K_KP9]) and p2.alive == True:
            f += .20
            p2.shooting = True
            shoot_anim = int(f)
            if pressed[pygame.K_KP7]:
                screen.blit(r_shooting_images[shoot_anim%4],(p2.x,p2.y))
            else:
                screen.blit(shooting_images[shoot_anim%4],(p2.x,p2.y))
            if sec >= .5:
                if pressed[pygame.K_KP7]:
                    bullets.append(['e',p2.x-5,p2.y+35])
                else:
                    bullets.append(['w',p2.x+30,p2.y+35])
                o_time = time.time()
                c_time = time.time()

        elif (pressed[pygame.K_KP4] or pressed[pygame.K_KP5] or pressed[pygame.K_KP6] or pressed[pygame.K_KP8]) and p2.alive == True:
            if pressed[pygame.K_KP4]:
                f += .20
                walk_anim = int(f)
                screen.blit(r_walk_images[walk_anim%4],(p2.x,p2.y))
            else:
                f += .20
                walk_anim = int(f)
                screen.blit(walk_images[walk_anim%4],(p2.x,p2.y))

        else:
            p2.shooting = False
            if p2.facing_west:
                screen.blit(r_idle_image,(p2.x,p2.y))
            else:
                screen.blit(idle_image,(p2.x,p2.y))
        if (pressed[pygame.K_KP8] and not p2.shooting) and p2.alive == True: 
            if p2.y < 0:
                p2.at_northern_edge = True
            else:
                if not p2.at_northern_edge:
                    p2.y -= 3
                    p2.at_southern_edge = False
        elif (pressed[pygame.K_KP5] and not p2.shooting) and p2.alive == True: 
            if p2.y > 715:
                p2.at_southern_edge = True
            else:
                if not p2.at_southern_edge:
                    p2.y += 3 
                    p2.at_northern_edge = False
        elif (pressed[pygame.K_KP4] and not p2.shooting) and p2.alive == True: 
            if  p2.x < 0:
                p2.facing_west = True
                p2.at_western_edge = True
            else:
                if not p2.at_western_edge:
                    p2.x -= 3
                    p2.at_eastern_edge = False
                p2.facing_west = True
        elif (pressed[pygame.K_KP6] and not p2.shooting) and p2.alive == True: 
            if p2.x > 990:
                p2.at_eastern_edge = True
            else:
                if not p2.at_eastern_edge:
                    p2.x += 3
                    p2.at_western_edge = False
                p2.facing_west = False
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
