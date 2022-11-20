from pygame import display

from character import Character


class Enemy(Character):
    def __init__(self, screen, name, hp, mp, attack, spells, img, coordinate):
        super().__init__(name, hp, mp, attack, spells)
        self.screen = screen
        self.coordinate = coordinate
        self.img = img

    def draw(self):
        self.screen.blit(self.img, self.coordinate)
        display.flip()
