#This is intended as script for testing kmedodis.cpp. It's great to use when changes are made
import numpy as np
import cluster_module_cpp

dist = np.array([
    [0,0.5,1,1,1],
    [0.5,0,1,1,1],
    [1,1,1,0.5,0.5],
    [1,1,0.5,0,1],
    [1,1,0.5,1,0]
], dtype=float)

medoids = [0,1]

def clustering_assignation(dist, medoids):
    result = cluster_module_cpp.run_clustering(dist, medoids)
    print(result)
    return result

clustering_assignation(dist,medoids)

def evaluate_objective_f(dist, clusterization):
    obj=0
    for i in range (len(clusterization)):
        obj=dist[i][clusterization[i]]
    print(obj)

evaluate_objective_f(dist, clustering_assignation(dist, medoids))
"""
        {1,0.5,0,0,0},
        {0.5,1,0,0,0},
        {0,0,1,0.5,0.5},
        {0,0,0.5,1,0},
        {0,0,0.5,0,1}
"""