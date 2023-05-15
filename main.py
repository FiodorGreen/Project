import pygame
from help_func import *
pygame.font.init()

WIDTH = 960
HEIGHT = 680
FPS = 60

num, data = count_of(14)
print('ok')
data = remove_repetition(change_for_command(data))
print('ok')
if num != len(data):
    raise TypeError("Wrong")
index = 0

surf_text = pygame.Surface((160, 40))
f1 = pygame.font.Font(None, 36)

surf = pygame.Surface((WIDTH, HEIGHT))
surf.fill((255, 255, 255))
for i in range(1, WIDTH // 40):
    pygame.draw.line(surf, (0, 0, 0), (i * 40, 0), (i * 40, HEIGHT))
for i in range(1, HEIGHT // 40):
    pygame.draw.line(surf, (0, 0, 0), (0, i * 40), (WIDTH, i * 40))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                index = (index - 1) % num
            if event.key == pygame.K_RIGHT:
                index = (index + 1) % num

    screen.blit(surf, (0, 0))

    pygame.draw.polygon(screen, (200, 40, 40), create_poly_coords(data[index]))


    surf_text.fill((255, 255, 255))
    text1 = f1.render(f"{index + 1} / {num}", True, (0, 0, 0))
    surf_text.blit(text1, (10, 10))

    screen.blit(surf_text, (0, 0))

    pygame.display.flip()
pygame.quit()

