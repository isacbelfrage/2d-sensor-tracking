from src.model import MovingObject

def main() -> None:
    start_x = 0.0
    start_y = 0.0
    vx = 1.0
    vy = 0.5
    dt = 0.1
    obj = MovingObject(start_x, start_y, vx, vy)
    positions: list[tuple(float, float)] = [(start_x, start_y)]

    for _ in range(100):
        obj.update(dt)
        positions.append((obj.x, obj.y))

    print(positions[0])
    print(positions[100])


if __name__ == "__main__":
    main()