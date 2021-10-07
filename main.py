from pygame.locals import *
import pygame
import sys
from settings import Settings
#from player import Player
#from enemy import Enemy
from log import Log

class Battle:
    #ゲームのアセットと動作を管理する全体的なクラス
    def __init__(self):
        #ゲームを初期化し、リソースを作成する
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("ドラクエ風戦闘ゲーム")

    def run_game(self):
        self.log = Log()
        


        #メインループ
        while True:
          #キーボード、マウスの監視
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()

          #画面のリセット
          self.screen.fill(self.settings.bg_color)

          #最新の画面の表示
          self.log.display(self.screen)
          pygame.draw.rect(self.screen, (255, 255, 255), Rect(self.settings.command_position), 10)
          pygame.draw.rect(self.screen, (0,0,0), Rect(self.settings.command_position) )
          pygame.draw.rect(self.screen, (255, 255, 255), Rect(self.settings.log_position), 10)
          pygame.draw.rect(self.screen, (0,0,0), Rect(self.settings.log_position) )
          pygame.draw.rect(self.screen, (255, 255, 255), Rect(self.settings.player_position), 10)
          pygame.draw.rect(self.screen, (0,0,0), Rect(self.settings.player_position) )

          pygame.display.flip()

if __name__ == "__main__":
    #ゲームのインスタンスを生成、その後実行する
    battle = Battle()
    battle.run_game()
