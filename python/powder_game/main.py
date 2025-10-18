# setting
import pygame

pygame.init()

# screen
width, height = 800, 650
pixel_size = 5
screen_width, screen_height = width * pixel_size, height * pixel_size

screen = pygame.display.set_mode((width, height))
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
def gravity() :
    for y in range(height - 2, -1, -1) :
        for x in range(width) :
            if grid[y][x] == sand and grid[y+1][x] == empty :
                grid[y+1][x] = sand
                grid[y][x] = empty
                
                rect1 = pygame.Rect(x*pixel_size, y*pixel_size, pixel_size, pixel_size)
                rect2 = pygame.Rect(x*pixel_size, (y+1)*pixel_size, pixel_size, pixel_size)
                pygame.draw.rect(screen, colors[empty], rect1)
                pygame.draw.rect(screen, colors[sand], rect2)
                pygame.display.update([rect1, rect2])

           
# main loop
running = True
while running :
    clock.tick(120)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        # creating sand
        if pygame.mouse.get_pressed()[0] :
                mx, my = pygame.mouse.get_pos()
                gx = mx // pixel_size
                gy = my // pixel_size

                if 0 <= gx < width and 0 <= gy < height :
                        grid[gy][gx] = sand
                        rect = pygame.Rect(gx*pixel_size, gy*pixel_size, pixel_size, pixel_size)
                        pygame.draw.rect(screen, colors[sand], rect)
                        pygame.display.update(rect)    

    gravity()


    pygame.display.flip()