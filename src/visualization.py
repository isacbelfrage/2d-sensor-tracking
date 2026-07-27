import matplotlib.pyplot as plt


def plot_positions(real_positions: list[tuple[float, float]],
                   sensor_positions: list[tuple[float, float]],
                   estimated_positions: list[tuple[float, float]]) -> None:
    real_x, real_y = split_positions(real_positions)
    sensor_x, sensor_y = split_positions(sensor_positions)
    estimated_x, estimated_y = split_positions(estimated_positions)

    plt.plot(real_x, real_y,label="Real")
    plt.scatter(sensor_x, sensor_y, label="Sensor 1", alpha=0.6)
    plt.scatter(estimated_x, estimated_y, label="Estimated", alpha=0.6)
    
    plt.legend()
    plt.ylabel("y-axis")
    plt.xlabel("x-axis")
    plt.title("Tracking")
    plt.show()


def split_positions(positions: list[tuple[float, float]]) -> tuple[list[float], list[float]]:
    x_positions = []
    y_positions = []
    for pos in positions:
        x_positions.append(pos[0])
        y_positions.append(pos[1])
    return (x_positions, y_positions)