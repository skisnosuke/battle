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
        
        #コマンド
        self.command_position = (block*7, 10)
        self.command_length = (block*7, block*3)
        self.command_action_position_upper_left = (block*7+8, 10, block*7, block*2)
        self.command_action_position_upper_right = (block*7+block*5, 10, block*7, block*2)
        self.command_action_position_lower_left = (block*7+8, block)
        self.command_action_position_lower_right = (block*7+block*5, block, block*7, block*2)
        
        #ログ
        self.log_position = (block*3, block*10)
        self.log_length = (block*10, block*5)

        #フィールド
        field_img_temp = pygame.image.load("img/field.png")
        self.field_img = pygame.transform.scale(field_img_temp,
            (self.screen_width, self.screen_height))

        #プレイヤー
        self.player_position = (block*1, block)
        self.player_length = (block*4, block*6)

        #敵 背景
        enemy_bg_img_temp = pygame.image.load("img/background.jpg")
        self.enemy_bg_img = pygame.transform.scale(enemy_bg_img_temp,
            (block*7, block*7))
        self.enemy_bg_img_position = (block*5, block*3)
        #敵 本体
        enemy_img_temp = pygame.image.load("img/slime.png")
        self.enemy_img = pygame.transform.scale(enemy_img_temp, (block*3, block*3))
        self.enemy_position = (block*7, block*6)

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