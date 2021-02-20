import pygame

pygame.init()

font = pygame.font.SysFont('Arial', 40)
screen = pygame.display.set_mode((680, 680))
# 绿豆色，护眼色
screen.fill((199, 238, 206 ))
# 控制棋盘颜色，True 为白棋，False 为黑棋
chess_color_flag = True

# 画棋盘
for i in range(15):
    pygame.draw.line(screen, (0, 0, 0), (60+i*40, 60), (60+i*40, 620))
for i in range(15):
    pygame.draw.line(screen, (0, 0, 0), (60, 60+i*40), (620, 60+i*40))

# 存储棋盘，空为 -1，白棋为 True，黑棋为 False，均初始化为 -1
chess_arr = []
for i in range(15):
    cur = []
    for j in range(15):
        cur.append(-1)
    chess_arr.append(cur)

def check_win(chess_arr, index_x, index_y, color):
    length = 1
    x, y = index_x, index_y
    # 左右直线方向
    while x <= 14 and chess_arr[x+1][y] == chess_arr[x][y]:
        length += 1
        x += 1
    x, y = index_x, index_y
    while x >= 0 and chess_arr[x-1][y] == chess_arr[x][y]:
        length += 1
        x -= 1
    if length == 5:
        return True
    else:
        length = 1
    # 上下直线方向
    x, y = index_x, index_y
    while y <= 14 and chess_arr[x][y+1] == chess_arr[x][y]:
        length += 1
        y += 1
    x, y = index_x, index_y
    while x >= 0 and chess_arr[x][y-1] == chess_arr[x][y]:
        length += 1
        y -= 1
    if length == 5:
        return True
    else:
        length = 1
    # 正比例函数方向
    x, y = index_x, index_y
    while x <= 14 and y <= 14 and chess_arr[x+1][y+1] == chess_arr[x][y]:
        length += 1
        x += 1
        y += 1
    x, y = index_x, index_y
    while x >= 0 and y >= 0 and chess_arr[x-1][y-1] == chess_arr[x][y]:
        length += 1
        x -= 1
        y -= 1
    if length == 5:
        return True
    else:
        length = 1
    # 反比例函数方向
    x, y = index_x, index_y
    while x >= 0 and y <= 14 and chess_arr[x-1][y+1] == chess_arr[x][y]:
        length += 1
        x -= 1
        y += 1
    x, y = index_x, index_y
    while y >= 0 and x <= 14 and chess_arr[x+1][y-1] == chess_arr[x][y]:
        length += 1
        x += 1
        y -= 1
    if length == 5:
        return True
    else:
        length = 1

while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # 计算点击的是第几个单元格，本来应该为 x-60+20 每个单元格的大小为 40
            index_x = int((x-40)/40)
            index_y = int((y-40)/40)
            # x > 40 and y > 40 是因为点击太左边和太上边的时候，也会出现棋子，外面的空白为 60，所以点击点靠近棋盘时才算
            # 0 <= index_x <= 14 and 0 <= index_y <= 14 是因为点击空白处可能会算成 15 -1 之类的数字，导致数组越界
            if x > 40 and y > 40 and 0 <= index_x <= 14 and 0 <= index_y <= 14 and chess_arr[index_x][index_y] == -1:
                chess_arr[index_x][index_y] = chess_color_flag
                chess_color = (255, 255, 255) if chess_color_flag else (0, 0, 0)
                # 渲染棋子，直接使用 circle 函数在指定位置画出即可
                pygame.draw.circle(screen, chess_color, (index_x*40+60, index_y*40+60), 16, 16)
                if check_win(chess_arr, index_x, index_y, chess_color_flag):
                    screen.blit(font.render('game over', True, (255, 0, 0)), (240, 300))
                # 反转颜色
                chess_color_flag = not chess_color_flag
    pygame.display.update()