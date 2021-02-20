# pygame_learn

pygame 学习所做小项目，此文档记录了一点原理性的内容。

## 实现动画的原理

pygame 实现动画的原理和我们的电视机基本是一样的，每次都画出来一张静止的图画，通过快速的刷新页面，达到人眼已经无法辨别的频率时就是动画了，我们生活中的手翻书也是通过这样的原理实现动画的。

![手翻书.gif](https://i.loli.net/2021/02/06/skwRxVZOKg254Sz.gif)

## 碰撞检测原理

窗口边界碰撞检测的原理很简单，比如 x 坐标小于等于 0，那就说明角色碰到了窗口左边侧。右边边界检测需要注意的是角色坐标 x 加上角色宽度 w 大于等于窗口右边坐标，即表示碰到了右边边界，计算公式即为：```x + w >= win_w```。

角色碰撞检测与边界碰撞检测类似，角色 a 是一个矩形，角色 b 也是一个矩形，两个矩形碰撞会有一个重叠区域，即判断两个矩形是否出现了重叠区域。角色碰撞有可能是 a 碰 b，也可能是 b 碰 a.

![碰撞检测原理.png](https://i.loli.net/2021/02/08/BlXWTjt5hb7iVCv.png)

```python
# a 碰 b
is_x = a.x + a.width <= b.x + b.width and a.x + a.width >= b.x
is_y = a.y + a.height <= b.y + b.height and a.y + a.height >= b.y
is_x and is_y

# b 碰 a
is_x = b.x + b.width  <= a.x + a.width and b.x + b.width >= a.x
is_y = b.y +  b.height <= a.y + a.height and b.y + b.height >= a.y
is_y and is_x
```

## 自制按键原理

按键在界面中是有长宽和位置的，比如现在有一个长和宽都为 100px 的按键图片，并且已经将其加载到了界面中 (0, 0) 的位置，那么我们可以获取鼠标点击时的位置，再比较鼠标点击的位置是否落在图片上即可：

```python
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if 0 <= x <= 100 and 0 <= y <= 100:
            print('点击了按钮')
```