from settings import SCREEN_WIDTH, LEVEL_WIDTH


class Camera:
    def __init__(self):
        self.offset_x = 0

    def update(self, target_rect):
        self.offset_x = target_rect.centerx - SCREEN_WIDTH // 2

        if self.offset_x < 0:
            self.offset_x = 0
        if self.offset_x > LEVEL_WIDTH - SCREEN_WIDTH:
            self.offset_x = LEVEL_WIDTH - SCREEN_WIDTH
        
    def apply(self, rect):
        return rect.move(-self.offset_x, 0)