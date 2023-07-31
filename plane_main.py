import plane_sprites
import pygame


class PlaneGame(object):
    """ 主游戏类 """

    def __init__(self):
        print("游戏正在初始化...")
        # 创建游戏主窗口
        self.screen = pygame.display.set_mode(plane_sprites.SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，创建精灵和精灵组
        self.__create_sprites__()
        # 设置定时器事件-每隔1秒创建敌机
        pygame.time.set_timer(plane_sprites.CREATE_ENEMY_EVENT, 1000)
        # 设置定时器事件-每隔0.5秒发射子弹
        pygame.time.set_timer(plane_sprites.HERO_FIRE_EVENT, 500)

    def __create_sprites__(self):
        """ 用于创建精灵和精灵组 """
        background1 = plane_sprites.BackGround()
        background2 = plane_sprites.BackGround(is_alt=True)
        self.background_group = pygame.sprite.Group(background1, background2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄飞机
        self.hero_plane = plane_sprites.Hero()
        # 创建英雄飞机精灵组
        self.hero_group = pygame.sprite.Group(self.hero_plane)

    def start_game(self):
        """ 启动游戏 """
        while True:
            self.clock.tick(120)
            # 事件监听
            self.__event_handler__()
            # 碰撞检测
            self.__check_collide__()
            # 位置更新
            self.__update_sprites__()
            # 游戏主窗口刷新显示
            pygame.display.update()

    def __check_collide__(self):
        """ 碰撞检测 """
        # 子弹与敌机之间的碰撞检测
        pygame.sprite.groupcollide(self.enemy_group, self.hero_plane.bullet_group, True, True)
        # 英雄飞机与敌机之间的碰撞检测
        enemy_list = pygame.sprite.spritecollide(self.hero_plane, self.enemy_group, True)
        if len(enemy_list) > 0:
            self.hero_plane.kill()
            self.__game_over__()

    def __event_handler__(self):
        """ 事件监听 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over__()
            elif event.type == plane_sprites.CREATE_ENEMY_EVENT:
                self.enemy_group.add(plane_sprites.Enemy())
            elif event.type == plane_sprites.HERO_FIRE_EVENT:
                self.hero_plane.fire()

        """ 按键判断 """
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.hero_plane.speed = -2
        elif keys_pressed[pygame.K_RIGHT]:
            self.hero_plane.speed = 2
        else:
            self.hero_plane.speed = 0

    def __update_sprites__(self):
        """
        位置更新
        精灵组更新所有精灵动作
        精灵组重新绘制图形
        """
        self.background_group.update()
        self.background_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero_plane.bullet_group.update()
        self.hero_plane.bullet_group.draw(self.screen)

    # 定义为一个静态方法，无法访问实例参数方法，但是可以通过类名直接调用
    @staticmethod
    def __game_over__():
        # 结束游戏
        print("游戏结束...")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 初始化pygame
    pygame.init()
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
