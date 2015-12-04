import matplotlib.pyplot as plt
import numpy as np
mu, sigma = 0, 0.1
noise = np.random.normal(mu, sigma, 200)/5
x = np.linspace(-1, 1, 200)
x2 = np.linspace(-0.7, 0.7, 200)
delta = 1*np.exp(-(x-0)**2/2)/(np.sqrt(2*np.pi)*1)
y = 0.5 - 0.8*x2**2 + noise + delta/2
y2 = 1.3*delta + noise - 0.1
fig = plt.figure('large deviate')
ax = fig.add_subplot(111)
ax2 = fig.add_subplot(111)
ax.fill_between(x2, y1=y, y2=y2, edgecolor='red', facecolor='blue', alpha=0.3)
ax2.plot(x, y2, color='black')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
