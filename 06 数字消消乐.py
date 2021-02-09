import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
# 设置字体和字号
font = pygame.font.SysFont('微软雅黑', 80)
# 随机生成 1-9 的数字和坐标，因为是从上往下掉，所以 y 坐标最开始都为 0
def gen_word():
    word = random.randint(0, 9)
    # x 的取值范围在 0-720，是因为窗口宽度为 800，字号大小为 80，所以 x 最大时取 800 - 720
    x = random.randint(0, 720)
    return word, x, 0

words = []
# 每隔多少毫秒就掉下来一个数字
step = 800
# 一开始设为 8000 毫秒是因为 pygame 启动需要时间，不然等窗口弹出来时就已经出现了一大堆数字
total_time = 8000

while True:
    pygame.time.delay(10)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if len(words) > 0 and event.type == pygame.KEYDOWN:
            # 按键 0 的值是 48，1 的值是 49，依次类推
            if event.key == words[0][0]+48:
                words.pop(0)
    keys = pygame.key.get_pressed()
    # pygame.time.get_ticks() 返回从 pygame.init() 开始到现在的时间
    cur_time = pygame.time.get_ticks()
    if cur_time > total_time:
        words.append(gen_word())
        total_time += step
    length = len(words)
    # 将数字渲染到屏幕上面
    for i in range(length):
        word, x, y = words[i]
        # 使用 render 方法转换为 Surface 对象，方便渲染使用
        text_img = font.render(str(word), True, (0, 0, 0))
        screen.blit(text_img, (x, y))
        # 每次对当前的数字向下移动一步
        words[i] = word, x, y+1
    pygame.display.update()