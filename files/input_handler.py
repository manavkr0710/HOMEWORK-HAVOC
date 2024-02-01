import pygame
import time

def handle_input(event, run, show_death_screen, start_time, player, book, book2):
    if event.type == pygame.QUIT:
        pygame.quit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            run = True
            show_death_screen = False
            start_time = time.time()
            player.reset()
            player.alive = True
            book.reset()
            book2 = None
            pygame.time.delay(200)
    
    return run, show_death_screen, start_time, book2
