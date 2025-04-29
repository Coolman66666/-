class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
         # 螢幕設定
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

         # 飛船設定
        self.ship_speed = 10
       # 子彈設定
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 100