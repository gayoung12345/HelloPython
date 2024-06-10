class Shape:
    area = 0
    def __add__(self, other):
        return self.area + other.area
    
    def __sub__(self, other):
        return self.area - other.area

    def __lt__(self, other):
        return self.area < other.area