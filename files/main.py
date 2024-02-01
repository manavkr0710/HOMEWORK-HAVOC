from playerFile import Player
from bookFile import Book
import pygame, random, time 
from start_screen import start_screen
from death_screen import draw_death_screen
from input_handler import handle_input
from rendering import render_background, render_player, render_book

pygame.font.init() ##change
pygame.init()

WIDTH, HEIGHT = 1234, 693
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
FONT = pygame.font.SysFont("Times New Roman", 50)

# IMAGES
base_path = "C:/Users/manav/PycharmProjects/PythonProjectsManav/Homework Havoc/images/"
bg = pygame.image.load(base_path + "school_background.png")
book_imgs = [pygame.image.load(base_path + "book_1.png"), pygame.image.load(base_path + "book_2.png")]
walk_left_imgs = [pygame.image.load(base_path + "Run_backwards_1.png"), pygame.image.load(base_path + "Run_backwards_2.png")]
stand_img = pygame.image.load(base_path + "stand.png")
crouch_img = pygame.image.load(base_path + "crouch(3).png")
jump_imgs = pygame.image.load(base_path + "Jump_1.png")
walk_right_imgs =[pygame.image.load(base_path + "Run_1.png"), pygame.image.load(base_path + "Run_2.png")]

# player object
player = Player(200, 500, 69, 88, 1, walk_right_imgs, walk_left_imgs, stand_img, crouch_img, jump_imgs, screen)
# book object
book = Book(random.randint(1409, 1410), 450,50,50,1,book_imgs)
book2 = None # second instance of book



# loading in start screen
start_screen(screen, bg,  WIDTH, HEIGHT, FONT)

clock = pygame.time.Clock()
start_time = time.time()
elapsed_time = 0

bgX, bgX2 = 0, bg.get_width() # for moving background

run = True
show_death_screen = False   # whether to show the death screen

# time count on screen to show elapsed time
def draw_time(elapsed_time):
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    screen.blit(time_text, (WIDTH/2, 10))

# game loop
while run:
    clock.tick(60)
    elapsed_time = time.time()- start_time

    # scrolling background logic:
    bgX  -=2
    bgX2 -=2
    player.move()   # player movement
    book.move()     # book movement
    
    # second book spawns when first book reaches mid-screen
    if book.x < WIDTH / 2 and book2 is None:
        book2 = Book(random.randint(1409, 1410), 450, 50, 50, 1, book_imgs)

    if book2 is not None:
        book2.move()

    # logic for infinite background scrolling
    

    # event handling
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            run = False 
            pygame.quit()

    render_background(screen, bg, bgX, bgX2)
    render_player(screen, player)
    render_book(screen, book)

    if book2 is not None:
        screen.blit(book2.img, book2.book_rect)

    # collision between player and book
    if player.player_rect.colliderect(book.book_rect):
        run = False
        show_death_screen = True  
    # collision between player and book2
    if book2 is not None and player.player_rect.colliderect(book2.book_rect):
        run = False
        show_death_screen = True  

    draw_time(elapsed_time)
    # draw death screen if player died    
    if not run and show_death_screen:
        draw_death_screen(screen, WIDTH, HEIGHT, FONT, elapsed_time)

        # game loop for if player decides to play again
        while True:
            for event in pygame.event.get():
                run, show_death_screen, start_time, book2 = handle_input(event, run, show_death_screen, start_time, player, book, book2)
                 
            if not show_death_screen:
                break
    # Fill white after player moves
    pygame.display.update()
    screen.fill((0, 0, 0))
pygame.quit()