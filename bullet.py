import pygame
from pygame.sprite import Sprite

#How to define our own class
#Frist Our Class is an Object, not an Operation.
#In the past, I usually define a class used to do something like draw or read data.
#But now, I need to define a class to represent an object.
#So I need to create its position, sizes, and its color .etc
#And sometimes, I also need to use 'inherit',which is not to be used in the Operation class.


class Bullet(Sprite):   # inherit

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # define self.rect's size.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # define self.rect's X and Y position.
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # why need to create y ?
        self.y = float(self.rect.y)

        # define self.color
        self.color = ai_settings.bullet_color

        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

