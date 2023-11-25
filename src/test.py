import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock() 
x, y, width, height, vel = 50, 250,40, 60, 5
 
isJump = False
jumpCountMax = 10
jumpCount = jumpCountMax

run = True 
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not isJump:
                sp_start = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
             if event.key == pygame.K_SPACE and not isJump:
                sp_time = pygame.time.get_ticks() - sp_start
                jumpCountMax = min(12, sp_time // 40) 
                jumpCount = jumpCountMax 
                isJump = True
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
 
    if isJump:
        if jumpCount >= -jumpCountMax:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = jumpCountMax
            isJump = False
 
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
 
pygame.quit()