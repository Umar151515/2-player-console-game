import time
from collections import deque

import pcg

import config
import controls
from gun import Gun_1, Gun_2, Gun_3


console = pcg.WindowConsole(config.width, config.height)
console.allow_console_resizing = True


class Game:
    def __init__(self):
        self.fps = pcg.FPS(30)

        self.guns = deque([
                     Gun_1,
                     Gun_2,
                     Gun_3,
                     ])
        self.guns_1 = self.guns.copy()
        self.guns_2 = self.guns.copy()

        self.start_game = False
        
        self.last_win_player = None

        self.console_rect = console.get_rect()
        
        self.delta = 0
        self.cur_time = time.time_ns()

        self.bonus_time = time.time()

        self.bullet_group = pcg.GroupEssence()
        self.bonus_group = pcg.GroupEssence()

        self.restart_menu()

    def restart_game(self):
        self.player_2 = self.guns_2[0](self, console, 'up')
        self.player_1 = self.guns_1[0](self, console, 'down')
        self.start_game = True
        
        self.bullet_group.groups.clear()
        self.bonus_group.groups.clear()

    def restart_menu(self):
        self.start_game = False

        self.bullet_group.groups.clear()
        self.bonus_group.groups.clear()

    def delta_time(self):
        self.delta = (time.time_ns()-self.cur_time)/1000000000
        self.cur_time = time.time_ns()


game = Game()

while True:
    controls.update(game, console)

    console.update()
    console.fill(' ')

    game.delta_time() 