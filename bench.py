
import random
import time
import statistics


def make_input(n: int, shape: str) -> list:
    if n < 0:
        raise ValueError("n must be non-negative")

    if shape == "shuffled":
        result = list(range(n))
        random.shuffle(result)

    elif shape == "sorted":
        result = list(range(n))

    elif shape == "reversed":
        result = list(range(n - 1, -1, -1))

    elif shape == "dups":
        result = [random.randint(0, 9) for _ in range(n)]

    else:
        raise ValueError("Unknown input shape")

    return result


def bench(fn, sizes, shape="shuffled", repeats=3):
    if repeats < 1:
        raise ValueError("repeats must be at least 1")

    results = []

    for n in sizes:
        times = []

        for _ in range(repeats):
            data = make_input(n, shape)

            start = time.perf_counter()
            fn(data)
            end = time.perf_counter()

            times.append(end - start)

        median_time = statistics.median(times)
        results.append((n, median_time))

    return results


if __name__ == "__main__":
    from sorts import (
        insertion_sort,
        merge_sort,
        quicksort,
        heapsort
    )

    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quicksort,
        "Heapsort": heapsort
    }

    sizes = [100, 500, 1000, 2000]
    shapes = ["shuffled", "sorted", "reversed", "dups"]

    for shape in shapes:
        print("\nInput shape:", shape)
        print("-" * 65)
        print(f"{'Algorithm':<20} {'Size':>10} {'Time (seconds)':>20}")

        for name, fn in algorithms.items():
            for n, seconds in bench(fn, sizes, shape, repeats=3):
                print(f"{name:<20} {n:>10} {seconds:>20.6f}")