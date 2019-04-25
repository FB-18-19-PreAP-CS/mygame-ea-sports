import pygame

pygame.init()

screen = pygame.display.set_mode((700, 600))
done = False
x = 30
y = 30
clock = pygame.time.Clock()

while not done:
    screen.fill((255, 255, 255))
    image = pygame.image.load('images/Cowboy 4 HiRes/Cowboy4_idle with gun_0.png')
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