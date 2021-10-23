from pygame.locals import *
import pygame
import sys
from settings import Settings
from player import Player
from enemy import Enemy
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
        self.enemy = Enemy()
        
        self._update_screen()
        #メインループ
        while True:
            #キーボード、マウスの監視
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_key(event)


    def _check_key_event(self, event):
        if event.key == pygame.K_UP:
            self.command.action_selected = (
                (self.command.action_selected - 2) % 4 )
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self.command.action_selected = (
                self.command.action_selected + 1 if
                self.command.action_selected % 2 == 0 else
                self.command.action_selected - 1 )
        elif event.key == pygame.K_DOWN:
                self.command.action_selected = (
                    (self.command.action_selected + 2) % 4 )
        elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
            self.log.action_idx = self.command.action_selected
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
