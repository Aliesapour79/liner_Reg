import matplotlib.pyplot as plt 
import numpy as np 
# Data points

xpoint = np.array([1,2,3,4])
ypoint = np.array([2,3,5,4])

# Linear regression equation: y = mx + b

def square(x, result=[]):
    for y in x:
        result.append(y**2)
    return result

def liner_reg(xp, yp):
    sum_x = sum(xpoint)
    sum_y = sum(ypoint)
    sum_xy = sum(np.multiply(xp, yp))
    sum_of_sq = (sum_x**2)
    if len(xp) == len(yp):
        n = len(xp)
    else:
        print("Invalid Values")
        return None, None
    sum_sq_x = sum(square(xp))

    m = (n * (sum_xy) - (sum_x * sum_y)) / (n * sum_sq_x - sum_x**2)
    b = (sum_y - m * sum_x) / n
    return m, b

m, b = liner_reg(xpoint, ypoint)

# Predict y values based on the regression model

y_p = []
for x in xpoint:
    y = b + m * x
    y_p.append(y)


# Calculate errors and metrics

error = ypoint - y_p
error_sq = error**2
sum_square = sum(error_sq)
mse = sum_square / len(xpoint)

# Display results


print("Predicted y: ", y_p)
print("Error: ", error)
print("E^2: ", error_sq)
print("Sum of Squared Error: ", sum_square)
print("MSE: ", mse)


# Plot the data and the regression line


plt.scatter(xpoint, ypoint, color="red", label="Original Data")
plt.plot(xpoint, y_p, color="blue", label="Fitted Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
