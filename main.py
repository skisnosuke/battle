from pygame.locals import *
import pygame
import sys
from settings import Settings
from player import Player
#from enemy import Enemy
from log import Log
from command import Command

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
        self.command = Command()
        self.player = Player()
        

        #メインループ
        while True:
          #キーボード、マウスの監視
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()

          #画面のリセット
          self.screen.fill(self.settings.bg_color)

          #最新の画面の表示
          #資格の表示
          self.command.draw(self.screen)
          self.log.draw(self.screen)
          self.player.draw(self.screen)
          self.log.display(self.screen)

          pygame.display.flip()

if __name__ == "__main__":
    #ゲームのインスタンスを生成、その後実行する
    battle = Battle()
    battle.run_game()
