from object_class import Basic_object
from random import randint
from math import radians, cos, sin, atan, pi

class Disk(Basic_object):
    def __init__(self, sprite, center, size, min_speed, max_speed, table_width, table_height):
        super().__init__(sprite, center, size)
        self.table_width  = table_width
        self.table_height = table_height

        deg = randint(0,360)
        rad = radians(deg)
        speed = randint(min_speed, max_speed)
        self.x_speed = int(cos(rad)*speed)
        self.y_speed = int(sin(rad)*speed)

    def move(self):
        if self.rect.left > 0 and self.rect.right < self.table_width:
            self.rect.centerx += self.x_speed
        else:
            self.x_speed = -self.x_speed
            self.rect.centerx += self.x_speed

        if self.rect.top > 0 and self.rect.bottom < self.table_height:
            self.rect.centery += self.y_speed
        else:
            self.y_speed = -self.y_speed
            self.rect.centery += self.y_speed

    def collide(self):
        speed = (self.x_speed**2 + self.y_speed**2)**0.5
        if self.x_speed != 0:
            rad = atan(self.y_speed/self.x_speed)
        elif self.y_speed > 0:
            rad = 3*pi/2
        else:
            rad = pi/2

    def get_top(self):
        return self.rect.top

    def get_bottom(self):
        return self.rect.bottom
        