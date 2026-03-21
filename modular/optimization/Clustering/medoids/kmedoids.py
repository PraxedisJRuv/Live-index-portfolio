import kmedoids_cpp

def clustering_medoids(dist,num_medoids):
    medoids=[0]*num_medoids
    for i in range(num_medoids):
        medoids[i]=i
    result = kmedoids_cpp.run_kmedoids(dist, medoids)
    return result