import Converter
import locations_pb2
import numpy as np
import timeit

# Create a C++ extension module using pybind11


def extract_coordinates(location_data, lat_arr, lon_arr):
    """
    Extract coordinates from a LocationData object and store them in NumPy arrays.

    Args:
        location_data (locations_pb2.LocationData): The LocationData object.
        lat_arr (np.ndarray): The array to store latitudes.
        lon_arr (np.ndarray): The array to store longitudes.

    Returns:
        int: The number of coordinates extracted.
    """
    size = len(location_data.polygon)
    for i in range(size):
        lat_arr[i] = location_data.polygon[i].lat
        lon_arr[i] = location_data.polygon[i].lon
    return size

for points in range(100000, 200000, 100000):

    # Create a LocationData object and populate it
    location_data = locations_pb2.LocationData()
    coordinates = [locations_pb2.Coordinates(lon=10.0, lat=20.0) for _ in range(points)]
    location_data.polygon.extend(coordinates)

    # Create NumPy arrays to hold the latitudes and longitudes
    lat_arr = np.zeros(len(coordinates), dtype=np.double)
    lon_arr = np.zeros(len(coordinates), dtype=np.double)

    # Call the C++ function to extract coordinates

    total = 0
    total_time_1 = 0
    total_time_2 = 0


    start_time = timeit.default_timer()
    size = Converter.extract_coordinates(location_data, lat_arr, lon_arr)
    end_time = timeit.default_timer()
    total_time_1 += end_time - start_time
    print(f"Time taken: {total_time_1*1000} miliseconds")

    start_time = timeit.default_timer()
    size = extract_coordinates(location_data, lat_arr, lon_arr)
    end_time = timeit.default_timer()
    total_time_2 += end_time - start_time
    print(f"Time taken: {total_time_2*1000} miliseconds")
    # print(total_time_1, total_time_2, total_time_2/total_time_1, total_time_2-total_time_1, total/1e6)
    print(total_time_2/total_time_1, points)
    total += points

    # Print out the result
    # print(f"Number of elements: {size}")
    # print(f"Latitudes: {lat_arr}")
    # print(f"Longitudes: {lon_arr}")


