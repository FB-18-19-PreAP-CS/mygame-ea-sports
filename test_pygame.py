import pygame

#pygame.init()

def part_1():
    screen = pygame.display.set_mode((700, 600))
    done = False
    is_blue = True
    x = 30
    y = 30

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            y -= 3
        if pressed[pygame.K_DOWN]: 
            y += 3
        if pressed[pygame.K_LEFT]: 
            x -= 3
        if pressed[pygame.K_RIGHT]: 
            x += 3
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: 
            color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        clock.tick(60)

def part_2():
    screen = pygame.display.set_mode((700, 600))
    done = False
    x = 30
    y = 30
    clock = pygame.time.Clock()

    while not done:
        screen.fill((255, 255, 255))
        image = pygame.image.load('white_ball.png').convert()
        screen.blit(image,(x,y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
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

part_2()