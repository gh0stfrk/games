import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Play Me !")


class Player:
    x = 50
    y = 50
    width = 40
    height = 60


vel = 5

# Game Loop
game = True

while game:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        Player.x -= vel
    
    if keys[pygame.K_RIGHT]:
        Player.x += vel
        
    if keys[pygame.K_UP]:
        Player.y -= vel
        
    if keys[pygame.K_DOWN]:
        Player.y += vel
        
    win.fill((0, 0, 0))
    pygame.draw.rect(
        win, (0, 255, 0), (Player.x, Player.y, Player.width, Player.height)
    )
    pygame.display.update()


pygame.quit()
