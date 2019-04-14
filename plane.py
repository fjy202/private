# coding:utf-8
import sys

import pygame
from pygame.locals import *

# 初始化pygame环境
pygame.init()

# 创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255, 255, 255))

# 设置窗口标题
pygame.display.set_caption("飞机大战")

# 加载图片
enemy = pygame.image.load("images/enemy1.png")
enemy2 = pygame.image.load("images/enemy2.png")
enemy3 = pygame.image.load("images/enemy3.png")
h = pygame.image.load("images/hero1.png")
bg = pygame.image.load("images/bg1.png")
bg2 = pygame.image.load("images/bg2.png")
bg3 = pygame.image.load("images/bg3.png")
bg4 = pygame.image.load("images/bg4.png")


def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

y=0
while True:
    # 下方写你的代码
    canvas.blit(bg,(0,0))
    #e1=canvas.blit(enemy,(200,200))
    #e2=canvas.blit(enemy,(250,250))
    e3=canvas.blit(enemy,(300,y))
    #e4=canvas.blit(enemy,(350,250))
    #e5=canvas.blit(enemy,(400,200))
    pygame.display.update()
    y+=1
    if y>650:
        y=0
    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()
