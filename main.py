import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Prosta gra w Pygame")

# Kolory
white = (255, 255, 255)
blue = (0, 0, 255)

# Pozycja gracza
player_pos = [screen_width // 2, screen_height // 2]
player_size = 50
player_speed = 5

# Główna pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ruch gracza
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Ograniczenia ekranu
    if player_pos[0] < 0:
        player_pos[0] = 0
    if player_pos[0] > screen_width - player_size:
        player_pos[0] = screen_width - player_size
    if player_pos[1] < 0:
        player_pos[1] = 0
    if player_pos[1] > screen_height - player_size:
        player_pos[1] = screen_height - player_size

    # Rysowanie na ekranie
    screen.fill(white)  # Tło
    pygame.draw.rect(screen, blue, (player_pos[0], player_pos[1], player_size, player_size))  # Gracz
    pygame.display.flip()  # Aktualizacja ekranu

    # Ustawienie prędkości klatek na 30 FPS
    pygame.time.Clock().tick(30)
