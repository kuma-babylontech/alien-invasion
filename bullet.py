import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """宇宙船から発射される弾を管理するクラス"""

    def __init__(self, ai_game):
        """宇宙船の現在位置から弾のオブジェクトを作成する"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # (0, 0)の位置に弾の矩形を作成し、正しい位置を設定する
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 弾の位置を浮動小数点数で格納する
        self.y = float(self.rect.y)

    def update(self):
        """画面上に弾を移動する"""
        # 弾の位置を更新する
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """画面上に弾を描画する"""
        pygame.draw.rect(self.screen, self.color, self.rect)
