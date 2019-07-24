import numpy as np

vertices = np.array([[3,4,5], [7,8,9], [4,9,3]])

p = np.array([2,7,4])

d = np.sqrt(np.sum(np.square((vertices-p)), axis=1))

print(vertices[d.argmin()], d.min())


