import time
import random

import keyboard
import pcg

from bonus import Bonus


def collision(game, console):
    if game.start_game:
        if pcg.collision.collision_essence_group(game.player_1, game.bullet_group, True):
            game.player_1.health -= game.player_2.damage
        if pcg.collision.collision_essence_group(game.player_2, game.bullet_group, True):
            game.player_2.health -= game.player_1.damage
        if pcg.collision.collision_essence_group(game.player_1, game.bonus_group, True):
            game.player_1.active_bonus()
        if pcg.collision.collision_essence_group(game.player_2, game.bonus_group, True):
            game.player_2.active_bonus()
    for bullet in game.bullet_group.get_list():
        if bullet.rect.right < 0 or bullet.rect.x_cor > console.size_x or\
            bullet.rect.bottom < 0 or bullet.rect.y_cor > console.size_y:
            game.bullet_group.remove(bullet)
    for bonus in game.bonus_group.get_list():
        if time.time() - bonus.start_time > 5:
            game.bonus_group.remove(bonus)

def controls_menu(game, console):
    if keyboard.is_pressed('w'):
        game.guns_2.rotate(-1)
        time.sleep(0.2)
    elif keyboard.is_pressed('s'):
        game.guns_2.rotate(1)
        time.sleep(0.2)

    if keyboard.is_pressed('up'):
        game.guns_1.rotate(-1)
        time.sleep(0.2)
    elif keyboard.is_pressed('down'):
        game.guns_1.rotate(1)
        time.sleep(0.2)

    if keyboard.is_pressed('enter'):
        game.restart_game()

def blit(game, console):
    game.bullet_group.blit(console)
    game.bonus_group.blit(console)

    if game.start_game:
        pcg.draw.blit(console, pcg.TextImage(str(int(game.fps.get_fps()))), (0, 0))

        pcg.draw.blit(console, pcg.TextImage('='*console.size_x), (0, console.size_y // 2))
    else:
        pcg.draw.blit(console, pcg.TextImage('Нажмите entr чтобы начать игру'), (0, 0))
        pcg.draw.blit(console, pcg.TextImage(game.guns_1[0].down_image), (console.size_x/2, (console.size_y/2) - (console.size_y/4)))
        pcg.draw.blit(console, pcg.TextImage(game.guns_2[0].up_image), (console.size_x/2, (console.size_y/2) + (console.size_y/4)))
        if not game.last_win_player is None:
            pcg.draw.blit(console, pcg.TextImage('Побидитель прошлой битвы'), (0, 2))
            pcg.draw.blit(console, pcg.TextImage(str(game.last_win_player)), (0, 3))

def update(game, console):
    blit(game, console)

    if game.start_game:
        if time.time() - game.bonus_time > 5:
            game.bonus_time = time.time()
            game.bonus_group.add(Bonus(random.randint(0, console.size_x), random.randint(0, console.size_y)))

        if game.player_1.health <= 0:
            game.last_win_player = 'player 2'
            game.restart_menu()
        elif game.player_2.health <= 0:
            game.last_win_player = 'player 1'
            game.restart_menu()

        collision(game, console)

        game.player_1.update()
        game.player_2.update()
        game.bullet_group.update()
    else:
        controls_menu(game, console)