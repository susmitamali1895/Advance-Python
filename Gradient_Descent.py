# linear regression in gradient descent 
import numpy as np
#sample data
X = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

# initialize parameter
m = 0
b =0
alpha = 0.01
n = len(X)

# Gradient Descent 
for i in range(1000):
    y_pred = m * X +b
    dm = (-2/n) * np.sum(X *(y-y_pred))
    db = (-2/n) * np.sum(y - y_pred)
    m = m - alpha * dm
    b = b - alpha * db

print("Slope:", m)
print("Intercept:", b)
