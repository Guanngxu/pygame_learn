import pygame
import math

pygame.init()

screen = pygame.display.set_mode((400, 600))
screen.fill((255, 255, 255))
font = pygame.font.SysFont('Arial', 20)

# 加载按钮
pi = pygame.image.load('img/calculator/pi.png')
ac = pygame.image.load('img/calculator/ac.png')
num0 = pygame.image.load('img/calculator/py0.png')
num1 = pygame.image.load('img/calculator/py1.png')
num2 = pygame.image.load('img/calculator/py2.png')
num3 = pygame.image.load('img/calculator/py3.png')
num4 = pygame.image.load('img/calculator/py4.png')
num5 = pygame.image.load('img/calculator/py5.png')
num6 = pygame.image.load('img/calculator/py6.png')
num7 = pygame.image.load('img/calculator/py7.png')
num8 = pygame.image.load('img/calculator/py8.png')
num9 = pygame.image.load('img/calculator/py9.png')
plus = pygame.image.load('img/calculator/jia.png')
equal = pygame.image.load('img/calculator/deng.png')
minus = pygame.image.load('img/calculator/jian.png')
multiply = pygame.image.load('img/calculator/cheng.png')
divide = pygame.image.load('img/calculator/pychu.png')
point = pygame.image.load('img/calculator/pydian.png')
left_kuo = pygame.image.load('img/calculator/zkuo.png')
right_kuo = pygame.image.load('img/calculator/ykuo.png')

# 将按钮渲染到屏幕
screen.blit(plus, (0, 100))
screen.blit(minus, (100, 100))
screen.blit(multiply, (200, 100))
screen.blit(divide, (300, 100))

screen.blit(num1, (0, 200))
screen.blit(num2, (100, 200))
screen.blit(num3, (200, 200))
screen.blit(left_kuo, (300, 200))

screen.blit(num4, (0, 300))
screen.blit(num5, (100, 300))
screen.blit(num6, (200, 300))
screen.blit(right_kuo, (300, 300))

screen.blit(num7, (0, 400))
screen.blit(num8, (100, 400))
screen.blit(num9, (200, 400))
screen.blit(point, (300, 400))

screen.blit(ac, (0, 500))
screen.blit(pi, (100, 500))
screen.blit(num0, (200, 500))
screen.blit(equal, (300, 500))

# 存储表达式
expression = ''
# 空字符串行，用来清空计算器显示的位置
blank = '                                                                '
# 当前是否为计算结果
cal_ret = False

while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # 根据按键拼装表达式
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 如果当前 expression 存储的是上一次的运算结果，则在按键按下时应该清除上一次的运算结果
            if cal_ret:
                screen.blit(font.render(blank, True, (0, 0, 0), (255, 255, 255)), (0, 40))
                pygame.display.update()
                expression = ''
                cal_ret = False
            x, y = pygame.mouse.get_pos()
            if 0 <= x <= 100 and 100 <= y <= 200:
                expression += '+'
            if 100 <= x <= 200 and 100 <= y <= 200:
                expression += '-'
            if 200 <= x <= 300 and 100 <= y <= 200:
                expression += '*'
            if 300 <= x <= 400 and 100 <= y <= 200:
                expression += '/'
            
            if 0 <= x <= 100 and 200 <= y <= 300:
                expression += '1'
            if 100 <= x <= 200 and 200 <= y <= 300:
                expression += '2'
            if 200 <= x <= 300 and 200 <= y <= 300:
                expression += '3'
            if 300 <= x <= 400 and 200 <= y <= 300:
                expression += '('

            if 0 <= x <= 100 and 300 <= y <= 400:
                expression += '4'
            if 100 <= x <= 200 and 300 <= y <= 400:
                expression += '5'
            if 200 <= x <= 300 and 300 <= y <= 400:
                expression += '6'
            if 300 <= x <= 400 and 300 <= y <= 400:
                expression += ')'
            
            if 0 <= x <= 100 and 400 <= y <= 500:
                expression += '7'
            if 100 <= x <= 200 and 400 <= y <= 500:
                expression += '8'
            if 200 <= x <= 300 and 400 <= y <= 500:
                expression += '9'
            if 300 <= x <= 400 and 400 <= y <= 500:
                expression += '.'

            # ac 清空按键
            if 0 <= x <= 100 and 500 <= y <= 600:
                screen.blit(font.render(blank, True, (0, 0, 0), (255, 255, 255)), (0, 40))
                pygame.display.update()
                expression = ''
            if 100 <= x <= 200 and 500 <= y <= 600:
                expression += 'math.pi'
            if 200 <= x <= 300 and 500 <= y <= 600:
                expression += '0'
            if 300 <= x <= 400 and 500 <= y <= 600:
                screen.blit(font.render(blank, True, (0, 0, 0), (255, 255, 255)), (0, 40))
                pygame.display.update()
                # 如果表达式不合法则显示错误：error
                try:
                    expression = str(eval(expression))
                except:
                    expression = 'error'
                cal_ret = True
    screen.blit(font.render(expression, True, (0, 0, 0), (255, 255, 255)), (0, 40))
    pygame.display.update()
    