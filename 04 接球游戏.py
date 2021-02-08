import pygame
import random

pygame.init()
ball_x, ball_y = 0, 0
# 小球的速度随机取，注意挡板移动的速度是 2，所以小球的速度不能超过 2 
ball_speed_x, ball_speed_y = random.randint(1, 2), random.randint(1, 2)
baf_x, baf_y = 270, 380
screen = pygame.display.set_mode((600, 400))

while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # 防止走出边界
    if baf_x < 0:
        baf_x = 0
    if baf_x > 540:
        baf_x = 540
    # 键盘移动挡板
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        baf_x += 2
    if keys[pygame.K_LEFT]:
        baf_x -= 2
    # 小球碰到边界和挡板反弹
    if ball_x < 0 or ball_x > 585:
        ball_speed_x = -ball_speed_x
    # 碰撞检测原理：小球的坐标和挡板的坐标相等，注意这里的相等是个范围
    if ball_y < 0 or (ball_y+15 < baf_y+2 and ball_y+15 > baf_y-2 and ball_x >= baf_x-10 and ball_x <= baf_x+70):
        ball_speed_y = -ball_speed_y
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    screen.fill((255, 255, 255))
    # 画出小球
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 15)
    # 画出挡板
    pygame.draw.rect(screen, (0, 255, 0), (baf_x, baf_y, 60, 15))
    pygame.display.update()