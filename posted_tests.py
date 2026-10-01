import random
from sorts import insertion_sort, merge_sort, quicksort
try:
    from sorts import heapsort as fourth
except ImportError:
    from sorts import counting_sort as fourth
from search import linear_search, binary_search

for f in (insertion_sort, merge_sort, quicksort, fourth):
    assert f([]) == []
    assert f([5]) == [5]
    assert f([3, 1, 2, 1]) == [1, 1, 2, 3]
    assert f([2, 2, 2]) == [2, 2, 2]
    assert f(list(range(9, -1, -1))) == list(range(10))
    a = [random.randrange(1000) for _ in range(500)]
    b = list(a)
    assert f(a) == sorted(a)
    assert a == b

assert linear_search([7, 2, 9], 9) == 2
assert linear_search([7, 2, 9], 5) == -1
assert binary_search([1, 3, 5, 7], 7) == 3
assert binary_search([1, 3, 5, 7], 4) == -1
assert binary_search([], 1) == -1
print("all posted tests pass")