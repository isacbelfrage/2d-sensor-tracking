# Design decisions

## Tracking algorithm
- For equivalent sensors with approximately the same amount of noise simply taking the mean value of all the sensor readings will work because each reading is independent. If the amount of noise differs per sensor a more suitable option is to do the approximation with inverse-variance weighting so the more accurate sensors are taken more into considerations.

- The weighting is calculated by: $w_i / \frac{1}{\sigma_i^2}$. The reason for this is because the greater the variance of the sensors readings the less it should be taken into consideration. This currently requires each participating sensor to have a positive `noise_std`. PositionSensor itself still supports zero noise for idealized simulations and tests.

- I then implemented an alpha-beta filter and compared the weighted mean estimate to the filtered estimate produced by the alpha-beta filter. This resulted in a slightly lower mean position error compared to the true position. This does not mean that the filter is automatically better but with the current simulation of an object with a constant velocity the filter gave a lower mean position error. 

The alpha-beta filter uses its current position and velocity estimates to predict the object's position at the next time step. It then calculates the residual as the difference between the measured position and the predicted position. In this implementation, the measurement is the weighted mean estimate. The filter uses this residual to correct its position and velocity estimates. The same calculations are applied independently to the x- and y-coordinates. The parameters $\alpha$ and $\beta$ control how strongly the position and velocity estimates react to the residual.

The predicted position is: 

$$
\hat{x}_{k|k-1}
=
\hat{x}_{k-1}
+
\hat{v}_{k-1}\Delta t
$$

The residual between the measurement and prediction is:

$$
r_k
=
z_k
-
\hat{x}_{k|k-1}
$$

The corrected position and velocity are:

$$
\hat{x}_k
=
\hat{x}_{k|k-1}
+
\alpha r_k
$$

$$
\hat{v}_k
=
\hat{v}_{k-1}
+
\frac{\beta}{\Delta t}r_k
$$

- $\hat{x}$: estimated position
- $\hat{v}$: estimated velocity
- $z_k$: measured position at step $k$
- $r_k$: residual
- $\Delta t$: time between updates
- $k$: current time step


## Assumptions
For this implementation some important assumptions have been made:

- All sensor errors are independent.
- The sensor errors have the mean value zero.
- Every sensors noise-level is positive and known.
- x- and y-errors are handeled the same way.

