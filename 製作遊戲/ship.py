import pygame 

class Ship:
    """A calss to manage the ship """
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() 

        #載入飛船圖片
        self.image = pygame.image.load('製作遊戲/images/ship.bmp')
        self.rect = self.image.get_rect() 
        # 將飛船放在螢幕底部
        self.rect.midbottom = self.screen_rect.midbottom 
        #儲存飛船橫向位置的小數值
        self.x = float(self.rect.x)
        #移動旗標；剛開始時飛船不移動
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """Update the ship's position based on the movement flag."""
        #更新飛船的x值，而不是直接更新rect
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.rect.x += 1
        if self.moving_left and self.rect.left>0:       
                self.x -= self.settings.ship_speed
                self.rect.x -=1
        #根據self.x更新rect位置
        self.rect.x = self.x
    
        

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)
