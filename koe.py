class Cow:

    def __init__(self, weight):
        self.weight = weight


class Feed:

    def __init__(self, koe):
        if koe.weight == 450:
            self.energy = 26500
            self.protein = 215
        elif koe.weight == 575:
            self.energy = 31500
            self.protein = 255
        elif koe.weight == 500:
            self.energy = 29500
            self.protein = 245
        elif koe.weight == 600:
            self.energy = 37000
            self.protein = 305
    