import time

import pcg


class Bonus(pcg.Essence):
    def __init__(self, x, y):
        self.image = pcg.TextImage('++\n++')
        self.rect = self.image.get_rect()

        self.rect.top_left = x, y

        self.start_time = time.time()
        
        super().__init__(self)