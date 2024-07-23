from point import Point
class Tracker:
    def __init__(self, p=None):
        if p is None:
            self.points = []
        else:
            self.points = [p]

    def add_point(self, p):
        self.points.append(p)

    def get_points(self):
        return self.points
