import sys

import pygame.event
from pygame import KEYDOWN, QUIT, display, font, image, init, transform

from command import Command
from configuration import Config
from enemy import Enemy
from log import Log
from path import Path
from player import Player
from sound import Sound


class Game:
    def __init__(self):
        init()
        self.settings = Config()
        self.screen = display.set_mode((Config.screen["width"], Config.screen["height"]))
        font_path = Path.generate_absolute_path(Config.font["path"])
        self.font = font.Font(font_path, Config.font["size"])
        field_path = Path.generate_absolute_path(Config.field["path"])
        self.field_img = transform.scale(image.load(field_path),(Config.screen["width"], Config.screen["height"]))
        background_path = Path.generate_absolute_path(Config.background["path"])
        self.background_img = transform.scale(image.load(background_path), (Config.background["size"]))
        self.log = Log()
        self.command = Command()
        self.player = Player(
            Config.player["status"]["level"],
            Config.player["status"]["name"],
            Config.player["status"]["hp"],
            Config.player["status"]["mp"],
            Config.player["status"]["attack"],
            Config.player["status"]["spell"],
        )

        enemy_name = "slime"
        enemy_path = Path.generate_absolute_path(Config.enemy[enemy_name]["path"])
        self.enemy = Enemy(
            Config.enemy[enemy_name]["status"]["name"],
            Config.enemy[enemy_name]["status"]["hp"],
            Config.enemy[enemy_name]["status"]["mp"],
            Config.enemy[enemy_name]["status"]["attack"],
            Config.enemy[enemy_name]["status"]["spell"],
            transform.scale(image.load(enemy_path), Config.enemy[enemy_name]["size"]),
            Config.enemy[enemy_name]["coordinate"],
        )

    def run_game(self):
        self._update_screen()
        Sound.play_bgm()

        #メインループ
        while True:
            #キーボード、マウスの監視
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.command.check_key_event(event.key, self.player, self.enemy, self.log)
                self._update_screen()

    def _update_screen(self):
        #画面のリセット
        self.screen.fill(Config.screen["bg_color"])
        #画面の描画
        self.screen.blit(self.field_img, Config.field["coordinate"])
        self.screen.blit(self.background_img, Config.background["coordinate"])
        self.command.draw(self.font, self.screen)
        self.log.draw(self.font, self.screen)
        self.enemy.draw(self.screen)
        self.player.draw(self.font, self.screen)
        #更新
        display.flip()

if __name__ == "__main__":
    display.set_caption("Dragon Quest 1")
    game = Game()
    game.run_game()
