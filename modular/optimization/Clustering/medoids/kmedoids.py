import kmedoids_cpp

def clustering_medoids(dist, medoids):
    result = kmedoids_cpp.run_kmedoids(dist, medoids)
    return result