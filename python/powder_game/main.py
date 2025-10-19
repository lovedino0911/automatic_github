# setting
import pygame
import random

pygame.init()

# screen
width, height = 160, 130
pixel_size = 5                                                                                                               
screen_width, screen_height = width * pixel_size, height * pixel_size

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("파우더 게임 by @lovedino")
clock = pygame.time.Clock()

# pixel type
empty = 0
sand = 1
water = 2
fire = 3

colors = {
    empty: (0, 0, 0), 
    sand: (194, 178, 128), 
    water: (64, 164, 223), 
    fire: (255, 100, 0)
    }

grid = [[empty for _ in range(width)] for _ in range(height)]


# functions

def draw_grid():
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x*pixel_size, y*pixel_size, pixel_size, pixel_size)
            pygame.draw.rect(screen, colors[grid[y][x]], rect) 

def gravity() :
    for y in range(height - 2, -1, -1) :
        for x in range(width) :
            # sand
            if grid[y][x] == sand :
                if grid[y+1][x] == empty :
                    grid[y+1][x] = sand
                    grid[y][x] = empty
                else:
                    for dx in [-1, 1]:
                        nx = x + dx
                        if 0 <= nx < width and grid[y+1][nx] == empty:
                            grid[y+1][nx] = sand
                            grid[y][x] = empty
                            break 
            # water
            elif grid[y][x] == water:
                moved = False
                # down
                if grid[y+1][x] == empty:
                    grid[y+1][x] = water
                    grid[y][x] = empty
                    moved = True
                else:
                    # left and right ~ 5, 바닥 위에서만
                    offsets = list(range(1, 6))
                    dirs = [-1, 1]
                    random.shuffle(dirs)  
                    random.shuffle(offsets)
                    for offset in offsets:
                        for dx in dirs:
                            nx = x + dx * offset
                            if (0 <= nx < width and
                                grid[y][nx] == empty and
                                grid[y+1][nx] != empty):
                                grid[y][nx] = water
                                grid[y][x] = empty
                                moved = True
                                break
                        if moved:
                            break

                if not moved :
                    dirs = [-1, 1]
                    random.shuffle(dirs)  
                    for dx in dirs:
                        nx = x + dx
                        if 0 <= nx < width and grid[y][nx] == empty:
                            grid[y][nx] = water
                            grid[y][x] = empty
                            break 
    
    # fire, water interection
    if current_pixel == fire and pygame.mouse.get_focused() :
        mx, my = pygame.mouse.get_pos()
        gx = mx // pixel_size
        gy = my // pixel_size
        fire_r = 8
        for dx in range(-fire_r, fire_r + 1) :
            for dy in range(-fire_r, fire_r + 1) :
                nx, ny = gx + dx, gy + dy
                if 0 <= nx < width and 0 <= ny < height :
                    dist = (dx**2 + dy**2)**0.5
                    if dist <= fire_r and grid[ny][nx] == water :
                        grid[ny][nx] = empty # 증발
                            
def draw_fire() :
    if current_pixel == fire and pygame.mouse.get_focused() :
        mx, my = pygame.mouse.get_pos()
        gx = mx // pixel_size
        gy = my // pixel_size
        fire_color = (255, 50, 0, 120)
        fire_r = 8
        fire_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        for dx in range(-fire_r, fire_r + 1) :
            for dy in range(-fire_r, fire_r + 1) :
                nx, ny = gx + dx, gy + dy
                if 0 <= nx < width and 0 <= ny < height :
                    dist = (dx**2 + dy**2)**0.5
                    if dist <= fire_r and random.random() > (dist / fire_r) * 0.6 :
                        # random fire
                        t = dist / fire_r
                        # yellow and outside
                        if t < 0.3 :
                            base_color = (255, 255, random.randint(0, 80), random.randint(180, 255))
                        elif t < 0.7 :
                            base_color = (255, random.randint(120, 200), 0, random.randint(120, 200))
                        else :
                            base_color = (255, random.randint(0, 80), 0, random.randint(60, 120))
                        rect = pygame.Rect(nx*pixel_size, ny*pixel_size, pixel_size, pixel_size)
                        fire_surface.fill(base_color, rect)
        screen.blit(fire_surface, (0, 0))


current_pixel = sand


# main loop
running = True
while running :
    clock.tick(120)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_pixel = sand
            elif event.key == pygame.K_2:
                current_pixel = water
            elif event.key == pygame.K_3:
                current_pixel = fire
                # add...

    if pygame.mouse.get_pressed()[0] and current_pixel != fire :
        mx, my = pygame.mouse.get_pos()
        gx = mx // pixel_size
        gy = my // pixel_size
        if 0 <= gx < width and 0 <= gy < height:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = gx + dx, gy + dy
                    if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == empty :
                        grid[ny][nx] = current_pixel

    gravity()
    draw_grid()
    draw_fire()

    pygame.display.flip()