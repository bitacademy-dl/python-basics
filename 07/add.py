# class Add

class Add:
    def __init__(self):
        self.x = None
        self.y = None

    def __str__(self):
        return f'Add({self.x}, {self.y})'

    def forward(self, x, y):
        self.x = x
        self.y = y

        z = x + y
        return z
