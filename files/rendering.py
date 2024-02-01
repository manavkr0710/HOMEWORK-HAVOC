import pygame

def render_background(screen, bg, bgX, bgX2):
    screen.blit(bg, (0, 0))
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX2, 0))

def render_player(screen, player):
    if player.crouching:
        player.y += 50
        player.player_rect.y += 50
        screen.blit(player.crouch_img, (player.x, player.y))
    else:
        screen.blit(player.img, player.player_rect)

def render_book(screen, book):
    screen.blit(book.img, book.book_rect)