import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,2, sharey=True)

plt.ylim([0, 100])
plt.xlim([0, 1])

ax[0].plot(0.5, 40, 'bo')
ax[1].plot(0.5, 40, 'bo')

ax[0].axhline(20, 0, 1)

plt.show()
