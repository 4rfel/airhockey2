from object_class import Basic_object

class Table(Basic_object):
    def __init__(self, sprite, center, size, goal1, goal2):
        super().__init__(sprite, center, size)
        self.goal1 = goal1
        self.goal2 = goal2
        self.player_points = 0
        self.CPU_points = 0

    def score(self, disk):
        pass