#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

int sum_array(py::array_t<int> input) {
    auto buf = input.request(); // get buffer info
    int* ptr = static_cast<int*>(buf.ptr);
    size_t len = buf.size;

    int sum = 0;
    for (size_t i = 0; i < len; i++) {
        sum += ptr[i];
    }
    return sum;
}

PYBIND11_MODULE(heavyCalc, m) {
    m.def("sum_array", &sum_array, "Sum elements of a NumPy array");
}
