import itertools as it
def permutations(arr, ind=0):

    if ind == len(arr) - 1:
        print(''.join(arr))

    for i in range(ind, len(arr)):
        arr[i], arr[ind] = arr[ind], arr[i]
        permutations(arr, ind + 1)
        arr[i], arr[ind] = arr[ind], arr[i]

def perms(arr, stroka=""):
    n = len(arr)
    if n == 2:
        stroka += "".join(map(str, arr[::-1]))
        print(stroka)
    for i in range(2, n+1):
        perms(arr[n-i:])

def perms2(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    print(n)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    print([p for p in indices])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

# if __name__ == "__main__":
#     n = int(input().strip())
#     arr = [str(i) for i in range(1, n+1)]
#     perms2(arr)
#     print(" ----- ")

# ----------------------------------------------

import heapq
import queue

def get_long_edge(arr, arr_heap):
    visited = [0 for _ in range(len(arr))]
    max_weight, i, j = arr_heap[0].pop()
    q = queue.Queue()
    part = 2
    weights = 0

    while max_weight:
        visited[i] = part
        part = 2 ** (part % 2)
        q.put(i)
        weights += 1000 - max_weight

        max_weight, i, j = arr_heap[j].pop()
 

if __name__ == "__main__":
    n = int(input().strip)
    arr_heap = [heapq.heapify([]) for _ in range(n)]
    arr = [[0 for _ in range(n)] for i in range(n)]

    for i in range(n):
        for j, weight in enumerate(input().strip().split()):
            arr[i][j] = weight
            if weight > 0:
                arr[i].push((1000 - weight, i, j))

    get_long_edge(arr, arr_heap)