import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Given data
t = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]).reshape(-1, 1)
volume_of_H2 = np.array([0, 0.8, 1.8, 2.8, 3.6, 4.4, 5.2, 6, 6.8, 7.4, 8])

# Create and fit the model
model = LinearRegression()
model.fit(t, volume_of_H2)

# Predict for the given time points
predicted_volumes = model.predict(t)
print(model.coef_)

print(model.intercept_)
# Plot the data and the linear regression line
plt.figure(figsize=(10, 6))
plt.scatter(t, volume_of_H2, color='blue', label='Actual Data')
plt.plot(t, predicted_volumes, color='red', label='Trend Line')
plt.title('Volume of H2 vs. Time for NaCl')
plt.xlabel('Time (minutes)')
plt.ylabel('Volume of H2 (mL)')
plt.legend()
plt.grid(True)
plt.show()
