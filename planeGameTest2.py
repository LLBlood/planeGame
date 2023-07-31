import plane_sprites
import pygame

pygame.init()
window = pygame.display.set_mode((480, 700))
background = pygame.image.load("images/background.png")

""" 创建敌机精灵和精灵组 """
enemy_plane1 = plane_sprites.GameSprite("images/enemy1.png", speed=3)
enemy_plane2 = plane_sprites.GameSprite("images/enemy2.png", speed=3)
enemy_plane3 = plane_sprites.GameSprite("images/enemy3_n1.png")
enemy_group = pygame.sprite.Group(enemy_plane1, enemy_plane2, enemy_plane3)

clock = pygame.time.Clock()
while True:
    window.blit(background, (0,0))
    enemy_group.draw(window)
    enemy_group.update()
    pygame.display.update()
    """ 设置帧率 """
    clock.tick(144)

    """ 此处必须对事件数据做处理，否则系统会直接崩溃 """
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            """ 直接退出游戏 """
            exit()
