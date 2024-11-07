import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Prosta gra z obsługą dotyku")

# Kolory
white = (255, 255, 255)
blue = (0, 0, 255)

# Pozycja gracza
player_pos = [screen_width // 2, screen_height // 2]
player_size = 50
dragging = False  # Zmienna, która sprawdza, czy kwadrat jest przeciągany

# Główna pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Obsługa dotyku
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Sprawdza, czy dotknięcie jest w obrębie kwadratu
            mouse_x, mouse_y = event.pos
            if (player_pos[0] <= mouse_x <= player_pos[0] + player_size and
                player_pos[1] <= mouse_y <= player_pos[1] + player_size):
                dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                # Aktualizacja pozycji gracza zgodnie z ruchem dotyku
                player_pos[0], player_pos[1] = event.pos

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
