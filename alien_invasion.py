import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


# some ideas of python program

# for arguments use. if you want to use one variable(change it or just read it),
#                    you need send it to the function as arguments.
#
# therefore,         in one function, only the variable created in this function,
#                    arguments you sent before and library imported before can
#                    be used as right value.
#                    left value is used, only when you want to create a variable
#                    or you want to modify arguments you sent before.
#
# in addition,        some class in python is use like structure in C plus plus like Settings
#                    and only for such class we will use its variable as right value.
#                    other class or library we only use its function as right value.


def run_game():

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    stats = GameStats(ai_settings)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:

            ship.update()                     #only modify variable in the ship, not update screen
            gf.update_bullets(bullets, aliens)        #only modify variable in the bullets and the members of the group
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens)          #show all element modes.


run_game()




