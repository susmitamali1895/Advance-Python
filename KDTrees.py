# Find the nearest neighbor to point(1,1)
from scipy.spatial import KDTree
points =[(1,-1),(2,3),(-2,3),(2,-3)]
kdtree = KDTree(points)
res = kdtree.query((1,1))
print(res)
