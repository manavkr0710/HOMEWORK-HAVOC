import pygame

def start_screen(screen, bg, WIDTH, HEIGHT, FONT):
    start_screen = True

    homework_havoc_img = pygame.image.load("C:/Users/manav/PycharmProjects/PythonProjectsManav/Homework Havoc/images/Homework_Havoc_bg.png")
    keys_img = pygame.image.load("C:/Users/manav/PycharmProjects/PythonProjectsManav/Homework Havocgit/images/Keys_image.png")

    while start_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                start_screen = False

            if event.type == pygame.KEYDOWN:
                start_screen = False

        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        screen.blit(keys_img, (900, 400))
        keys_text = FONT.render("Controls: ", 1, "white")
        screen.blit(keys_text, (750,550))

        screen.blit(homework_havoc_img, (400,0))
        start_text = FONT.render("Press any key to start", 1, "white")
        screen.blit(start_text, (WIDTH/2 - start_text.get_width()/2, HEIGHT/2))
        pygame.display.update()