import numpy as np 
import matplotlib.pyplot as plt

#create some sample data (1d array for simplicity)
data = np.random.normal(scale=0.5, size=1000)

#Reshape the data to fit the model input format
data = data.reshape(-1, 1)

plt.plot(range(len(data)), data)
plt.show()