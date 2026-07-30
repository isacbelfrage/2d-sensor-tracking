# Design desicions

## Tracking algorithm
- For equivalent sensors with approximately the same ammount of noise simply taking the mean value of all the sensor readings will work because each reading is independent. If the amount of noise differs per sensor a more suitable option is to do a weighted approximation where the more accurate sensors.

- The wheighting is calculated by: $1 / (noise_std)^2$ The reason for this is because the greater the standard deviation is that sensors readings should be taken less into consideration.

## Assumptions
For this implementation som important assumptions have been made:

- All sensor readings are independent.
- The sensors are independet from each other.
- The noise level is known.

