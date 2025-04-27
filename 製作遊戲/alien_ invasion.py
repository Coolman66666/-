import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and creat game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen= pygame.display.set_mode((1200,800))
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # 設定背景顏色
        self.bg_color = (230,230,230)
        
    def run_game(self):

            """Start the main loop for the game"""
    
            while True:
               
                self._check_events()
                self.ship.update()
                self._update_bullets()               
                self._update_screen()
                self.clock.tick(60)
                
                #監測鍵盤和滑鼠事件
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
              sys.exit()
             elif event.type == pygame.KEYDOWN:
              self._check_keydown_events(event)
             elif event.type == pygame.KEYUP:
              self._check_keyup_events(event)
    def _check_keydown_events(self,event):
             """Respond to keypresses."""
             if event.key == pygame.K_RIGHT:
                 self.ship.moving_right = True
             elif event.key == pygame.K_LEFT:
                 self.ship.moving_left = True
             elif event.key == pygame.K_q:
                 sys.exit()
             elif event.key == pygame.K_SPACE:
                 self._fire_bullet()
             
    def _check_keyup_events(self,event):
              """Respond to key releases."""
              if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
              elif event.key == pygame.K_LEFT:
                  self.ship.moving_left =  False
              #讓飛船往右移動

    def _fire_bullet(self):
               """Creat a  new bullet and add it to the bullets group."""
               if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
                #在每次迴圈中重繪螢幕
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
                               
        self.bullets.update()
                # 消除已經消失在螢幕之外的子彈
        for bullet in self.bullets.copy():
         if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print(len(self.bullets))
    def _update_screen(self):
        """Update images on the screen , and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
             bullet.draw_bullet()
        self.ship.blitme()
        #顯示最近繪製的螢幕內容
        pygame.display.flip()
        self.clock.tick(60)
    
                        
                 
                 
if __name__=='__main__':
    #創建一個遊戲實例並運行遊戲
    ai = AlienInvasion()
    ai.run_game()

    
    
