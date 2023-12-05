import random
from timeit import default_timer as timer


def quick_sort(arr):
    quick_sort_impl(arr, 0, len(arr) - 1)
    return arr


def quick_sort_impl(arr, left, right):
    if left < right:
        q = partition(arr, left, right)
        quick_sort_impl(arr, left, q - 1)
        quick_sort_impl(arr, q + 1, right)


def partition(arr, left, right):
    j = random.randint(left, right)
    x = arr[j]
    arr[j], arr[right] = arr[right], arr[j]
    less = left
    for i in range(left, right):
        if arr[i] <= x:
            arr[i], arr[less] = arr[less], arr[i]
            less += 1
    arr[less], arr[right] = arr[right], arr[less]
    return less


if __name__ == "__main__":
    t = 0
    n = 5
    for _ in range(n):
        arr = random.sample(range(10**8), 10**8)
        start = timer()
        quick_sort(arr)
        end = timer()
        t += end - start
    print(f"Average running time of sequential algorithm: {t / n} sec.")
