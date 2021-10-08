import pygame
class Settings:
    #設定を格納するクラス
    def __init__(self):
        """画面設定"""
        self.screen_width = 480
        self.screen_height = 480
        self.bg_color = (10, 10, 10)
        self.font = pygame.font.Font("font/DragonQuestFCIntact.ttf", 20)
        block = 30
        
        #コマンド
        self.command_position = (block*7, 10, block*7, block*3)
        
        #ログ
        self.log_position = (block*3, block*10, block*10, block*5)

        #フィールド
        field_img_temp = pygame.image.load("img/field.png")
        self.field_img = pygame.transform.scale(field_img_temp,
            (self.screen_width, self.screen_height))
        

        #プレイヤー
        self.player_position = (block*1, block, block*4, block*6)

        #敵 背景
        bg_img_temp = pygame.image.load("img/field.png")
        self.bg_img = pygame.transform.scale(bg_img_temp,
            (self.screen_width, self.screen_height))
        #敵 本体
        enemy_img_temp = pygame.image.load("img/example.png")
        self.enemy_img = pygame.transform.scale(enemy_img_temp, (400, 300))
        self.enemy_position = (block*5+10, block*5)

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