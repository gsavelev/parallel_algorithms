import random

from joblib import Parallel, delayed
from timeit import default_timer as timer


class ParallelQuickSort:
    def __init__(self, n_jobs):
        self.k = 0
        self.n_jobs = n_jobs

    def partition(self, arr, l, r):
        i = l + 1
        j = r
        key = arr[l]
        while True:
            while i < r and key >= arr[i]:
                i += 1
            while key < arr[j]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                arr[l], arr[j] = arr[j], arr[l]
                return j

    def quickSort(self, arr, l, r):
        if l < r:
            p = self.partition(arr, l, r)
            with Parallel(n_jobs=self.n_jobs):
                self.k += 1
                delayed(self.quickSort(arr, l, p - 1))
                self.k += 1
                delayed(self.quickSort(arr, p + 1, r))

    def run(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    t = 0
    n = 5
    for _ in range(n):
        arr = random.sample(range(10**8), 10**8)
        pqs = ParallelQuickSort(n_jobs=4)
        start = timer()
        pqs.run(arr)
        end = timer()
        t += end - start
    print(f"Average running time of parallel algorithm: {t / n} sec.")
