import pygame
import random
import math
import sys


"""Simple Space Shooter

Features in this version:
- Single enemy that falls from top to bottom when active
- Enemy spawns when player score reaches a threshold (configurable)
- Shooting the enemy increments score and schedules the next spawn
"""

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter 🚀")
clock = pygame.time.Clock()

# Player
PLAYER_W, PLAYER_H = 50, 50
player_img = pygame.Surface((PLAYER_W, PLAYER_H), pygame.SRCALPHA)
player_img.fill((0, 255, 0))
player_x = WIDTH // 2 - PLAYER_W // 2
player_y = HEIGHT - 80
player_speed = 5

# Bullet
BULLET_W, BULLET_H = 6, 12
bullet_img = pygame.Surface((BULLET_W, BULLET_H), pygame.SRCALPHA)
bullet_img.fill((255, 0, 0))
bullet_x = 0
bullet_y = player_y
bullet_speed = 8
bullet_state = "ready"  # 'ready' or 'fire'

# Enemy (single)
ENEMY_W, ENEMY_H = 50, 50
enemy_img = pygame.Surface((ENEMY_W, ENEMY_H), pygame.SRCALPHA)
enemy_img.fill((0, 0, 255))
enemy_x = 0
enemy_y = -ENEMY_H
enemy_speed = 2
enemy_active = False

# Spawn config: adjust these to control when and how often the enemy appears
ENEMY_INITIAL_SPAWN_SCORE = 0  # spawn immediately when score >= this (0 => immediate)
ENEMY_SPAWN_INTERVAL = 5  # after kill, spawn again when score >= current + interval
next_spawn_score = ENEMY_INITIAL_SPAWN_SCORE

# Score
score_value = 0
font = pygame.font.Font(None, 36)


def show_score(surface, x=10, y=10):
    txt = font.render(f"Score: {score_value}", True, (255, 255, 255))
    surface.blit(txt, (x, y))


def draw_player(surface, x, y):
    surface.blit(player_img, (x, y))


def draw_enemy(surface, x, y):
    surface.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"


def is_collision(ex, ey, bx, by):
    # center distance
    ex_c = ex + ENEMY_W / 2
    ey_c = ey + ENEMY_H / 2
    bx_c = bx + BULLET_W / 2
    by_c = by + BULLET_H / 2
    return math.hypot(ex_c - bx_c, ey_c - by_c) < 30


def spawn_enemy():
    global enemy_x, enemy_y, enemy_active
    enemy_x = random.randint(0, WIDTH - ENEMY_W)
    enemy_y = -ENEMY_H
    enemy_active = True


