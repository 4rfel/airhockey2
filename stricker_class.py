from object_class import Basic_object

class Stricker(Basic_object):
    def __init__(self, sprite, center, size):
        super().__init__(sprite, center, size)

    def collide(self, disk):
        pass