#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <vector>
#include <algorithm>

namespace py = pybind11;
using namespace std;

double sum_total(const vector<int>& medoids,
                 const vector<vector<double>>& dist)
{
    int n = dist.size();
    double sum = 0.0;

    for(int i = 0; i < n; i++){
        double best = 1e18;

        for(int m : medoids)
            best = min(best, dist[i][m]);

        sum += best;
    }

    return sum;
}

vector<int> run_kmedoids(py::array_t<double> dist_np,
                         vector<int> medoids)
{
    auto buf = dist_np.request();
    double* ptr = (double*) buf.ptr;

    int n = buf.shape[0];
    int m = buf.shape[1];

    vector<vector<double>> dist(n, vector<double>(m));

    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            dist[i][j] = ptr[i*m + j];

    int k = medoids.size();
    bool mejora = true;

    while(mejora){

        mejora = false;
        double bestsum = sum_total(medoids, dist);

        for(int mi=0; mi<k; mi++){
            for(int i=0; i<n; i++){

                vector<int> nuevo = medoids;
                nuevo[mi] = i;

                double c = sum_total(nuevo, dist);

                if(c < bestsum){
                    medoids = nuevo;
                    bestsum = c;
                    mejora = true;
                }
            }
        }
    }

    return medoids;
}

PYBIND11_MODULE(kmedoids, m) {
    m.def("run_kmedoids", &run_kmedoids);
}