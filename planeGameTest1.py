import pygame

pygame.init()

""" 窗口大小（400，700） """
window = pygame.display.set_mode((480, 700))
""" 加载图片到内存 """
background = pygame.image.load("images/background.png")
me1 = pygame.image.load("images/me1.png")
me2 = pygame.image.load("images/me2.png")

""" 设定一个时钟 """
clock = pygame.time.Clock()

while True:
    """ 在游戏主窗口显示图片 """
    window.blit(background, (0, 0))
    window.blit(me2, (189, 574))
    """ 刷新显示 """
    pygame.display.update()
    clock.tick(60)

    """ 在游戏主窗口显示图片 """
    window.blit(background, (0, 0))
    window.blit(me1, (189, 574))
    """ 刷新显示 """
    pygame.display.update()
    clock.tick(60)

    """ 此处必须对事件数据做处理，否则系统会直接崩溃 """
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            """ 直接退出游戏 """
            exit()