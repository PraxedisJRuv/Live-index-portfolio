import numpy as np
from optimization.Clustering.medoids.test import clustering_medoids
dist = np.array([
    [1,0.5,0,0,0],
    [0.5,1,0,0,0],
    [0,0,1,0.5,0.5],
    [0,0,0.5,1,0],
    [0,0,0.5,0,1]
], dtype=float)

medoids = [0,1]

clustering_medoids(dist,medoids)
