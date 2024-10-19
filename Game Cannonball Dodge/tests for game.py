# IMPORTS

import pygame
import sys
import time
import math
import random

# COLORS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

# VARIABLES
window_width, window_height = 15 * 70, 10 * 70
print(window_width, window_height)  # DEBUG
x_center, y_center = window_width // 2, window_height // 2
c1 = 25
c2 = 2
c3 = c2 + c1

walls = []
cannonballs = []

# DEBUGGING VARIABLES
cannonball_count = 0
walls_count = 0
last_cannonball_spawn_time = time.time()


# FUNCTIONS:

# CLASSES:
class Player:
    def __init__(self, radius, speed, x, y):
        self.x, self.y = x, y  # Initial position
        self.radius = radius  # Radius of the player
        self.speed = speed  # Speed of the player

    def movement(self):
        top_radius = self.y - self.radius
        bottom_radius = self.y + self.radius
        left_radius = self.x - self.radius
        right_radius = self.x + self.radius

        touching_top_wall = (top_radius <= top_wall.y + top_wall.height)
        touching_bottom_wall = (bottom_radius >= bottom_wall.y)

        touching_left_wall = (left_radius <= left_wall.x + left_wall.width)
        touching_right_wall = (right_radius >= right_wall.x)
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        # If the player touches a wall, the player will not move in the wall's direction.
        # This is to prevent the player from going through walls.
        if keys[pygame.K_UP] and not touching_top_wall:
            dy -= self.speed  # Move up # Negative y value
        if keys[pygame.K_DOWN] and not touching_bottom_wall:
            dy += self.speed  # Move down # Positive y value
        if keys[pygame.K_LEFT] and not touching_left_wall:
            dx -= self.speed  # Move left # Negative x value
        if keys[pygame.K_RIGHT] and not touching_right_wall:
            dx += self.speed  # Move right # Positive x value

        # S - S0 = v*t
        self.x += dx * self.speed  # Variation in x is dx*t
        self.y += dy * self.speed  # Variation in y is dy*t

        # Debugging
        if keys[pygame.K_SPACE]:
            print("Player",
                  (left_radius, right_radius),
                  (top_radius, bottom_radius))

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        #   print(f"X: {dx} | Y: {dy}")


class Wall:
    def __init__(self, name, color, x, y, width, height):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.x2 = x + width
        self.y2 = y + height
        self.width = width
        self.height = height


class Cannonball:
    def __init__(self, color, x, y, speed, radius, angle):
        self.color = color
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.angle = angle

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))


# DEFINING FUNCTIONS:

def spawn_cannonball(wall_list, cannonball_list):
    wall_choice = random.choice(wall_list)
    wall_name = wall_choice.name
    if wall_name == "Left wall":
        cannonball_x = left_wall.x2 + c2
        cannonball_y = random.randint(left_wall.y, left_wall.y2)
        cannonball_angle = random.randint(-89, 89)
        cannonball_color = left_wall.color

    elif wall_name == "Right wall":
        cannonball_x = right_wall.x - c2
        cannonball_y = random.randint(right_wall.y, right_wall.y2)
        cannonball_angle = random.randint(91, 269)
        cannonball_color = right_wall.color

    elif wall_name == "Top wall":
        cannonball_x = random.randint(top_wall.x, top_wall.x2)
        cannonball_y = top_wall.y2 + c2
        cannonball_angle = random.randint(1, 179)
        cannonball_color = top_wall.color

    elif wall_name == "Bottom wall":
        cannonball_x = random.randint(bottom_wall.x, bottom_wall.x2)
        cannonball_y = bottom_wall.y - c2
        cannonball_angle = random.randint(181, 359)
        cannonball_color = bottom_wall.color

    cannonball_radius = 9
    cannonball_speed = 2.5
    cannonball = Cannonball(cannonball_color, cannonball_x, cannonball_y, cannonball_speed, cannonball_radius,
                            cannonball_angle)
    print(f"X: {cannonball.x} | Y: {cannonball.y} | Angle: {cannonball.angle}")
    cannonball_list.append(cannonball)


def move_cannonballs(cannonball_list):
    for cannonball in cannonball_list:
        cannonball.move()


# INITIALIZE PYGAME
pygame.init()  # Initialize pygame
game_window = pygame.display.set_mode((window_width, window_height))  # Create the game window
pygame.display.set_caption('Cannon Ball Dodge Game')  # Set the title of the window
background = pygame.Surface(game_window.get_size()).convert()  # Create background
background.fill(BLACK)  # Fill background
clock = pygame.time.Clock()  # Create a clock to control the speed of the game.

# SET OBJECTS
player = Player(9, 2.5, x_center, y_center)  # Create player

top_wall = Wall("Top wall", PURPLE,
                x=(0 + c3), y=(0 + c2),
                width=(window_width - 2 * c3), height=c1)

bottom_wall = Wall("Bottom wall", RED,
                   x=(0 + c3), y=(window_height - c3),
                   width=(window_width - 2 * c3), height=c1)

left_wall = Wall("Left wall", YELLOW,
                 x=(0 + c2), y=(0 + c3),
                 width=c1, height=(window_height - 2 * c3))

right_wall = Wall("Right wall", GREEN,
                  x=(window_width - c3), y=(0 + c3),
                  width=c1, height=(window_height - 2 * c3))

walls.append(top_wall)
walls.append(bottom_wall)
walls.append(left_wall)
walls.append(right_wall)

# DEBUGGING
for wall in walls:
    print(wall.name, (wall.x, wall.x2), (wall.y, wall.y2), (wall.width, wall.height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # GAME LOGIC
    player.movement()  # Move player
    if time.time() - last_cannonball_spawn_time >= 5:
        last_cannonball_spawn_time = time.time()
        print("Spawning cannonball")
        spawn_cannonball(walls, cannonballs)
    move_cannonballs(cannonballs)
    # TODO: Add collision detection
    for cannonball in cannonballs: # If a cannonball hits a wall, reflect the cannonball with an elastic collision
        # resolution.
        for wall in walls:
            if wall.name == "Left wall" and cannonball.x - cannonball.radius <= wall.x:
                cannonball.angle = 180 - cannonball.angle
            elif wall.name == "Right wall" and cannonball.x + cannonball.radius >= wall.x2:
                cannonball.angle = 180 - cannonball.angle
            elif wall.name == "Top wall" and cannonball.y - cannonball.radius <= wall.y:
                cannonball.angle = 360 - cannonball.angle
            elif wall.name == "Bottom wall" and cannonball.y + cannonball.radius >= wall.y2:
                cannonball.angle = 360 - cannonball.angle
    # If a cannonball hits the player, game over.

    # DRAW PHASE
    game_window.blit(background, (0, 0))  # Draw background
    pygame.draw.circle(game_window, WHITE, (player.x, player.y), player.radius)  # Draw player
    for wall in walls:  # Draw walls
        pygame.draw.rect(game_window, wall.color, (wall.x, wall.y, wall.width, wall.height))
    for cannonball in cannonballs:  # Draw cannonballs
        pygame.draw.circle(game_window, cannonball.color, (cannonball.x, cannonball.y), cannonball.radius)

    # REFRESH PHASE
    pygame.display.flip()
    clock.tick(60)
