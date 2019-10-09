from stricker import Stricker

class CPU_stricker(Stricker):
    def __init__(self, sprite, center, size, speed, threshold):
        super().__init__(sprite, center, size)
        self.speed = speed
        self.threshold = threshold
        self.collided = False
        self.y_initial = center[1]

    def move(self, prediction_point, disk):
        center = disk.get_center()

        # align stricker with where we think the disk will intercept a arbritary line
        if self.rect.centerx > prediction_point[0] + self.threshold:
            self.rect.centerx += self.speed
        elif self.rect.centerx < prediction_point[0] - self.threshold:
            self.rect.centerx -= self.speed

        elif 0 <= self.rect.top - center[1] <= 30: # check if the disk is less than 30px of the top of the stricker.
            if not self.collided:                  # check if the stricker already collided with the disk and
                self.rect.centery -= self.speed    # if not collided yet accelerate in y.

        if self.collided:                          # check if the stricker already collided with the disk
            self.reset_y()                         # reset the vertical position to its original value

    def reset_y(self):
        if self.y_initial - self.rect.top > 0:     # check if the stricker is its vertical original position
            self.rect.top += self.speed            # try to reset vertical position 
        elif self.y_initial - self.rect.top < 0:   # check if the stricker is its vertical original position
            self.rect.top -= self.speed            # try to reset vertical position