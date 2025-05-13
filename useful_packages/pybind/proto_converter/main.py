import Converter
import locations_pb2
import timeit
import psutil
import numpy as np
from concurrent.futures import ProcessPoolExecutor
import multiprocessing




def extract_coordinates(location_data, lat_arr, lon_arr):
    size = len(location_data.polygon)
    for i in range(size):
        lat_arr[i] = location_data.polygon[i].lat
        lon_arr[i] = location_data.polygon[i].lon
    return size

def batch_extract_coordinates(chunk):
    lat = [pt.lat for pt in chunk]
    lon = [pt.lon for pt in chunk]
    return lat, lon



def extract_multi_process(location_data, lats, lons):
    num_workers = 2
    size = len(location_data.polygon)
    chunk_size = size // num_workers
    with ProcessPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(batch_extract_coordinates, (location_data.polygon[i:i + chunk_size] for i in range(0, size, chunk_size))))

    lats = np.concatenate([np.array(lat) for lat, _ in results])
    lons = np.concatenate([np.array(lon) for _, lon in results])
    
    
def main():

    points = 100000  # Number of points to generate

    # Create a LocationData object and populate it
    location_data = locations_pb2.LocationData()
    coordinates = [locations_pb2.Coordinates(lon=10.0, lat=20.0) for _ in range(points)]
    location_data.polygon.extend(coordinates)


    # Create NumPy arrays to hold the latitudes and longitudes
    lat_arr = np.zeros(len(coordinates), dtype=np.double)
    lon_arr = np.zeros(len(coordinates), dtype=np.double)

    
    start_time = timeit.default_timer()
    size = Converter.extract_coordinates(location_data, lat_arr, lon_arr)
    end_time = timeit.default_timer()
    time = end_time - start_time
    print(f"Time taken: {time*1000} miliseconds")

    start_time = timeit.default_timer()
    size = extract_coordinates(location_data, lat_arr, lon_arr)
    end_time = timeit.default_timer()
    time = end_time - start_time
    print(f"Time taken: {time*1000} miliseconds")

    start_time = timeit.default_timer()
    size = extract_multi_process(location_data, lat_arr, lon_arr)
    end_time = timeit.default_timer()
    time = end_time - start_time
    print(f"Time taken: {time*1000} miliseconds")

    t1 = timeit.default_timer()
    lons = np.fromiter((pt.lon for pt in location_data.polygon), dtype=np.float64, count=len(location_data.polygon))
    lats = np.fromiter((pt.lat for pt in location_data.polygon), dtype=np.float64, count=len(location_data.polygon))
    print((timeit.default_timer() - t1) * 1000, "ms")  # in 80ms for 100k points, the most elegant way in good time



    t1 = timeit.default_timer()
    Converter.extract_coordinates(location_data, lat_arr, lon_arr)
    coordinates = [locations_pb2.Coordinates(lon=lon, lat=lat) for lon, lat in zip(lon_arr, lat_arr)]
    t2 = timeit.default_timer()
    location_data.polygon.extend(coordinates)
    t3 = timeit.default_timer()
    size = lon_arr.size
    for i in range(size):
        coord = locations_pb2.Coordinates(lon=lon_arr[i], lat=lat_arr[i])
        location_data.polygon.append(coord)
    t4 = timeit.default_timer()
    for lon, lat in zip(lon_arr, lat_arr):
        coord = locations_pb2.Coordinates(lon=lon, lat=lat)
        location_data.polygon.append(coord)
    t5 = timeit.default_timer()
    print(f"1Time taken: {(t2 - t1) * 1000} miliseconds")
    print(f"2Time taken: {(t3 - t2) * 1000} miliseconds")
    print(f"3Time taken: {(t4 - t3) * 1000} miliseconds")
    print(f"4Time taken: {(t5 - t4) * 1000} miliseconds")

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Needed for Windows to properly spawn new processes
    main()



# Print out the result
# print(f"Number of elements: {size}")
# print(f"Latitudes: {lat_arr}")
# print(f"Longitudes: {lon_arr}")


