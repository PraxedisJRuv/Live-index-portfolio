#This is intended as script for testing kmedodis.cpp. It's great to use when changes are made
import numpy as np
import kmedoids_cpp

dist = np.array([
    [1,0.5,0,0,0],
    [0.5,1,0,0,0],
    [0,0,1,0.5,0.5],
    [0,0,0.5,1,0],
    [0,0,0.5,0,1]
], dtype=float)

medoids = [0,1]

def clustering_medoids(dist, medoids):
    result = kmedoids_cpp.run_kmedoids(dist, medoids)
    print(result)

clustering_medoids(dist,medoids)
"""
        {1,0.5,0,0,0},
        {0.5,1,0,0,0},
        {0,0,1,0.5,0.5},
        {0,0,0.5,1,0},
        {0,0,0.5,0,1}
"""