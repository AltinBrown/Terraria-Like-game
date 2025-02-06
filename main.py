import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 64

# Screen_W/H
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 840
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PYGAME_GAME")

# Define game variables
tile_size = 50

bg_img = pygame.image.load('IMG/BG_img.png')

# World data
world_data = [
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 5, 5, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0],
]

def draw_grid():
    # Get dimensions of world_data
    rows = len(world_data)
    cols = len(world_data[0])

    # Draw horizontal grid lines
    for line in range(0, rows + 1):
        pygame.draw.line(screen, "Red", (0, line * tile_size), (SCREEN_WIDTH, line * tile_size))
    # Draw vertical grid lines
    for line in range(0, cols + 1):  # One extra line for the right side
        pygame.draw.line(screen, "Blue", (line * tile_size, 0), (line * tile_size, SCREEN_HEIGHT))


class Player:
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f"IMG/DUDE{num}.png")
            img_right = pygame.transform.scale(img_right, (40, 110))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.vel_x = 0
        self.acceleration = 2
        self.max_speed = 20
        self.friction = -0.1

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 10

        # Get KEY PRESS
        key = pygame.key.get_pressed()

        # Check if the player is on the ground (collision with the world tiles)
        on_ground = False
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y + 1, self.width, self.height):
                on_ground = True
                break

        # Only allow jumping if the player is on the ground
        if key[pygame.K_SPACE] and not self.jumped and on_ground:
            self.vel_y = -20  # The Jump force
            self.jumped = True

        if not key[pygame.K_SPACE]:
            self.jumped = False

        if key[pygame.K_a]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_d]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if not key[pygame.K_a] and not key[pygame.K_d]:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # Apply friction to vertical movement
        self.vel_y += self.vel_y * self.friction

        # Ensure the player does not exceed max speed
        if self.vel_y > self.max_speed:
            self.vel_y = self.max_speed
        if self.vel_y < -self.max_speed:
            self.vel_y = -self.max_speed

        dy += self.vel_y

        # Animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # Gravity
        self.vel_y += 1  # Gravity force
        dy += self.vel_y

        # Check for collisions with tiles
        for tile in world.tile_list:
            # x direction collision
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            # y direction collision
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.vel_y < 0:  # If moving upwards (jumping)
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:  # If falling down
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.jumped = False  # Player is grounded

        # Update player position
        self.rect.x += dx
        self.rect.y += dy

        # Prevent the player from falling below the screen
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.jumped = False  # Reset jump state when touching the ground

        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, 'Red', self.rect, 2)


class World:
    def __init__(self, data):
        self.tile_list = []
        # Load dirt image once
        self.dirt_img = pygame.image.load('IMG/dirt.png')
        self.grass_img = pygame.image.load('IMG/grass.png')
        self.corner_img = pygame.image.load('IMG/corner.png')
        self.grass_to_dirt_img = pygame.image.load('IMG/grass_to_dirt.png')
        self.COBLE_img = pygame.image.load('IMG/COBLE.png')

        # Scale the dirt image to fit the tile size
        self.dirt_img = pygame.transform.scale(self.dirt_img, (tile_size, tile_size))
        self.grass_img = pygame.transform.scale(self.grass_img, (tile_size, tile_size))
        self.corner_img = pygame.transform.scale(self.corner_img, (tile_size, tile_size))
        self.grass_to_dirt_img = pygame.transform.scale(self.grass_to_dirt_img, (tile_size, tile_size))
        self.COBLE_img = pygame.transform.scale(self.COBLE_img, (tile_size, tile_size))

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = self.dirt_img
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                if tile == 2:
                    img = self.grass_img
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                if tile == 3:
                    img = self.corner_img
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                if tile == 4:
                    img = self.grass_to_dirt_img
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                if tile == 5:
                    img = self.COBLE_img
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                col_count += 1
            row_count += 1

    def draw(self):
        # Draw all tiles in the tile list
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            # pygame.draw.rect(screen, 'Blue', tile[1], 2)


player = Player(100, 650)
# Create the world with world_data
world = World(world_data)

run = True
while run:
    clock.tick(fps)

    # Draw the background image first
    screen.blit(bg_img, (0, 0))

    # Draw the world (tiles)
    world.draw()
    player.update()

    # Draw the grid on top
    # draw_grid()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update the screen
    pygame.display.update()

pygame.quit()