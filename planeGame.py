import pygame
import time

pygame.init()

""" 窗口大小（400，700） """
window = pygame.display.set_mode((480, 700))
""" 加载图片到内存 """
background = pygame.image.load("images/background.png")
me1 = pygame.image.load("images/me1.png")
me2 = pygame.image.load("images/me2.png")

""" 创建一个矩形区域对象，设置初始位置 """
hero_plane = pygame.Rect(189, 574, 102, 126)

""" 设定一个时钟 """
clock = pygame.time.Clock()

run = True
while run:
    """ 在游戏主窗口显示图片 """
    window.blit(background, (0, 0))
    window.blit(me1, hero_plane)
    """ 刷新显示 """
    pygame.display.update()
    hero_plane.y -= 50
    clock.tick(1)

    """ 此处必须对事件数据做处理，否则系统会直接崩溃 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



# """ 刷新显示 """
# pygame.display.update()
# """ 系统休眠5秒 """
# time.sleep(5)

pygame.quit()
