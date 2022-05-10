class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fall_to_point(self, lower_point, higher_point):
        if lower_point[0] < self.x < lower_point[0] \
            and higher_point[1] < self.y < higher_point[1]:

            return True
        else:
            return False

    def distance(self, x, y):
        d1 = x + self.x
        d2 = y + self.y
        return d1 - d2
