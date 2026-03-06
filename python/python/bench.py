import time
from workloads import sum_to_n, count_positives, max_value


def time_sum_to_n(n: int) -> None:
    start = time.perf_counter()
    result = sum_to_n(n)
    end = time.perf_counter()
    print(f"sum_to_n({n}) = {result}, time = {end - start:.6f} s")


def time_count_positives(size: int) -> None:
    data = list(range(-size // 2, size // 2))
    start = time.perf_counter()
    result = count_positives(data)
    end = time.perf_counter()
    print(f"count_positives({size}) = {result}, time = {end - start:.6f} s")


def time_max_value(size: int) -> None:
    data = list(range(size))
    start = time.perf_counter()
    result = max_value(data)
    end = time.perf_counter()
    print(f"max_value({size}) = {result}, time = {end - start:.6f} s")


if __name__ == "__main__":
    time_sum_to_n(100_000)
    time_count_positives(100_000)
    time_max_value(100_000)
