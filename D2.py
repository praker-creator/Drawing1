import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1080, 1920
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 80, bold=True)

text = "PRAKER BOY"
draw_text = ""

index = 0
timer = 0
t = 0

running = True
typing = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 15, 30))

    timer += 0.5

    if timer >= 8:
        timer = 0

        if typing:
            index += 1
            if index >= len(text):
                typing = False
        else:
            index -= 1
            if index <= 0:
                typing = True

    draw_text = text[:index]
        
    for i in range(250):
        x = WIDTH // 2 + math.cos(i * 0.1 + t) * i * 1.5
        y = HEIGHT // 2 + math.sin(i * 0.001 + t) * i * 1.5

        color = (
            (i * 5) % 255,
            (i * 3) % 255,
            (i * 7) % 255
        )

        pygame.draw.rect(screen, color, (int(x), int(y), 4, 4))


    r = int(128 + 127 * math.sin(t))
    g = int(128 + 127 * math.sin(t + 2))
    b = int(128 + 127 * math.sin(t + 4))

    surface = font.render(draw_text, True, (r, g, b))

    rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(surface, rect)

    pygame.display.flip()

    t += 0.03
    clock.tick(60)

pygame.quit()