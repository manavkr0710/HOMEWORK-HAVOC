import pygame

class Player:
    def __init__(self, x, y, width, height, scale, walk_right_imgs, walk_left_imgs, stand_img, crouch_img, jump_imgs, screen):
        self.x, self.y = x, y # x, y coordinate of player
        self.ground_y = self.y # ground y coordinate, same as player y coordinate
        self.scale = scale # scale for player image
        self.width, self.height  = width, height
        
        self.walk_right_imgs = walk_right_imgs # images for walking right
        self.walk_left_imgs = walk_left_imgs #  images for walking left
        self.stand_img = stand_img      # image for standing
        self.crouch_img = crouch_img
        self.jump_imgs = jump_imgs      # images for jumping
        self.screen = screen
    
        self.player_rect = pygame.Rect(x, y, width, height) # player rectangle
        self.player_rect.center = (x, y) # center of player
        self.speed = 5# speed for walking left or right

        # for sprite animations
        self.current_frame = 0 # keeps track of current frame
        self.animation_speed = 10 # control of animation speed
        self.animation_counter = 0  # time elapsed since last frame was displayed
        self.direction = 0  # 0 for idle, 1 for right, -1 for left
        
        self.alive = True
        self.jump = False
        self.crouching = False

        self.GRAVITY = 1
        self.vel_y =0
        self.vel_x = 0
        self.vel_y += self.GRAVITY
        self.max_jump_height = self.ground_y-150 # the ceiling that the character can jump

    # reset values if player plays again
    def reset(self):
        self.x, self.y = 200, 500
        self.vel_y = 0
        self.alive = True
       
    # movement logic
    def move(self):
        keys = pygame.key.get_pressed()
        if self.alive:
            if keys[pygame.K_UP] and not self.jump and self.alive:
                self.jump = True
                self.vel_y = self.speed * -5
                self.jump_start_y = self.y
                self.animate_jump()

            if keys[pygame.K_DOWN] and not self.jump and self.alive:
                self.crouching = True
                self.animate_crouch()
                self.vel_y = 0  # Set vertical velocity to 0 while crouching
            else:
                # moving left/right
                self.crouching = False
                if not self.jump:
                    if keys[pygame.K_RIGHT] and self.alive:
                        self.x += self.speed
                        if self.x > 1250 - self.width:
                            self.x = 1250 - self.width
                        self.direction = 1
                        self.animate_right()

                    elif keys[pygame.K_LEFT] and self.alive:
                        self.x -= self.speed * 1.25
                        if self.x < 0:
                            self.x = 0
                        self.direction = -1
                        self.animate_left()
                    #standing
                    elif not self.jump:
                        self.animate_stand()
                        self.animation_counter += 1

        # Horizontal movement during jump
        if self.jump:
            self.x += self.vel_x

            if keys[pygame.K_RIGHT] and self.alive:
                self.x += self.speed
                if self.x > 1250 - self.width:
                    self.x = 1250 - self.width
                    self.animate_jump()

            elif keys[pygame.K_LEFT] and self.alive:
                self.x -= self.speed * 1.25
                if self.x < 0:
                    self.x = 0
                self.animate_jump()

        # gravity
        self.vel_y += self.GRAVITY
        self.y += self.vel_y

        if self.y <= self.max_jump_height:
            self.y = self.max_jump_height
            self.vel_y = 0

        if self.y > self.ground_y:
            self.y = self.ground_y
            self.vel_y = 0
            self.jump = False

        self.update()

    def animate_crouch(self):
            self.img = pygame.transform.scale(self.crouch_img,(int(self.width * self.scale) , int(self.height * self.scale)))

    def animate_jump(self):
        # Choose the appropriate jump image based on the player's direction
        if self.direction == 1:
            self.vel_x = self.speed  # Move right during jump
            self.img = pygame.transform.scale(self.jump_imgs,(int(self.width * self.scale), int(self.height * self.scale)))
        
        if self.direction == -1:
            self.vel_x = -self.speed  # Move left during jump
            flipped_jump_imgs = pygame.transform.flip(self.jump_imgs, True, False)
            self.img = pygame.transform.scale(flipped_jump_imgs, (int(self.width * self.scale), int(self.height * self.scale)))
            
    def animate_stand(self):
        self.img = pygame.transform.scale(self.stand_img,(int(self.width * self.scale), int(self.height * self.scale)))
  
    def animate_right(self):
        # each time animation is performed, animation counter increments
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.current_frame += 1
            # set it to the initial state of movement
            if self.current_frame >= len(self.walk_right_imgs):
                self.current_frame = 0
                # choose which image from list with self.current frame
            self.img = pygame.transform.scale(self.walk_right_imgs[self.current_frame],(int(self.width * self.scale), int(self.height * self.scale)))
            #reset for next animation cycle
            self.animation_counter = 0

    def animate_left(self):
        # each time animation is performed, animation counter increments
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.current_frame += 1
            # set it to the initial state of movement
            if self.current_frame >= len(self.walk_left_imgs):
                self.current_frame = 0
                # choose which image from list with self.current frame
            self.img = pygame.transform.scale(self.walk_left_imgs[self.current_frame],(int(self.width * self.scale), int(self.height * self.scale))) 
            # reset for next animation cycle
            self.animation_counter = 0

    #updates pos of player's imaginary rectangle
    def update(self):
        if not self.jump and self.y == self.ground_y:
            self.vel_x = 0

        self.player_rect.x, self.player_rect.y = self.x, self.y
        self.player_rect.width, self.player_rect.height = self.width, self.height