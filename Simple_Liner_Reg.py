import matplotlib.pyplot as plt 
import numpy as np 

# Data points
x_values = np.array([1, 2, 3, 4])
y_values = np.array([2, 3, 5, 4])

# Linear regression equation: y = mx + b
def calculate_square(values):
    squared_values = []
    for value in values:
        squared_values.append(value**2)
    return squared_values

def linear_regression(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(np.multiply(x, y))
    n = len(x)
    
    if len(x) != len(y):
        print("Invalid Values")
        return None
    
    sum_of_squares_x = sum(calculate_square(x))
    
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_of_squares_x - sum_x**2)
    intercept = (sum_y - slope * sum_x) / n
    return slope, intercept

slope, intercept = linear_regression(x_values, y_values)

# Predict y values based on the regression model
predicted_y_values = []
for x in x_values:
    y = intercept + slope * x
    predicted_y_values.append(y)

# Calculate errors and metrics
errors = y_values - predicted_y_values
squared_errors = errors**2
sum_of_squared_errors = sum(squared_errors)
mean_squared_error = sum_of_squared_errors / len(x_values)

# Display results
print("Predicted y: ", predicted_y_values)
print("Errors: ", errors)
print("Squared Errors: ", squared_errors)
print("Sum of Squared Errors (SSE): ", sum_of_squared_errors)
print("Mean Squared Error (MSE): ", mean_squared_error)

# Plot the data and the regression line
plt.scatter(x_values, y_values, color="blue", label="Actual Data")
plt.plot(x_values, predicted_y_values, color="red", label="Regression Line")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.show()
