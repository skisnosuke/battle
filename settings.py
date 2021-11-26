import pygame
class Settings:
    #設定を格納するクラス
    def __init__(self):
        """画面設定"""
        self.screen_width = 480
        self.screen_height = 480
        self.bg_color = (10, 10, 10)
        self.font = pygame.font.Font("font/DragonQuestFC.ttf", 32)
        block = 30
        
        #サウンド
        self.bgm = "sound/bgm.mp3"
        self.attack_sound = "sound/attack.wav"
        self.attacked_sound = "sound/attacked.wav"
        self.incantation_sound = "sound/incantation.wav"
        self.cursor_sound = "sound/cursor.wav"
        self.end_sound = "sound/end.wav"

        #コマンド
        self.command_position = (block*7, 10)
        self.command_length = (block*7, block*3)
        self.command_action_position_upper_left = (block*8, 10)
        self.command_action_position_upper_right = (block*7+block*4, 10)
        self.command_action_position_lower_left = (block*8, 20+block)
        self.command_action_position_lower_right = (block*7+block*4, 20+block)
        
        #ログ
        self.log_position = (block*3, block*10)
        self.log_length = (block*10, block*5)

        #エネミー
        self.enemy_img = pygame.image.load("img/example.png")
        self.enemy_position = (block*5+10, block*5)
        self.enemy_hp = 100
        
        #フィールド
        field_img_temp = pygame.image.load("img/field.png")
        self.field_img = pygame.transform.scale(field_img_temp,
            (self.screen_width, self.screen_height))

        #プレイヤー
        self.player_position = (block, 10)
        self.player_length = (block*4, block*6)
        self.player_status_attack = 5
        self.player_status_hp = 10
        self.player_status_mp = 0
        self.player_status_lv = 1
        self.player_status_name = "ゆうしゃ"


        #敵 背景
        enemy_bg_img_temp = pygame.image.load("img/background.jpg")
        self.enemy_bg_img = pygame.transform.scale(enemy_bg_img_temp,
            (block*7, block*7))
        self.enemy_bg_img_position = (block*5, block*3)
        #敵 本体
        enemy_img_temp = pygame.image.load("img/slime.png")
        self.enemy_img = pygame.transform.scale(enemy_img_temp, (block*3, block*3))
        self.enemy_position = (block*7, block*6)
        self.enemy_status_attack = 10
        self.enemy_status_hp = 4
        self.enemy_status_name = "スライム"

# 敵
#   敵画像
#   HP
#   攻撃力
#   行動

# 主人公
#   名前
#   HP
#   MP
#   攻撃力