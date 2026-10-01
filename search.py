
def linear_search(a: list, target) -> int:
    
    for i in range(len(a)):
        if a[i] == target:
            return i

    return -1


def binary_search(a: list, target) -> int:

    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == target:
            return mid

        elif a[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1