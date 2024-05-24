import pygame

pygame.init()

screen_width = 500
screen_height = 480
sensitivity = 20

win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Keep Walkin")

bullet_sound = pygame.mixer.Sound("assets/audio/bullet.mp3")
hit_sound = pygame.mixer.Sound("assets/audio/hit.mp3")

music = pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.play(-1)

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


class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 5 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Enemy:
    walk_right = [
        pygame.image.load("assets/R1E.png"),
        pygame.image.load("assets/R2E.png"),
        pygame.image.load("assets/R3E.png"),
        pygame.image.load("assets/R4E.png"),
        pygame.image.load("assets/R5E.png"),
        pygame.image.load("assets/R6E.png"),
        pygame.image.load("assets/R7E.png"),
        pygame.image.load("assets/R8E.png"),
        pygame.image.load("assets/R9E.png"),
        pygame.image.load("assets/R10E.png"),
        pygame.image.load("assets/R11E.png"),
    ]

    walk_left = [
        pygame.image.load("assets/L1E.png"),
        pygame.image.load("assets/L2E.png"),
        pygame.image.load("assets/L3E.png"),
        pygame.image.load("assets/L4E.png"),
        pygame.image.load("assets/L5E.png"),
        pygame.image.load("assets/L6E.png"),
        pygame.image.load("assets/L7E.png"),
        pygame.image.load("assets/L8E.png"),
        pygame.image.load("assets/L9E.png"),
        pygame.image.load("assets/L10E.png"),
        pygame.image.load("assets/L11E.png"),
    ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walk_count = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0
            if self.vel > 0:
                win.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            else:
                win.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1

            pygame.draw.rect(
                win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)
            )
            pygame.draw.rect(
                win,
                (0, 128, 0),
                (
                    self.hitbox[0],
                    self.hitbox[1] - 20,
                    50 - (5 * (10 - self.health)),
                    10,
                ),
            )
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walk_count = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walk_count = 0

    def hit(self):
        hit_sound.play()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


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
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if not self.standing:
            if self.left:
                win.blit(walk_left[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(walk_right[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.right:
                win.blit(walk_right[0], (self.x, self.y))
            else:
                win.blit(walk_left[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def hit(self):
        self.x = 60
        self.y = 410
        self.walk_count = 0
        self.is_jumping = False
        self.jump_count = 10
        score_deduction = pygame.font.SysFont("comicsans", 80)
        message = pygame.font.SysFont("comicsans", 100)
        msg_text = message.render("Wasted", 1, (180, 0, 0))
        text = score_deduction.render("-5", 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
        win.blit(msg_text,(250 - (msg_text.get_width() / 2), 120))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


def redraw_game_window():
    win.blit(bg, (0, 0))
    text = display_score.render("Score " + str(score), 1, (0, 0, 0))
    win.blit(text, (200, 10))
    player.draw()
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


player = Player(200, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)


score = 0
display_score = pygame.font.SysFont("comicsans", 30, True)

game = True
bullets = []
shotloop = 0

while game:

    if goblin.visible:
        if (
            player.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3]
            and player.hitbox[1] + player.hitbox[3] > goblin.hitbox[1]
        ):
            if (
                player.hitbox[0] + player.hitbox[2] > goblin.hitbox[0]
                and player.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]
            ):
                player.hit()
                score -= 5

    if shotloop > 0:
        shotloop += 1
    if shotloop > 3:
        shotloop = 0

    for bullet in bullets:
        if (
            bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3]
            and bullet.y + bullet.radius > goblin.hitbox[1]
        ):
            if (
                bullet.x + bullet.radius > goblin.hitbox[0]
                and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]
                and goblin.visible
            ):
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    pygame.time.delay(sensitivity)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shotloop == 0:
        bullet_sound.play()
        if player.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                Projectile(
                    round(player.x + player.width // 2),
                    round(player.y + player.height // 2),
                    5,
                    (0, 0, 0),
                    facing,
                )
            )
        shotloop = 1

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x >= player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False

    elif (
        keys[pygame.K_RIGHT] or keys[pygame.K_d]
    ) and player.x < screen_width - player.width:
        player.x += player.vel
        player.right = True
        player.left = False
        player.standing = False
    else:
        player.standing = True
        player.walk_count = 0

    if not player.is_jumping:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
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
