#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>

namespace py = pybind11;

//in order to build do: python setup.py build_ext --inplace

size_t extract_coordinates(py::object location_data, py::array_t<double> lat_arr, py::array_t<double> lon_arr) {
    
    //Get the pointer to the NumPy arrays
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

    return i;
}

int parse_and_extract(py::bytes data, py::array_t<double> lat_arr, py::array_t<double> lon_arr) {
    // 1) Parse the Protobuf from the raw bytes
    std::string s = data;  // copies the bytes
    LocationData msg;
    if (!msg.ParseFromString(s)) {
        throw std::runtime_error("Failed to parse LocationData");
    }
    // 2) Get the C pointers for your pre‑allocated NumPy arrays
    auto latb = lat_arr.request(), lonb = lon_arr.request();
    double* latp = static_cast<double*>(latb.ptr);
    double* lonp = static_cast<double*>(lonb.ptr);

    // 3) Fill them in one tight loop
    size_t n = msg.polygon_size();
    for (size_t i = 0; i < n; ++i) {
        const auto& pt = msg.polygon(i);
        lonp[i] = pt.lon();
        latp[i] = pt.lat();
    }
    return static_cast<int>(n);
}


PYBIND11_MODULE(Converter, m) {
        m.def("extract_coordinates", &extract_coordinates, "Extract lat and lon into NumPy arrays and return the size of the polygon");
        m.def("parse_and_extract", &parse_and_extract, "Parse serialized LocationData and fill two pre-allocated NumPy arrays");
}
