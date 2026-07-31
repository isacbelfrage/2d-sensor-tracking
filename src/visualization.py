import matplotlib.pyplot as plt


def plot_positions(real_positions: list[tuple[float, float]],
                   sensor_readings: list[tuple[float, float]],
                   mean_estimates: list[tuple[float, float]],
                   weighted_mean_estimates: list[tuple[float, float]],
                   alpha_beta_estimates: list[tuple[float, float]]) -> None:
    real_x, real_y = split_positions(real_positions)
    sensor_x, sensor_y = split_positions(sensor_readings)
    mean_x, mean_y = split_positions(mean_estimates)
    weighted_mean_x, weighted_mean_y = split_positions(weighted_mean_estimates)
    alpha_beta_x, alpha_beta_y = split_positions(alpha_beta_estimates)

    plt.plot(real_x, real_y, label="Real")
    #plt.scatter(sensor_x, sensor_y, label="Individual sensor", marker="o", alpha=0.6)
    #plt.scatter(mean_x, mean_y, label="Mean estimate", marker="x", alpha=0.6)
    plt.scatter(weighted_mean_x, weighted_mean_y, label="Weighted mean estimate", marker="s", alpha=0.6)
    plt.plot(alpha_beta_x, alpha_beta_y, label="Alpha-beta filter estimate")
    
    plt.legend()
    plt.ylabel("y-axis")
    plt.xlabel("x-axis")
    plt.title("Tracking")
    plt.axis("equal")

    plt.show()


def split_positions(positions: list[tuple[float, float]]) -> tuple[list[float], list[float]]:
    x_positions = []
    y_positions = []
    for pos in positions:
        x_positions.append(pos[0])
        y_positions.append(pos[1])
    return (x_positions, y_positions)