def main():
    global player_x, player_y, enemy_x, enemy_y, enemy_active, next_spawn_score
    global bullet_x, bullet_y, bullet_state, score_value

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    # align bullet with player's visual center
                    bullet_x = player_x + (PLAYER_W - BULLET_W) // 2
                    bullet_y = player_y
                    fire_bullet(bullet_x, bullet_y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        player_x = max(0, min(player_x, WIDTH - PLAYER_W))

        # spawn enemy when score threshold reached
        if not enemy_active and score_value >= next_spawn_score:
            spawn_enemy()

        # enemy falls top -> bottom when active
        if enemy_active:
            enemy_y += enemy_speed
            # if it goes off screen, deactivate and schedule next spawn
            if enemy_y > HEIGHT:
                enemy_active = False
                next_spawn_score = score_value + ENEMY_SPAWN_INTERVAL

        # bullet movement
        if bullet_state == "fire":
            bullet_y -= bullet_speed
            # if bullet leaves screen reset
            if bullet_y < -BULLET_H:
                bullet_y = player_y
                bullet_state = "ready"

        # collision: only when enemy is active
        if bullet_state == "fire" and enemy_active and is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
            bullet_y = player_y
            bullet_state = "ready"
            score_value += 1
            enemy_active = False
            next_spawn_score = score_value + ENEMY_SPAWN_INTERVAL

        # draw
        screen.fill((0, 0, 30))
        draw_player(screen, player_x, player_y)
        if enemy_active:
            draw_enemy(screen, enemy_x, enemy_y)

        if bullet_state == "fire":
            screen.blit(bullet_img, (bullet_x, bullet_y))

        show_score(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
import pygame
import random
import math
import sys


"""Simple Space Shooter

Features in this version:
- Single enemy that falls from top to bottom when active
- Enemy spawns when player score reaches a threshold (configurable)
- Shooting the enemy increments score and schedules the next spawn
"""

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter 🚀")
clock = pygame.time.Clock()

# Player
PLAYER_W, PLAYER_H = 50, 50
player_img = pygame.Surface((PLAYER_W, PLAYER_H), pygame.SRCALPHA)
player_img.fill((0, 255, 0))
player_x = WIDTH // 2 - PLAYER_W // 2
player_y = HEIGHT - 80
player_speed = 5

# Bullet
BULLET_W, BULLET_H = 6, 12
bullet_img = pygame.Surface((BULLET_W, BULLET_H), pygame.SRCALPHA)
bullet_img.fill((255, 0, 0))
bullet_x = 0
bullet_y = player_y
bullet_speed = 8
bullet_state = "ready"  # 'ready' or 'fire'

# Enemy (single)
ENEMY_W, ENEMY_H = 50, 50
enemy_img = pygame.Surface((ENEMY_W, ENEMY_H), pygame.SRCALPHA)
enemy_img.fill((0, 0, 255))
enemy_x = 0
enemy_y = -ENEMY_H
enemy_speed = 2
enemy_active = False

# Spawn config: adjust these to control when and how often the enemy appears
ENEMY_INITIAL_SPAWN_SCORE = 0  # spawn immediately when score >= this (0 => immediate)
ENEMY_SPAWN_INTERVAL = 5  # after kill, spawn again when score >= current + interval
next_spawn_score = ENEMY_INITIAL_SPAWN_SCORE

# Score
score_value = 0
font = pygame.font.Font(None, 36)


def show_score(surface, x=10, y=10):
    txt = font.render(f"Score: {score_value}", True, (255, 255, 255))
    surface.blit(txt, (x, y))


def draw_player(surface, x, y):
    surface.blit(player_img, (x, y))


def draw_enemy(surface, x, y):
    surface.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"


def is_collision(ex, ey, bx, by):
    # center distance
    ex_c = ex + ENEMY_W / 2
    ey_c = ey + ENEMY_H / 2
    bx_c = bx + BULLET_W / 2
    by_c = by + BULLET_H / 2
    return math.hypot(ex_c - bx_c, ey_c - by_c) < 30


def spawn_enemy():
    global enemy_x, enemy_y, enemy_active
    enemy_x = random.randint(0, WIDTH - ENEMY_W)
    enemy_y = -ENEMY_H
    enemy_active = True


def main():
    global player_x, player_y, enemy_x, enemy_y, enemy_active, next_spawn_score
    global bullet_x, bullet_y, bullet_state, score_value

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    # align bullet with player's visual center
                    bullet_x = player_x + (PLAYER_W - BULLET_W) // 2
                    bullet_y = player_y
                    fire_bullet(bullet_x, bullet_y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        player_x = max(0, min(player_x, WIDTH - PLAYER_W))

        # spawn enemy when score threshold reached
        if not enemy_active and score_value >= next_spawn_score:
            spawn_enemy()

        # enemy falls top -> bottom when active
        if enemy_active:
            enemy_y += enemy_speed
            # if it goes off screen, deactivate and schedule next spawn
            if enemy_y > HEIGHT:
                enemy_active = False
                next_spawn_score = score_value + ENEMY_SPAWN_INTERVAL

        # bullet movement
        if bullet_state == "fire":
            bullet_y -= bullet_speed
            # if bullet leaves screen reset
            if bullet_y < -BULLET_H:
                bullet_y = player_y
                bullet_state = "ready"

        # collision: only when enemy is active
        if bullet_state == "fire" and enemy_active and is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
            bullet_y = player_y
            bullet_state = "ready"
            score_value += 1
            enemy_active = False
            next_spawn_score = score_value + ENEMY_SPAWN_INTERVAL

        # draw
        screen.fill((0, 0, 30))
        draw_player(screen, player_x, player_y)
        if enemy_active:
            draw_enemy(screen, enemy_x, enemy_y)

        if bullet_state == "fire":
            screen.blit(bullet_img, (bullet_x, bullet_y))

        show_score(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
import pygame
import random
import math
import sys


# ---------------------------
# Space Shooter - working
# ---------------------------

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter 🚀🌠")
clock = pygame.time.Clock()

# Player
player_img = pygame.Surface((50, 50), pygame.SRCALPHA)
player_img.fill((0, 255, 0))  # green square for the player
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 80
player_speed = 5

# Enemy
enemy_img = pygame.Surface((50, 50), pygame.SRCALPHA)
enemy_img.fill((0, 0, 255))  # blue square for the enemy
enemy_x = random.randint(0, WIDTH - 50)
enemy_y = random.randint(50, 150)
enemy_speed_x = 2
enemy_speed_y = 40

# Bullet
bullet_img = pygame.Surface((6, 12), pygame.SRCALPHA)
bullet_img.fill((255, 0, 0))  # red bullets
bullet_x = 0
bullet_y = player_y
bullet_speed = 8
bullet_state = "ready"  # 'ready' or 'fire'
 
# Score
score_value = 0
font = pygame.font.Font(None, 36)


def show_score(surface, x=10, y=10):
    txt = font.render(f"Score: {score_value}", True, (255, 255, 255))
    surface.blit(txt, (x, y))


def draw_player(surface, x, y):
    surface.blit(player_img, (x, y))


def draw_enemy(surface, x, y):
    surface.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    # only set state and initial position here; drawing happens in the draw phase
    bullet_state = "fire"


def is_collision(ex, ey, bx, by):
    # simple distance check between centers
    ex_center = ex + 25
    ey_center = ey + 25
    bx_center = bx + 3
    by_center = by + 6
    distance = math.hypot(ex_center - bx_center, ey_center - by_center)
    return distance < 27


def reset_enemy():
    return random.randint(0, WIDTH - 50), random.randint(50, 150)


def main():
    global player_x, player_y, enemy_x, enemy_y, enemy_speed_x
    global bullet_x, bullet_y, bullet_state, score_value

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bullet_x = player_x
                    bullet_y = player_y
                    fire_bullet(bullet_x, bullet_y)

        # key state for smooth movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # clamp player
        player_x = max(0, min(player_x, WIDTH - 50))

        # enemy movement
        enemy_x += enemy_speed_x
        if enemy_x <= 0:
            enemy_speed_x = abs(enemy_speed_x)
            enemy_y += enemy_speed_y
        elif enemy_x >= WIDTH - 50:
            enemy_speed_x = -abs(enemy_speed_x)
            enemy_y += enemy_speed_y

        # bullet movement
        if bullet_state == "fire":
            bullet_y -= bullet_speed

        # reset bullet if it goes off screen
        if bullet_y <= -20:
            bullet_y = player_y
            bullet_state = "ready"

        # collision
        if bullet_state == "fire" and is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
            bullet_y = player_y
            bullet_state = "ready"
            score_value += 1
            enemy_x, enemy_y = reset_enemy()

        # draw
        screen.fill((0, 0, 30))
        draw_player(screen, player_x, player_y)
        draw_enemy(screen, enemy_x, enemy_y)

        # draw bullet in the draw phase so it remains visible after clearing
        if bullet_state == "fire":
            screen.blit(bullet_img, (bullet_x + 22, bullet_y))

        show_score(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

