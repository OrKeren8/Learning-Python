#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>

namespace py = pybind11;

size_t extract_coordinates(py::object location_data, py::array_t<double> lat_arr, py::array_t<double> lon_arr) {
    
    // Get the pointer to the NumPy arrays
    auto lat_buffer = lat_arr.request();
    double* lat_ptr = static_cast<double*>(lat_buffer.ptr);
    auto lon_buffer = lon_arr.request();
    double* lon_ptr = static_cast<double*>(lon_buffer.ptr);
    
    // Access the 'polygon' field in the LocationData protobuf
    auto polygon = location_data.attr("polygon");
    
    size_t i = 0;
    for (auto coord : polygon) {
        lon_ptr[i] = coord.attr("lon").cast<double>();
        lat_ptr[i] = coord.attr("lat").cast<double>();
        i++;
    }

    // Return the size of the repeated object (number of coordinates)
    return i;
}

PYBIND11_MODULE(Converter, m) {
    m.def("extract_coordinates", &extract_coordinates, "Extract lat and lon into NumPy arrays and return the size of the polygon");
}
