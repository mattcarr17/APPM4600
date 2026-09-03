# Matt Carr - APPM 4600 Lab 1
# 3.2 Exercises: The Basics

import numpy as np
import matplotlib.pyplot as plt

# Create two Numpy Arrays
# These will be used to create semilogy plot

x = np.linspace(0, 100, num=50)
y = np.arange(0, 50)


# Print first three entries of x
print('the first three entries of x are: ', x[:3])

# vector w
w = 10**(-np.linspace(1,10,10))

# w is a vector with increasing orders of magnitude

x = np.arange(0,len(w))

plt.semilogy(x, w)
plt.xlabel('X')
plt.ylabel('W')
plt.title('X vs W Seminology Plot')

s = 3*w

plt.semilogy(x, s)

plt.show()

