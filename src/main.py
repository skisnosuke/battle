import sys

import pygame.event
from pygame import KEYDOWN, QUIT, display, font, image, init, transform

from command import Command
from configuration import Config
from enemy import Enemy
from error import NotEnoughMpError
from key import Key
from log import Log
from path import Path
from player import Player
from sound import Sound


class Battle:
    def __init__(self):
        init()
        self.screen = display.set_mode((Config.screen["width"], Config.screen["height"]))
        field_path = Path.generate_absolute_path(Config.field["path"])
        self.field_img = transform.scale(image.load(field_path),(Config.screen["width"], Config.screen["height"]))
        background_path = Path.generate_absolute_path(Config.background["path"])
        self.background_img = transform.scale(image.load(background_path), (Config.background["size"]))
        font_path = Path.generate_absolute_path(Config.font["path"])
        font_initialized = font.Font(font_path, Config.font["size"])
        self.command = Command(self.screen, font_initialized)
        self.player = Player(
            self.screen,
            font_initialized,
            Config.player["status"]["name"],
            Config.player["status"]["level"],
            Config.player["status"]["hp"],
            Config.player["status"]["mp"],
            Config.player["status"]["attack"],
            Config.player["status"]["spells"],
        )
        enemy_name = "slime"
        enemy_path = Path.generate_absolute_path(Config.enemy[enemy_name]["path"])
        self.enemy = Enemy(
            self.screen,
            Config.enemy[enemy_name]["status"]["name"],
            Config.enemy[enemy_name]["status"]["hp"],
            Config.enemy[enemy_name]["status"]["mp"],
            Config.enemy[enemy_name]["status"]["attack"],
            Config.enemy[enemy_name]["status"]["spells"],
            transform.scale(image.load(enemy_path), Config.enemy[enemy_name]["size"]),
            Config.enemy[enemy_name]["coordinate"],
        )
        self.log = Log(self.screen, font_initialized)

    def run(self):
        self.draw()
        Sound.play_bgm()

        while True:
            #入力を監視
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if not Key.is_valid_key(event.key):
                        break
                    Sound.play_cursor()
                    if Key.should_cursor_move(event.key):
                        self.command.move_cursor(event.key)
                        break
                    if Key.should_command_execute(event.key):
                        try:
                            self.command.execute(self.player, self.enemy, self.log)
                        except NotEnoughMpError:
                            self.log.draw("MPがたりない")
                        break
                    if Key.should_go_back(event.key):
                        self.command.go_back()
                        break

    def draw(self):
        #画面のリセット
        self.screen.fill(Config.screen["bg_color"])
        #画面の描画
        self.screen.blit(self.field_img, Config.field["coordinate"])
        self.screen.blit(self.background_img, Config.background["coordinate"])
        self.command.draw()
        self.log.draw(self.enemy.name + "が あらわれた！\nコマンド？")
        self.enemy.draw()
        self.player.draw()
        #更新
        display.flip()

if __name__ == "__main__":
    display.set_caption("Dragon Quest 1")
    battle = Battle()
    battle.run()
