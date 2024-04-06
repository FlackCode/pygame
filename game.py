import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Flack")

x = 50
y = 50
width = 50
height = 70
vel = 10
playerColor = (255, 0, 0)

isJump = False
jumpCount = 10

while running:
    pygame.time.delay(100)
    clock.tick(75)
    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > vel:
        x -= vel

    if keys[pygame.K_d] and x < 800 - vel - width:
        x += vel

    if not(isJump):
        if keys[pygame.K_s] and y < 600 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    screen.fill((255, 255, 255))
    player = pygame.draw.rect(screen, playerColor, pygame.Rect(x, y, width, height))
    pygame.display.update()
    
pygame.quit()
