from object_class import Basic_object

class Table(Basic_object):
    def __init__(self, sprite, center, size, player_goal, CPU_goal):
        super().__init__(sprite, center, size)
        self.player_goal   = player_goal # [x1, y1, x2, x2]
        self.CPU_goal      = CPU_goal # [x1, y1, x2, x2]
        self.player_points = 0
        self.CPU_points    = 0

    def score(self, disk):
        center = disk.get_center()
        if self.player_goal[0] > center[0] > self.player_goal[2] and self.player_goal[1] > center[1] > self.player_goal[3]:
            self.CPU_points += 1
        if self.CPU_goal[0] > center[0] > self.CPU_goal[2] and self.CPU_goal[1] > center[1] > self.player_goal[3]:
            self.player_goal += 1