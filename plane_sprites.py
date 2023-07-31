import pygame
import random

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建发射子弹的定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprite):
    def __init__(self, is_alt=False):
        # 调用父类方法创建精灵对象
        super().__init__("images/background.png")
        # 判断是否为背景图片2，若是则改变初始坐标位置
        if is_alt:
            self.rect.y = -SCREEN_RECT.height

    def update(self):
        # 调用父类方法一起向下移动
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):
    """ 敌机精灵类，继承自GameSprite """
    def __init__(self):
        # 随机抽取敌机
        number = random.randint(1, 3)
        if number == 1:
            # 调用父类方法创建精灵对象
            super().__init__("images/enemy1.png")
            # 随机抽取出场位置
        elif number == 2:
            super().__init__("images/enemy2.png")
        elif number == 3:
            super().__init__("images/enemy3_n1.png")

        # 随机抽取出场位置
        self.rect.x = random.randrange(0, (SCREEN_RECT.width - self.rect.width), self.rect.width)
        # 随机抽取出场速度
        self.speed = random.randint(1, 3)
        # 初始位置应该在游戏主窗口的上方
        self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法一起向下移动
        super().update()
        # 判断是否飞出屏幕外，是则移出精灵组释放内存
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    def __init__(self):
        super().__init__("images/me1.png", speed=0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height - 10
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width
        else:
            self.rect.x += self.speed

    def fire(self):
        """ 英雄飞机发射子弹 """
        for i in (0, 1, 2):
            bullet = Bullet()
            # 设定子弹精灵的位置，应该与英雄飞机的正上方中央发射
            bullet.rect.y = self.rect.y - 2 * i * bullet.rect.height
            bullet.rect.centerx = self.rect.centerx
            # 子弹精灵加入精灵组
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        # 调用父类方法创建背景
        super().__init__("images/bullet1.png", speed=-2)

    def update(self):
        # 调用父类方法进行移动
        super().update()
        if self.rect.bottom <= 0:
            self.kill()



