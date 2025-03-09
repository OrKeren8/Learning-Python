from concurrent.futures import ProcessPoolExecutor
import os
import psutil
import numpy as np

def set_cpu_affinity():
    p = psutil.Process(os.getpid())
    p.cpu_affinity(list(range(os.cpu_count())))  # Use all cores

set_cpu_affinity()

def process(data_list):
    for i in range(len(data_list)):
        data_list[i][2] = data_list[i][0]+data_list[i][1]
    return data_list

def batch_square(numbers):
    return [n * n for n in numbers]

def create_indices_list(size):
    indices = np.indices((size,size), int, False)
    print(indices)
    in_poly = np.zeros((size, size), dtype=int)
    result = np.dstack((indices[0], indices[1], in_poly)).reshape(size*size, 3)
    return result

def return_mat_to_shape(flatted, size):
    return_to_the_future = flatted.reshape(size, size, 3)
    return return_to_the_future
    
def multi_process_task(data, batch_size):
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        results = list(executor.map(process, [data[i:i+batch_size] for i in range(0, len(data), batch_size)]))
    result = np.concatenate(results, axis=0)
    return result

def main():
    size = 20000
    res = create_indices_list(size)
    print("1")
    res = multi_process_task(res, 10000)
    print("2")
    res = return_mat_to_shape(res, size)
    res[size-3:size, 0:size, 2] = 1
    # print(res)


if __name__ == "__main__":
    main()    