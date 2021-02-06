import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen, (255, 0, 0), (40, 40, 40, 40))
    pygame.display.update()
pygame.quit()