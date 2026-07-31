# Design decisions

## Tracking algorithm
- For equivalent sensors with approximately the same amount of noise simply taking the mean value of all the sensor readings will work because each reading is independent. If the amount of noise differs per sensor a more suitable option is to do the approximation with inverse-variance weighting so the more accurate sensors are taken more into considerations.

- The weighting is calculated by: $1 / (\text{noise_std})^2$. The reason for this is because the greater the variance of the sensors readings the less it should be taken into consideration. This currently requires each participating sensor to have a positive `noise_std`. PositionSensor itself still supports zero noise for idealized simulations and tests.

## Assumptions
For this implementation some important assumptions have been made:

- All sensor errors are independent.
- The sensor errors have the mean value zero.
- Every sensors noise-level is positive and known.
- x- and y-errors are handeled the same way.

