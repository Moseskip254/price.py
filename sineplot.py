from matplotlib import pyplot as plt
import numpy as py
import math #needed for definition of pi
x = np.arange(0,math.pi*2,0.05) # type: ignore
y = np.sin(x) # type: ignore
pl.plot(x,y) # type: ignore
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
plt.show()
