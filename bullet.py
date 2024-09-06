import math
import random
import time
import pcg


class Bullet(pcg.Essence):
    def __init__(self, game, player, position):
        self.game = game
        self.player = player
        self.position = position

        self.speed_x = 0

        self.speed_y = 150
        self.image = pcg.TextImage('''\/''')
        if position == 'up':
            self.speed_y = -150
            self.image = pcg.TextImage('''/\\''')
        self.rect = self.image.get_rect()

        self.rect.top_center = player.rect.bottom_center[0], player.rect.bottom_center[1]+1
        if position == 'up':
            self.rect.bottom_center = player.rect.top_center[0], player.rect.top_center[1]-1
        super().__init__(self)

    def update(self):
        self.move()

    def move(self):
        self.rect.x_cor += self.game.delta * self.speed_x
        self.rect.y_cor += self.game.delta * self.speed_y / 2


class Bullet_2(Bullet):
    def __init__(self, game, player, position):
        super().__init__(game, player, position)
        
        self.speed_y = 100
        self.image = pcg.TextImage('###\n###')
        if position == 'up':
            self.speed_y = -100
        self.rect = self.image.get_rect()

        self.rect.top_center = player.rect.bottom_center[0], player.rect.bottom_center[1]+1
        if position == 'up':
            self.rect.bottom_center = player.rect.top_center[0], player.rect.top_center[1]-1

            
class Bullet_3(Bullet):
    def __init__(self, game, player, position, mode='l'):
        super().__init__(game, player, position)

        self.mode = mode

        self.speed_x = 200
        
        self.speed_y = 180
        self.image = pcg.TextImage('|/')
        if mode == 'l':
            self.image = pcg.TextImage('\|')
        if position == 'up':
            self.speed_y = -180
            self.image = pcg.TextImage('|\\')
            if mode == 'l':
                self.image = pcg.TextImage('/|')
        self.rect = self.image.get_rect()
        
        self.rect.top_center = player.rect.bottom_center[0], player.rect.bottom_center[1]+1
        if position == 'up':
            self.rect.bottom_center = player.rect.top_center[0], player.rect.top_center[1]-1

    def move(self):
        r = random.randint(-100, 100)
        r = self.rect.x_cor / r if r != 0 else 1
        
        if self.mode == 'l':
            self.rect.x_cor += self.game.delta * self.speed_x * math.cos(r)
        else:
            self.rect.x_cor += self.game.delta * self.speed_x * math.sin(r)

        self.rect.y_cor += self.game.delta * self.speed_y / 2


class Bullet_4(Bullet):
    def __init__(self, game, player, bullet_group, position):
        super().__init__(game, player, position)
        self.bullet_group = bullet_group

        self.start_time_mini_bullet = time.time()
        self.time_mini_bullet = 0.1

        self.image = pcg.TextImage(' /*\\\n#-#-#\n \\*/')
        self.rect = self.image.get_rect()

        self.speed_y = 25
        if position == 'up':
            self.speed_y = -25
        
        self.rect.top_center = player.rect.bottom_center[0], player.rect.bottom_center[1]+1
        if position == 'up':
            self.rect.bottom_center = player.rect.top_center[0], player.rect.top_center[1]-1

    def update(self):
        super().update()

        if time.time() - self.start_time_mini_bullet > self.time_mini_bullet:
            self.bullet_group.add(Bullet_3(self.game, self, self.position, 'l'))
            self.bullet_group.add(Bullet_3(self.game, self, self.position, 'r'))
            self.start_time_mini_bullet = time.time()