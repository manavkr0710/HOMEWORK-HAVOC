import pygame
import random

class Book:
    def __init__(self, x, y, width, height,scale, book_imgs):
        self.x, self.y= x, y
        self.width, self.height = width, height
        self.scale = scale
        self.book_imgs = book_imgs
        self.book_rect = pygame.Rect(x, y, 40, 35)
        self.book_rect.center = (x, y)
        self.speed = random.randint(10,25) # speed for book 
        self.current_frame = 0 #keeps track of current frame
        self.animation_speed = 10 # control of animation speed
        self.animation_counter = 0  #tracks the time elapsed since last frame was displayed
        self.isalive = True
        
        self.img = pygame.transform.scale(self.book_imgs[self.current_frame],
                                                (int(self.width * self.scale), int(self.height * self.scale)))  # Initialize img attribute  
    def move(self):
        if self.isalive:   
            self.x-= self.speed
            #each time animation is performed, animation counter increments
            self.animation_counter += 1
            if self.animation_counter >= self.animation_speed:
                self.current_frame += 1

                #setting it to the initial state of movement
                if self.current_frame >= len(self.book_imgs):
                    self.current_frame = 0

                    #choosing which image from the list with self.current frame
                self.img = pygame.transform.scale(self.book_imgs[self.current_frame],(int(self.width * self.scale), int(self.height * self.scale)))
                #resetting for next animation cycle
                self.animation_counter = 0
                print(self.y)

            self.update()

    def update(self):
        if self.x <0:
            self.x = 1400
            self.y = random.randint(450, 515)
            self.speed = random.randint(10,25)

        self.book_rect.width, self.book_rect.height = self.width, self.height
        self.book_rect.x, self.book_rect.y = self.x, self.y

    def reset(self):
        self.x = 1400
        self.y = random.randint(450, 530)
        self.speed = random.randint(10, 25)