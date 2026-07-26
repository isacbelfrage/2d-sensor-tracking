from src.model import MovingObject
from src.sensor import PositionSensor

def main() -> None:
    sensor_1 = PositionSensor(1)
    sensor_2 = PositionSensor(1)
    sensor_3 = PositionSensor(1)

    obj = MovingObject(0, 0, 2, 1)
    real_positions: list[tuple[float, float]] = []
    estimated_positions: list[tuple[float, float]] = []

    for _ in range(100):
        obj.update(0.1)
        real_positions.append((obj.x, obj.y))
        sum_x = 0.0
        sum_y = 0.0
        sensor_readings = [sensor_1.measure(obj.x, obj.y), 
                           sensor_2.measure(obj.x, obj.y), 
                           sensor_3.measure(obj.x, obj.y)]
        for reading in sensor_readings:
            sum_x += reading[0]
            sum_y += reading[1]
        estimated_pos = (sum_x / len(sensor_readings), sum_y / len(sensor_readings))
        estimated_positions.append(estimated_pos)

    print(real_positions[99])
    print(estimated_positions[99])


if __name__ == "__main__":
    main()