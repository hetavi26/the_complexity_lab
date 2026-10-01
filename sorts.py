import random

def insertion_sort(a: list) -> list:

    result = list(a)

    for i in range(1, len(result)):
        current = result[i]
        j =i - 1

        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result

def merge_sort(a: list) -> list:

    if len(a) <= 1:
        return list(a)

    mid = len(a) // 2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quicksort(a: list) -> list:
    result = list(a)

    def quicksort_helper(items):
        if len(items) <= 1:
            return items

        pivot = random.choice(items)

        less = []
        equal = []
        greater = []

        for item in items:
            if item < pivot:
                less.append(item)
            elif item > pivot:
                greater.append(item)
            else:
                equal.append(item)

        return (
            quicksort_helper(less)
            + equal
            + quicksort_helper(greater)
        )

    return quicksort_helper(result)

def heapsort(a: list) -> list:
    result = list(a)
    n = len(result)

    def heapify(size, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < size and result[left] > result[largest]:
            largest = left

        if right < size and result[right] > result[largest]:
            largest = right

        if largest != root:
            result[root], result[largest] = (
                result[largest],
                result[root]
            )
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

   
    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        heapify(i, 0)

    return result
