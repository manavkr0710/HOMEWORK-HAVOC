import pygame

def draw_death_screen(screen, WIDTH, HEIGHT, FONT, elapsed_time):
    screen.fill((0, 0, 0))
    death_text = FONT.render("You Died!", 1, "red")
    time_text = FONT.render(f"Time survived: {round(elapsed_time)}s", 1, "white")
    instruction_text = FONT.render("Press SPACE to restart", 1, "white")

    screen.blit(death_text, (WIDTH/2 - death_text.get_width()/2, HEIGHT/2 - death_text.get_height()))
    screen.blit(time_text, (WIDTH/2 - time_text.get_width()/2, HEIGHT/2 + 20))
    screen.blit(instruction_text, (WIDTH/2 - instruction_text.get_width()/2, HEIGHT/2 + 60))
    pygame.display.update()