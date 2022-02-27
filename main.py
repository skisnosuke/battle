from pygame.locals import *
import pygame
import sys
import time
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

        #bgmのロード
        pygame.mixer.music.load(self.settings.bgm)

        #効果音のロード
        self.attack_sound = pygame.mixer.Sound(self.settings.attack_sound)
        self.attacked_sound = pygame.mixer.Sound(self.settings.attacked_sound)
        self.spell_sound = pygame.mixer.Sound(self.settings.spell_sound)
        self.cursor_sound = pygame.mixer.Sound(self.settings.cursor_sound)
        self.end_sound = pygame.mixer.Sound(self.settings.end_sound)
        self.escape_sound = pygame.mixer.Sound(self.settings.escape_sound)

    def run_game(self):
        self.log = Log()
        self.command = Command()
        self.player = Player()
        self.enemy = Enemy()
        
        self._update_screen()
        pygame.mixer.music.play(-1)
        #メインループ
        while True:
            #キーボード、マウスの監視
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_key_event(event)

    def _check_key_event(self, event):
        if event.key == pygame.K_UP:
            self.command.action_selected = (
                (self.command.action_selected - 2) % 4 )
            self.cursor_sound.play()
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self.command.action_selected = (
                self.command.action_selected + 1 if
                self.command.action_selected % 2 == 0 else
                self.command.action_selected - 1 )
            self.cursor_sound.play()
        elif event.key == pygame.K_DOWN:
                self.command.action_selected = (
                    (self.command.action_selected + 2) % 4 )
                self.cursor_sound.play()
        elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
            self.cursor_sound.play()
            self.log.change_action_idx(self.command.action_selected)
            time.sleep(0.5)
            self._update_screen()
            self._effect_of_attack(self.command.action_selected)
            self._effect_of_spell(self.command.action_selected)
            self._effect_of_escape(self.command.action_selected)
        self._update_screen()

    def _effect_of_attack(self, act):
        if act == 0:
            self.command.act(self.player, self.enemy)
            self.attack_sound.play()
            time.sleep(1)
            self.attacked_sound.play()

    def _effect_of_spell(self, act):
        if act == 1:
            self.canCastSpell = self.command.cast(self.player, self.enemy)
            if self.canCastSpell == True:
                self.spell_sound.play()
                time.sleep(1.5)
                self.attacked_sound.play()

    def _effect_of_escape(self, act):
        if act == 2:
            self.escape_sound.play()


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
