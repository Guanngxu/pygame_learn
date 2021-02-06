import pygame

pygame.init()
# 设置窗口大小
screen = pygame.display.set_mode((400, 400))
x, y = 0, 0
while True:
    # 要有延时，防止 CPU 跑死
    pygame.time.delay(10)
    for event in pygame.event.get():
        # 一定要有 quit 事件的判断，不然点击关闭按钮不会生效
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 5
            if event.key == pygame.K_RIGHT:
                x += 5
            # pygame 的坐标轴，x 轴朝右，y 轴朝下，所以向上时候 y 轴坐标应该变小
            if event.key == pygame.K_UP:
                y -= 5
            if event.key == pygame.K_DOWN:
                y += 5
    # 上面的按键检测方法的特点是，每按一次键只会响应一次，不能实现长按某个按键一直移动的效果
    # 下面这一段代码的按键检测方法可以实现长按一直移动的效果
    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    '''
    # 防止方块走出边界了
    if x < 0:
        x = 0
    # 为什么是 360？因为方块的宽设置的是 40 ，而窗口大小设置的是 400，方块的坐标默认是左上角顶点，所以应该是 400-40
    if x > 360:
        x = 360
    if y < 0:
        y = 0
    if y > 360:
        y = 360
    # 将窗口背景颜色设置为白色，这一句和下面画方块的一句不能对调顺序，否则不会出现红色方块
    screen.fill((255, 255, 255))
    # 画一个正方形，screen 表示在哪个地方画，第二个参数表示正方形的颜色，第三个参数中的四个数字中，前两个表示坐标，后两个表示长宽
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 40))
    # 对页面的内容修改了，需要刷新窗口才能看到
    pygame.display.update()
pygame.quit()