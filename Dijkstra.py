# Dikstra = Use that method to find the shortest path in a graph from one element to another 
# it takes some arguments =
# return_predecessors: boolean (True to return whole path of traversal otherwise False)
# indices = index of the element to return all paths from that element only
#limit = max weight of path
# Find all shortest path from element 1 to 2
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
arr = np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
newarr = csr_matrix(arr)
print(dijkstra(newarr, return_predecessors = True, indices =0))
