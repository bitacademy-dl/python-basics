
class Multiply:
    def __init__(self):
        self.x = None
        self.y = None

    def __str__(self):
        return f'Multiply(x={self.x}, y={self.y})'

    def forward(self, x, y):
        self.x = x
        self.y = y

        out = self.x * self.y
        return out