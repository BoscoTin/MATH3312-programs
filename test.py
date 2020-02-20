import numpy as np

B = [
    [1,1,0,3],
    [0,-1,-1,-5],
    [0,0,3,13],
    [0,0,0,-13]
]

A = [
    [1,1,0,3],
    [2,-1,-1,1],
    [3,-1,-1,2],
    [-1,2,3,-1]
]

invB = np.linalg.inv(np.array(B))

result = np.matmul(A,invB)
print result
