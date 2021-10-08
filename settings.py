import pygame
class Settings:
    #設定を格納するクラス
    def __init__(self):
        """画面設定"""
        self.screen_width = 480
        self.screen_height = 480
        self.bg_color = (10, 10, 10)
        self.font_name = "font/DragonQuestFCIntact.ttf"
        block = 30
        
        #コマンド
        self.command_position = (block*7, 10, block*7, block*3)
        
        #ログ
        self.log_position = (block*3, block*10, block*10, block*5)
        
        #プレイヤー
        self.player_position = (block*1, block, block*4, block*6)
# 背景画像

# コマンド
#   x
#   y
#   width
#   height

# ログ
#   x
#   y
#   width
#   height

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