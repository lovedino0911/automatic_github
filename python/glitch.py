import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glitch Text Background - Blue")

font = pygame.font.SysFont('arialblack', 100, bold=True)

TEXT = "Jin Sohyeon"
COLOR_BASE = (30, 144, 255)
COLOR_GLITCH1 = (0, 191, 255)
COLOR_GLITCH2 = (135, 206, 250)

clock = pygame.time.Clock()

def draw_glitch_text(text, x, y):
    base_text = font.render(text, True, COLOR_BASE)
    screen.blit(base_text, (x, y))
    
    offset_x1 = random.randint(-5, 5)
    offset_y1 = random.randint(-3, 3)
    glitch1 = font.render(text, True, COLOR_GLITCH1)
    screen.blit(glitch1, (x + offset_x1, y + offset_y1))
    
    offset_x2 = random.randint(-3, 3)
    offset_y2 = random.randint(-5, 5)
    glitch2 = font.render(text, True, COLOR_GLITCH2)
    screen.blit(glitch2, (x + offset_x2, y + offset_y2))

def main():
    running = True
    while running:
        screen.fill((10, 10, 40))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        text_surface = font.render(TEXT, True, COLOR_BASE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
        draw_glitch_text(TEXT, text_rect.x, text_rect.y)
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
