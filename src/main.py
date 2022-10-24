import pygame
from pygame.locals import *
import sys
from settings import Settings
from player import Player
from enemy import Enemy
from log import Log
from command import Command
from sound import Sound

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
        self.enemy = Enemy()
        self.is_turn_end = False
        
        self._update_screen()
        Sound.play_bgm()

        #メインループ
        while True:
            #キーボード、マウスの監視
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.is_turn_end = self.command.check_key_event(event, self.player, self.enemy, self.log)
                    print(self.is_turn_end)
                    if self.is_turn_end == True:
                        print("スライムのターン")
                        if self.enemy.hp <= 0:
                            print("スライムは倒れた")
                self._update_screen()

    def _update_screen(self):
        #画面のリセット
        self.screen.fill(self.settings.bg_color)

        #最新の画面の表示
        #背景の表示
        self.screen.blit(self.settings.field_img, (0,0))
        self.enemy.draw(self.screen)
        #矩形の表示
        self.command.draw(self.screen)
        self.log.draw(self.screen)
        self.player.draw(self.screen)
        #テキストの表示
        self.log.draw(self.screen)
        #更新
        pygame.display.flip()

if __name__ == "__main__":
    #ゲームのインスタンスを生成、その後実行する
    battle = Battle()
    battle.run_game()
