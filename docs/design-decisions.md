# Design decisions

## Tracking algorithm
- For equivalent sensors with approximately the same amount of noise simply taking the mean value of all the sensor readings will work because each reading is independent. If the amount of noise differs per sensor a more suitable option is to do the approximation with inverse-variance weighting so the more accurate sensors are taken more into considerations.

- The weighting is calculated by: $w_i = \frac{1}{\sigma_i^2}$. The reason for this is because the greater the variance of the sensors readings the less it should be taken into consideration. This currently requires each participating sensor to have a positive `noise_std`. PositionSensor itself still supports zero noise for idealized simulations and tests.

### Alpha-beta filter
- I then implemented an alpha-beta filter and compared the weighted mean estimate to the filtered estimate produced by the alpha-beta filter. This resulted in a slightly lower mean position error compared to the true position. This does not mean that the filter is automatically better but with the current simulation of an object with a constant velocity the filter gave a lower mean position error. 

The alpha-beta filter uses its current position and velocity estimates to predict the object's position at the next time step. It then calculates the residual as the difference between the measured position and the predicted position. In this implementation, the measurement is the weighted mean estimate. The filter uses this residual to correct its position and velocity estimates. The same calculations are applied independently to the x- and y-coordinates. The parameters $\alpha$ and $\beta$ control how strongly the position and velocity estimates react to the residual.

The predicted position is: 

```math
\hat{x}_{k|k-1} = \hat{x}_{k-1} + \hat{v}_{k-1}\Delta t
```

The residual between the measurement and prediction is:

```math
r_k = z_k - \hat{x}_{k|k-1}
```

The corrected position and velocity are:

```math
\hat{x}_k = \hat{x}_{k|k-1} + \alpha r_k
```

```math
\hat{v}_k = \hat{v}_{k-1} + \frac{\beta}{\Delta t}r_k
```

- $\hat{x}$: estimated position
- $\hat{v}$: estimated velocity
- $z_k$: measured position at step $k$
- $r_k$: residual
- $\Delta t$: time between updates
- $k$: current time step

### Kalman filter

The Kalman filter estimates both the position and velocity of the tracked object. Its state is represented by the vector:

```math
\mathbf{x} =
\begin{bmatrix}
p \\
v
\end{bmatrix}
```

The current implementation is one-dimensional. Therefore, two independent filters are used: one for position and velocity along the x-axis and one for position and velocity along the y-axis. This assumes that motion and measurement errors along the two axes can be handled independently.

The filter alternates between two phases:

1. Predict the next state using the motion model.
2. Correct the prediction using a sensor measurement.

The important matrices and variables are:

- $F$, the state transition matrix, describes how the state evolves between time steps.
- $P$, the state covariance matrix, describes the uncertainty in the position and velocity estimates and the relationship between their errors.
- $Q$, the process noise covariance, represents uncertainty in the motion model.
- $H$, the measurement model, describes which part of the state is measured.
- $R$, the measurement variance, represents uncertainty in the measurement.
- $S$, the residual variance, represents the combined uncertainty of the prediction and measurement.
- $K$, the Kalman gain, determines how strongly the measurement corrects the prediction.

#### Prediction

The filter assumes a constant-velocity motion model. The state is predicted using:

```math
\mathbf{x}_{pred} = F\mathbf{x}
```

The state transition matrix is:

```math
F =
\begin{bmatrix}
1 & \Delta t \\
0 & 1
\end{bmatrix}
```

This gives the following prediction:

```math
p_{pred} = p + v\Delta t
```

```math
v_{pred} = v
```

The covariance is predicted using the same motion model:

```math
P_{pred} = FPF^T + Q
```

The constant-velocity model is not assumed to be perfect. An object may accelerate or otherwise deviate from the predicted motion. This uncertainty is represented by the process noise covariance:

```math
Q =
\sigma_a^2
\begin{bmatrix}
\Delta t^4/4 & \Delta t^3/2 \\
\Delta t^3/2 & \Delta t^2
\end{bmatrix}
```

Here, $\sigma_a^2$ is the acceleration variance. A larger acceleration variance means that the filter trusts the constant-velocity model less, while a smaller value means that it trusts the model more.

#### Measurement update

The measurement passed to the Kalman filter is the inverse-variance weighted mean of the sensor measurements. A sensor with lower variance is assigned a higher weight:

```math
w_i = \frac{1}{\sigma_i^2}
```

Assuming that the sensor errors are independent, the variance of the combined measurement is:

```math
R =
\frac{1}{\sum_i w_i}
=
\frac{1}{\sum_i 1/\sigma_i^2}
```

For sensor noise standard deviations of 1, 3, and 5, this gives:

```math
R =
\frac{1}{1/1^2 + 1/3^2 + 1/5^2}
\approx 0.869
```

The sensors measure position but do not directly measure velocity. The measurement model is therefore:

```math
H =
\begin{bmatrix}
1 & 0
\end{bmatrix}
```

The residual is the difference between the weighted sensor measurement and the position predicted by the filter:

```math
r = z - H\mathbf{x}_{pred}
```

The residual variance combines the uncertainty of the predicted state and the measurement:

```math
S = HP_{pred}H^T + R
```

The Kalman gain is then calculated as:

```math
K = P_{pred}H^TS^{-1}
```

A larger Kalman gain gives the measurement more influence, while a smaller gain gives the prediction more influence.

The state is corrected using the residual and the Kalman gain:

```math
\mathbf{x}_{new} = \mathbf{x}_{pred} + Kr
```

Although the sensors only measure position, the velocity estimate can also be corrected. This is possible because the covariance matrix represents the relationship between position and velocity uncertainty.

Finally, the covariance is updated after the measurement has been used:

```math
P_{new} = (I-KH)P_{pred}
```

The updated covariance represents the filter's uncertainty after combining the prediction with the measurement.

#### Initial values

Both filters use the following initial values:

- Initial position: `0.0`
- Initial velocity: `0.0`
- Initial position variance: `1.0`
- Initial velocity variance: `4.0`
- Acceleration variance: `0.1`

The initial position corresponds to the known starting position of the simulated object. The initial velocity is zero because the filter is not given the object's true velocity. The velocity variance is larger than the position variance because the initial velocity estimate is more uncertain.

The small acceleration variance reflects that the simulated object follows a constant-velocity model while still allowing some uncertainty in that model. These values are reasonable starting values for the current simulation, but they have not been proven to be optimal.

#### Experimental result

The Kalman filter was compared with the weighted mean and the alpha-beta filter using four reproducible sensor-noise sequences. It produced the lowest mean position error for all four tested random seeds.

On average, its error was 69.4% lower than the weighted mean error and 42.9% lower than the alpha-beta filter error. These results only apply to the current constant-velocity simulation, sensor-noise assumptions, and selected filter parameters. They do not prove that the Kalman filter will perform better for every motion model or noise condition.

The complete results are documented in [the filter experiment](experiment.md).



## Assumptions
For this implementation some important assumptions have been made:

- All sensor errors are independent.
- The sensor errors have the mean value zero.
- Every sensors noise-level is positive and known.
- x- and y-errors are handeled the same way.
