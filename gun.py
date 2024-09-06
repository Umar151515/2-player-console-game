import keyboard
import time
import pcg

from bullet import Bullet, Bullet_2, Bullet_3, Bullet_4


class Gun_1(pcg.Essence):
    up_image = '/\\\n||'
    down_image = '||\n\/'

    def __init__(self, game, console, position):
        self.position = position
        self.console = console
        self.game = game

        self.image = pcg.TextImage(self.down_image)
        if self.position == 'up':
            self.image = pcg.TextImage(self.up_image)
        self.rect = self.image.get_rect()
        self.health_rect = pcg.Rect(0, 0, size_x=2, size_y=1)
        self.console_rect = console.get_rect()

        self.start_time_bullet = time.time()
        self.time_bullet = 0.5
        self.start_time_fire = time.time()
        self.time_fire = 0.1

        self.health = 3
        self.damage = 1

        self.rect.top_left = console.size_x / 2, console.size_y / 2 - console.size_y / 4
        if position == 'up':
            self.rect.top_left = console.size_x / 2, console.size_y / 2 + console.size_y / 4

        self.cartridges = 0
        self.max_cartridges = 15

        self.speed = 125

        super().__init__(self)

    def draw(self):
        pcg.draw.blit(self.console, self.image, self.rect)
        pcg.draw.blit(self.console, pcg.TextImage(str(self.health)), self.health_rect)
        pcg.draw.blit(self.console, pcg.TextImage(str(self.cartridges)), (self.rect.x_cor+3, self.rect.y_cor))

        self.health_rect.bottom = self.rect.y_cor - 2
        self.health_rect.x_center = self.rect.x_center
        if self.position == 'up':
            self.health_rect.y_cor = self.rect.bottom + 2


    def up(self):
        self.rect.y_cor -= self.speed * self.game.delta / 2

    def down(self):
        self.rect.y_cor += self.speed * self.game.delta / 2

    def right(self):
        self.rect.x_cor += self.speed * self.game.delta

    def left(self):
        self.rect.x_cor -= self.speed * self.game.delta

    def fire(self):
        self.cartridges -= 1
        self.start_time_bullet = time.time()
        self.start_time_fire = time.time()
        self.game.bullet_group.add(Bullet(self.game, self, self.position))

    def move(self):
        if self.position == 'up':
            if keyboard.is_pressed('d'):
                self.right()
            elif keyboard.is_pressed('a'):
                self.left()
            if keyboard.is_pressed('w'):
                self.up()
            elif keyboard.is_pressed('s'):
                self.down()
            if keyboard.is_pressed('f') and time.time() - self.start_time_fire > self.time_fire and self.cartridges > 0:
                self.fire()
        else:
            if keyboard.is_pressed('right'):
                self.right()
            elif keyboard.is_pressed('left'):
                self.left()
            if keyboard.is_pressed('down'):
                self.down()
            elif keyboard.is_pressed('up'):
                self.up()
            if keyboard.is_pressed('l') and time.time() - self.start_time_fire > self.time_fire and self.cartridges > 0:
                self.fire()

    def collision(self):
        if time.time() - self.start_time_bullet > self.time_bullet and self.cartridges < self.max_cartridges:
            self.cartridges += 1
            self.start_time_bullet = time.time()

        if self.rect.right > self.console_rect.right:
            self.rect.right = self.console_rect.right
        elif self.rect.x_cor < 0:
            self.rect.x_cor = 0
        if self.rect.bottom > self.console_rect.bottom-1:
            self.rect.bottom = self.console_rect.bottom-1
        elif self.rect.y_cor < 0:
            self.rect.y_cor = 0

        if self.position == 'up':
            if self.rect.y_cor < (self.console_rect.size_y + 2) // 2:
                self.rect.y_cor = (self.console_rect.size_y + 2) // 2
        else:
            if self.rect.bottom > (self.console_rect.size_y - 1) // 2:
                self.rect.bottom = (self.console_rect.size_y - 1) // 2

    def update(self):
        self.draw()
        self.move()
        self.collision()

        self.console_rect = self.console.get_rect()

    def active_bonus(self):
        self.cartridges += 25


class Gun_2(Gun_1):
    up_image = '##\n||'
    down_image = '||\n##'

    def __init__(self, game, console, position):
        super().__init__(game, console, position)

        self.image = pcg.TextImage(self.down_image)
        if self.position == 'up':
            self.image = pcg.TextImage(self.up_image)
        self.health_rect = pcg.Rect(0, 0, size_x=2, size_y=1)

        self.start_time_bullet = time.time()
        self.time_bullet = 1
        self.start_time_fire = time.time()
        self.time_fire = 0.4

        self.bonus = False

        self.health = 5
        self.damage = 2

        self.max_cartridges = 5

        self.speed = 75

    def fire(self):
        self.cartridges -= 1
        self.start_time_bullet = time.time()
        self.start_time_fire = time.time()
        if self.bonus:
            self.game.bullet_group.add(Bullet_4(self.game, self, self.game.bullet_group, self.position))
            self.bonus = False
        else:
            self.game.bullet_group.add(Bullet_2(self.game, self, self.position))

    def active_bonus(self):
        self.bonus = True

class Gun_3(Gun_1):
    up_image = '\/\n||'
    down_image = '||\n/\\'

    def __init__(self, game, console, position):
        super().__init__(game, console, position)

        self.image = pcg.TextImage(self.down_image)
        if self.position == 'up':
            self.image = pcg.TextImage(self.up_image)
        self.health_rect = pcg.Rect(0, 0, size_x=2, size_y=1)

        self.start_time_bullet = time.time()
        self.time_bullet = 0.3
        self.start_time_fire = time.time()
        self.time_fire = 0.15

        self.start_time_bonus = time.time()
        self.time_bonus = 5
        self.bonus = False

        self.health = 2
        self.damage = 1

        self.max_cartridges = 25

        self.speed = 170

    def fire(self):
        self.cartridges -= 1
        self.start_time_bullet = time.time()
        self.start_time_fire = time.time()
        self.game.bullet_group.add(Bullet_3(self.game, self, self.position, 'l'))
        self.game.bullet_group.add(Bullet_3(self.game, self, self.position, 'r'))
        if self.bonus:
            self.game.bullet_group.add(Bullet_3(self.game, self, self.position, 'l'))
            self.game.bullet_group.add(Bullet_3(self.game, self, self.position, 'r'))
            self.cartridges += 1
        if time.time() - self.start_time_bonus > self.time_bonus:
            self.bonus = False
            
    def active_bonus(self):
        self.start_time_bonus = time.time()
        self.bonus = True