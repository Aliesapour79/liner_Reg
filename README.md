```markdown
# Linear Regression Implementation

## Overview

This project demonstrates a manual implementation of linear regression from scratch without using pre-built libraries. It covers the following steps:

1. **Data Definition:** Defines input data points for `x` and `y` used in the linear regression model.
2. **Calculation of Regression Coefficients:** Computes the slope and intercept of the regression line using manual formulas.
3. **Prediction:** Predicts `y` values based on the linear regression model.
4. **Error Calculation:** Calculates errors, squared errors, and Mean Squared Error (MSE) to evaluate the model's performance.
5. **Plotting:** Plots the actual data points and the regression line for visualization.

## Files

- `linear_regression.py`: Contains the code for implementing linear regression manually.

## Usage

To run the code, ensure you have `numpy` and `matplotlib` installed. Then execute the script as follows:

```bash
python linear_regression.py
```

This will display the predicted `y` values, errors, squared errors, and Mean Squared Error (MSE). It will also generate a plot showing the actual data points and the regression line.

## Dependencies

- `numpy`: For numerical operations and array manipulations.
- `matplotlib`: For plotting graphs and visualizations.

## Code Explanation

### `linear_regression.py`

1. **Data Definition:**
   - Defines sample data points `x_values` and `y_values`.

2. **Functions:**
   - `calculate_square(values)`: Computes the square of each value in the given list.
   - `linear_regression(x, y)`: Calculates the slope and intercept for the linear regression line using manual formulas.

3. **Prediction and Error Calculation:**
   - Uses the computed slope and intercept to predict `y` values.
   - Calculates errors and Mean Squared Error (MSE) for model evaluation.

4. **Plotting:**
   - Uses `matplotlib` to plot the actual data points and the regression line.

## Example Output

When running the script, you will get an output similar to:

```
Predicted y:  [2.3, 3.1, 3.9000000000000004, 4.7]
Errors:  [-0.3 -0.1  1.1 -0.7]
Squared Errors:  [0.09 0.01 1.21 0.49]
Sum of Squared Errors:  1.7999999999999994
Mean Squared Error (MSE):  0.44999999999999984
```

And a plot showing the actual data points and the regression line.

## Author

[Ali.ei]
