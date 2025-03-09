from typing import List, Iterable
import timeit

VALUES = [7, 3, 3, 5, 6, 8, 2]

def check_time(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        res = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(end_time-start_time)
        return res
    return wrapper

@check_time
def count_occurrences_from_list(values: Iterable[int]) -> dict[int, int]:
    occurrences: dict[int, int] = {}
    for num in values:
        try:
            occurrences[num] += 1
        except:
            occurrences[num] = 1
    return occurrences

def occurrences_from_file() -> Iterable[int]:
    values: List[int] = []
    with open("values.txt", "r") as f:
        for item in f:
            values.append(int(item))
    return values

def occurrences_generator() -> Iterable[int]:
    with open("values.txt", "r") as f:
        for item in f:
            yield int(item)

def main():
    print(count_occurrences_from_list(VALUES))
    print(count_occurrences_from_list(occurrences_from_file()))
    print(count_occurrences_from_list(occurrences_generator()))

if __name__ == "__main__":
    main()