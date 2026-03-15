#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

// Función que recibe un array y devuelve uno nuevo con los valores duplicados
py::array_t<double> procesar_array(py::array_t<double> input_array) {
    auto r = input_array.unchecked<1>(); // Acceso rápido de solo lectura (1 dimensión)
    size_t size = r.shape(0);
    
    // Crear un nuevo array para el resultado
    py::array_t<double> result_array(size);
    auto w = result_array.mutable_unchecked<1>(); // Acceso de escritura
    
    for (size_t i = 0; i < size; i++) {
        w(i) = r(i) * 2.0; // Procesamiento
    }
    
    return result_array;
}

PYBIND11_MODULE(mi_modulo, m) {
    m.def("procesar", &procesar_array, "Multiplica los elementos por 2");
}
