import numpy as np 
import matplotlib.pyplot as plt

"""
    1. Membuat data
    2. Mambuat plot
    3. Menampilkan plotnya
"""
# 1. Membuat data
x = np.array([1,2,3,4,5])
y = np.array([1,4,9,16,25])

y2 = np.array([1,16,81,256,625])

# 2. Membuat plotnya
plt.plot(x,y)
plt.plot(x,y2)

# 3. Menampilkan plotnya
plt.show()

