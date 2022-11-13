from character import Character


class Enemy(Character):
    def __init__(self, name, hp, mp, attack, spells, img, coordinate):
        super().__init__(name, hp, mp, attack, spells)
        self.coordinate = coordinate
        self.img = img

    def draw(self, screen):
        screen.blit(self.img, self.coordinate)
