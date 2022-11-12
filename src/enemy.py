from character import Character


class Enemy(Character):
    def __init__(self, name, hp, mp, attack, spell, img, coordinate):
        super().__init__(name, hp, mp, attack, spell)
        self.coordinate = coordinate
        self.img = img

    def draw(self, screen):
        screen.blit(self.img, self.coordinate)
