import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('assets/launch.png')
player_icon = pygame.image.load('assets/player.png')
pygame.display.set_caption("Space invaders.")
pygame.display.set_icon(icon)
player_x = 370
player_y = 536
player_x_change = 0
movement_speed = 15


def player(x, y):
    screen.blit(player_icon, (x, y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -movement_speed
            if event.key == pygame.K_RIGHT:
                player_x_change = movement_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_x_change = 0

    screen.fill((0, 100, 100))
    player_x += player_x_change
    player(player_x, player_y)
    pygame.display.update()
