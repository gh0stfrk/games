import pygame

pygame.init()

screen_width = 500
screen_height = 500
sensitivity = 20

win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Play Me !")


class Player:
    x = 50
    y = 50
    width = 40
    height = 60

    is_jumping = False
    jump_count = 10


vel = 5

# Game Loop
game = True

while game:

    pygame.time.delay(sensitivity)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and Player.x >= vel:
        Player.x -= vel

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and Player.x < screen_width - Player.width:
        Player.x += vel

    if not Player.is_jumping:
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and Player.y >= vel:
            Player.y -= vel

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and Player.y < screen_height - Player.height:
            Player.y += vel

        if keys[pygame.K_SPACE]:
            Player.is_jumping = True
    else:
        if Player.jump_count >= -10:
            Player.y -= (Player.jump_count * abs(Player.jump_count)) * 0.2
            Player.jump_count -= 1
        else:
            Player.jump_count = 10
            Player.is_jumping = False

    win.fill((0, 0, 0))
    pygame.draw.rect(
        win, (0, 255, 0), (Player.x, Player.y, Player.width, Player.height)
    )
    pygame.display.update()


pygame.quit()
