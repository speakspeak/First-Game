import pygame


class Ship:
    def __init__(self, ai_settings, screen):

        self.ai_settings = ai_settings

        self.screen = screen

        self.image = pygame.image.load("images/ship.bmp")

        self.rect = self.image.get_rect()                      # create rect
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx           # modify or create ?
        self.rect.bottom = self.screen_rect.bottom             # unknown.
                                                               # but after this, we know it has existed.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx



