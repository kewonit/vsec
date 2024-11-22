import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 1, 5, 3])
categories = ['A', 'B', 'C', 'D', 'E']

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y, 'r-o')
plt.title('Line Plot')
plt.xlabel('X values')
plt.ylabel('Y values')

plt.subplot(1, 2, 2)
plt.bar(categories, y)
plt.title('Bar Chart')

plt.tight_layout()
plt.show()