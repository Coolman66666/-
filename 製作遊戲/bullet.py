import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        先在 (0, 0) 建立一個子彈的矩形，再設定成正確的位置.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

       # 用浮點數儲存子彈的垂直位置，讓移動更平滑
        self.y = float(self.rect.y)

     
    def update(self):
        """Move the bullet up the screen."""
        # 更新子彈的實際位置（浮點數）
        self.y -= self.settings.bullet_speed
         # 更新矩形位置，讓子彈顯示在畫面上
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)   