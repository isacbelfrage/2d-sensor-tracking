class MovingObject:
    def __init__(self, x: float, y: float, vx: float, vy: float):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def update(self, dt: float) -> None:
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt

