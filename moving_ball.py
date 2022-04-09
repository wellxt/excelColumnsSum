# -*- coding:utf-8 -*-
'''
制作一个跳跃的小球游戏：
    创建一个游戏窗口，然后在窗口内创建一个小球。以一定的速度移动小球，当小球碰到游戏窗口的边缘时，小球弹回，继续移动。
'''

import sys          # 导入sys模块
import pygame       # 导入pygame模块

pygame.init()                               # 初始化pygame
size = width, height = 640, 480             # 设置窗口
screen = pygame.display.set_mode(size)      # 显示窗口
color =(0,0,0)                              # 设置颜色

ball = pygame.image.load("ball.png")        # 加载图片
ballrect = ball.get_rect()                  # 获取矩形区域

speed = [5,5]                               # 设置移动的X轴、Y轴的距离
clock = pygame.time.Clock()                 # 设置时针

# 执行死循环，确保窗口一直显示
while True:
    clock.tick(60)                          # 每秒执行60次
    # 检查事件
    for event in pygame.event.get():        # 遍历所有事件
        if event.type == pygame.QUIT:       # 如果单击关闭窗口，则退出
            pygame.quit()                   # 退出pygame
            sys.exit()

    ballrect = ballrect.move(speed)         # 移动小球
    # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top <0 or ballrect.right > height:
        speed[1] = -speed[-1]

    screen.fill(color)                      # 填充颜色
    screen.blit(ball, ballrect)             # 将图片画在窗口上
    pygame.display.flip()                   # 更新全部显示
