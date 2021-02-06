import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
x, y = 0, 360

# 加载图片资源，函数返回的内容就是一个 Surface 对象实例
background_img = pygame.image.load('img/actor/bg.jpg')

standing_img = pygame.image.load('img/actor/standing.png')

# 向右边走的图片组
walk_right_imgs = [
    pygame.image.load('img/actor/R1.png'),
    pygame.image.load('img/actor/R2.png'),
    pygame.image.load('img/actor/R3.png'),
    pygame.image.load('img/actor/R4.png'),
    pygame.image.load('img/actor/R5.png'),
    pygame.image.load('img/actor/R6.png'),
    pygame.image.load('img/actor/R7.png'),
    pygame.image.load('img/actor/R8.png'),
    pygame.image.load('img/actor/R9.png')
]

# 向左边走的图片组
walk_left_imgs = [
    pygame.image.load('img/actor/L1.png'),
    pygame.image.load('img/actor/L2.png'),
    pygame.image.load('img/actor/L3.png'),
    pygame.image.load('img/actor/L4.png'),
    pygame.image.load('img/actor/L5.png'),
    pygame.image.load('img/actor/L6.png'),
    pygame.image.load('img/actor/L7.png'),
    pygame.image.load('img/actor/L8.png'),
    pygame.image.load('img/actor/L9.png')
]

# bilt 函数的作用可以理解为一个图章，可以在一个图片上面再盖一个图片，盖的顺序决定层次
screen.blit(background_img, (0, 0))
screen.blit(standing_img, (0, 360))
pygame.display.update()

img_index = 0

while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(background_img, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        # 使用 img_index 重复切换图片向左边走的动作
        screen.blit(walk_left_imgs[img_index % 9], (x, y))
        x -= 1
        img_index += 1
        pygame.display.update()
    if keys[pygame.K_RIGHT]:
        screen.blit(walk_right_imgs[img_index % 9], (x, y))
        x += 1
        img_index += 1
        pygame.display.update()
    # 防止出边界
    if x < -20:
        x = -20
    if x > 600:
        x = 600
pygame.quit()