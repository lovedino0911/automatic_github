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
particles = []
particle_buttons = [
    {"type" : sand, "rect" : pygame.Rect(20, screen_height - 70, 70, 50)},
    {"type" : water, "rect" : pygame.Rect(110, screen_height - 70, 70, 50)},
    {"type" : fire, "rect" : pygame.Rect(200, screen_height - 70, 70, 50)}
]

button_font = pygame.font.SysFont("malgungothic", 28)

# functions

def draw_grid():
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x*pixel_size, y*pixel_size, pixel_size, pixel_size)
            pygame.draw.rect(screen, colors[grid[y][x]], rect)

def draw_particles() :
    for p in particles[ : ] :
        px = int(p["x"] * pixel_size)
        py = int(p["y"] * pixel_size)
        surf = pygame.Surface((pixel_size, pixel_size), pygame.SRCALPHA)
        surf.fill(p["color"])
        screen.blit(surf, (px, py))
        # move particles
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["life"] -= 1
        if p["life"] < 8:
            alpha = max(0, int(p["color"][3] * p["life"] / 8))
            p["color"] = (p["color"][0], p["color"][1], p["color"][2], alpha)
        if p["life"] <= 0 or p["y"] < 0:
            particles.remove(p)

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
            elif grid[y][x] == water :
                # down
                if grid[y+1][x] == empty:
                    grid[y+1][x] = water
                    grid[y][x] = empty
                else:
                    # left and right ~ 5, 바닥 위에서만
                    offsets = list(range(1, 6))
                    random.shuffle(offsets)
                    dirs = [-1, 1]
                    random.shuffle(dirs)
                    moved = False
                    for offset in offsets:
                        for dx in dirs:
                            nx = x + dx * offset
                            if 0 <= nx < width:
                                if grid[y][nx] == empty and grid[y+1][nx] == empty:
                                    grid[y+1][nx] = water
                                    grid[y][x] = empty
                                    moved = True
                                    break
                                elif grid[y][nx] == empty and grid[y+1][nx] != empty:
                                    grid[y][nx] = water
                                    grid[y][x] = empty
                                    moved = True
                                    break
                        if moved:
                            break

              
    
    # fire, water interection
    if (
        current_pixel == fire 
        and pygame.mouse.get_focused() 
        and pygame.mouse.get_pressed()[0]
        and not click_blocked
    ) :
        mx, my = pygame.mouse.get_pos()
        gx = mx // pixel_size
        gy = my // pixel_size
        fire_r = 8
        for dx in range(-fire_r, fire_r + 1) :
            for dy in range(-fire_r, fire_r + 1) :
                nx, ny = gx + dx, gy + dy
                if 0 <= nx < width and 0 <= ny < height :
                    dist = (dx**2 + dy**2)**0.5
                    if dist <= fire_r and grid[ny][nx] in (water, sand) :
                        grid[ny][nx] = empty # burn
                        # effect
                        if random.random() < 0.3 :
                            particles.append({
                                "x" : nx,
                                "y" : ny,
                                "color" : (180, 180, 180, 120),
                                "life": random.randint(10, 20),
                                "vx": random.uniform(-0.5, 0.5),
                                "vy": random.uniform(-1.5, -0.5)
                            })
                            
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

def draw_info_button() :
    pygame.draw.rect(screen, (200, 200, 200), info_button_rect)
    pygame.draw.rect(screen, (100, 100, 100), info_button_rect, 2)
    text = font.render("INFO", True, (0, 0, 0))
    text_rect = text.get_rect(center = info_button_rect.center)
    screen.blit(text, text_rect)

def draw_info() :
    info_lines = [
        f"Current pixel : {'SAND' if current_pixel == sand else 'WATER' if current_pixel == water else 'FIRE'}",
        "Left click : create pixel",
        "FIRE : click to burn!"
    ]
    for i, line in enumerate(info_lines) :
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (20, 20 + i * 28))

def draw_particle_buttons() :
    for b in particle_buttons :
        color = colors[b["type"]]
        pygame.draw.rect(screen, color, b["rect"])
        pygame.draw.rect(screen, (255, 255, 255) if current_pixel == b["type"] else (100, 100, 100), b["rect"], 3)
        label = {sand : "SAND", water : "WATER", fire : "FIRE"}[b["type"]]
        text = font.render(label, True, (0, 0, 0))
        text_rect = text.get_rect(center = b["rect"].center)
        screen.blit(text, text_rect)


current_pixel = sand
info_button_rect = pygame.Rect(screen_width - 120, 20, 100, 40)
show_info = False
font = pygame.font.SysFont("malgungothic", 20)


# main loop
running = True
click_blocked = False

while running :
    clock.tick(120)
    skip_drawing_this_frame = False
    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if info_button_rect.collidepoint(event.pos):
                show_info = not show_info
                click_blocked = True
            else:
                for b in particle_buttons:
                    if b["rect"].collidepoint(event.pos):
                        current_pixel = b["type"]
                        click_blocked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            click_blocked = False


    if (
        pygame.mouse.get_pressed()[0] 
        and not click_blocked
        and current_pixel != fire
     ) :
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
    draw_particles()
    draw_fire()
    draw_info_button()
    if show_info :
        draw_info()
    draw_particle_buttons()

    pygame.display.flip()   