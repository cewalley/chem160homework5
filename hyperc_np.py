import numpy as np

import random

n = 1000 # no of trails

x1 = np.random.random(n)

x2 = np.random.random(n)

y1 = np.random.random(n)

y2 = np.random.random(n)

z1 = np.random.random(n)

z2 = np.random.random(n)

dist=np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2))

print(dist,0.66170)
