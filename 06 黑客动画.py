import pygame
import random

pygame.init()

screen = pygame.display.set_mode()
surface = pygame.Surface((1500, 800), flags=pygame.SRCALPHA) 
# 设置字体和字号
font = pygame.font.SysFont('Arial', 20)
screen.fill((0, 0, 0))
# 第四个参数为 alpha 通道，表示透明度的意思，取值范围为 0～255
surface.fill((0, 0, 0, 28))
# 在屏幕上显示的文字
words = ['1', 's', 'd', 'a', 'f', '3', 'h', 'o', 'n', 'p', '?', '}']
# 使用生成器将文字变成 Surface 对象
texts = [font.render(str(i), True, (0, 255, 0)) for i in words]
# 计算总共有多少列，屏幕宽度为 1500，字号为 20
cols = int(1500/20)
# 每个字母的 y，所有字母都是从屏幕最上面掉下来的，所以一开始 y 坐标都为 0
# 总共有 cols 列，所以需要生成 cols 个 0
pos_y = [0 for i in range(cols)]
while True:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(surface, (0, 0))
    for i in range(cols):
        text = random.choice(texts)
        screen.blit(text, (i*20, pos_y[i]*20))
        pos_y[i] += 1
        if pos_y[i] * 10 > 800 or random.random() > 0.95:
            pos_y[i] = 0
    pygame.display.update()

# 实现该黑客动画的原理是让每一列有很多不同的字母逐渐向下移动，每一次移动都在上面加上一层遮盖布 surface
# 因为 surface 是半透明的，随着遮盖布的层数增加，则之前的字母会被完全遮住，层数越少字母越明显
# 所以最终看起来的效果是字母从上掉下来，并且颜色会逐渐的加深