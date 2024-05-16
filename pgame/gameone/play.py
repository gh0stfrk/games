import pygame

pygame.init()

screen_width = 500
screen_height = 480
sensitivity = 20

win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First Game")

walk_right = [
    pygame.image.load("assets/R1.png"),
    pygame.image.load("assets/R2.png"),
    pygame.image.load("assets/R3.png"),
    pygame.image.load("assets/R4.png"),
    pygame.image.load("assets/R5.png"),
    pygame.image.load("assets/R6.png"),
    pygame.image.load("assets/R7.png"),
    pygame.image.load("assets/R8.png"),
    pygame.image.load("assets/R9.png"),
]

walk_left = [
    pygame.image.load("assets/L1.png"),
    pygame.image.load("assets/L2.png"),
    pygame.image.load("assets/L3.png"),
    pygame.image.load("assets/L4.png"),
    pygame.image.load("assets/L5.png"),
    pygame.image.load("assets/L6.png"),
    pygame.image.load("assets/L7.png"),
    pygame.image.load("assets/L8.png"),
    pygame.image.load("assets/L9.png"),
]

bg = pygame.image.load("assets/bg.jpg")
char = pygame.image.load("assets/standing.png")


class Player:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_jumping = False
        self.jump_count = 10
        self.walk_count = 0
        self.left = False
        self.right = False
        self.vel = 5

    def draw(self):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if left:
            win.blit(walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif right:
            win.blit(walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(char, (self.x, self.y))
            self.walk_count = 0


def redraw_game_window():
    win.blit(bg, (0, 0))
    player.draw()
    pygame.display.update()


player = Player(200, 410, 64, 64)

game = True
while game:

    pygame.time.delay(sensitivity)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x >= player.vel:
        player.x -= player.vel
        left = True
        right = False

    elif (
        keys[pygame.K_RIGHT] or keys[pygame.K_d]
    ) and player.x < screen_width - player.width:
        player.x += player.vel
        right = True
        left = False
    else:
        left = False
        right = False

    if not player.is_jumping:
        if keys[pygame.K_SPACE]:
            player.is_jumping = True
    else:
        if player.jump_count >= -10:
            player.y -= (player.jump_count * abs(player.jump_count)) * 0.2
            player.jump_count -= 1
        else:
            player.jump_count = 10
            player.is_jumping = False

    redraw_game_window()


pygame.quit()
