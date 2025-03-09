from concurrent.futures import ProcessPoolExecutor
import os
import psutil

def set_cpu_affinity():
    p = psutil.Process(os.getpid())
    p.cpu_affinity(list(range(os.cpu_count())))  # Use all cores

set_cpu_affinity()

def batch_square(numbers):
    return [n * n for n in numbers]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        batch_size = 100  # Process batches instead of single numbers
        numbers = range(1, 1000)
        results = list(executor.map(batch_square, [numbers[i:i+batch_size] for i in range(0, len(numbers), batch_size)]))

    flattened_results = [num for sublist in results for num in sublist]  # Flatten result list
    print(flattened_results)