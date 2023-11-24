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


import itertools


def get_comb(arr, n):
    max_weight = 0
    parts = ""
    for p in itertools.product("21", repeat=n):
        weight = get_long(arr, n, p)
        if weight > max_weight:
            max_weight = weight
            parts = p

    return str(max_weight), " ".join(parts)


def get_long(arr, n, visited):
    s = set()
    weight = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            if visited[i] != visited[j]:
                weight += arr[i][j]
                s.add((i, j))
                s.add((j, i))
    return weight


def get_comb2(arr, n, first, segm=2, s=set([5]), v="5 ", counter=1):
    if counter == n:
        print(v)

    for i in range(n):
        if i != first and i not in s:
            segm = 2 ** (segm % 2)
            get_comb2(arr, n, first, segm, s|{i}, v+str(i)+" ", counter+1)



# if __name__ == "__main__":
#     n = int(input().strip())
#     arr = [[0 for _ in range(n)] for _ in range(n)]
#
#     for i in range(n):
#         for j, weight in enumerate(map(int, input().strip().split())):
#             arr[i][j] = weight
#
#     # print("\n".join(get_comb(arr, n)))
#     get_comb2(arr, n, 5)


import heapq
def get_long_edge(heap, j):
    new_heap = [[] for _ in range(len(heap))]
    for a in heap:
        heapq.heapify(a)

    visited = [0 for _ in range(len(heap))]
    part = 2
    weights = 0
    s = set()

    while heap[j]:
        max_weight, i, j = heapq.heappop(heap[j])
        new_heap[i].append((max_weight, i, j))
        # print(weights, 1000-max_weight, i+1, j+1, "visited", visited[i], visited[j])
        if (i, j) in s:
            j = i
            continue

        s.add((i, j))
        s.add((j, i))

        if not visited[i]:
            visited[i] = part
            part = 2 ** (part % 2)
        if not visited[j]:
            visited[j] = part
            part = 2 ** (part % 2)
        if visited[i] != visited[j]:
            weights += 1000 - max_weight

    for h in heap:
        while h:
            max_weight, i, j = heapq.heappop(h)
            new_heap[i].append((max_weight, i, j))
            if visited[i] != visited[j] and (i, j) not in s:
                s.add((i, j))
                s.add((j, i))
                weights += 1000 - max_weight
    return (weights, " ".join(map(str, visited))), new_heap


if __name__ == "__main__":
    n = int(input().strip())
    arr_heap = [[] for _ in range(n)]
    arr = [[0 for _ in range(n)] for _ in range(n)]
    sum_j = []
    for i in range(n):
        for j, weight in enumerate(map(int, input().strip().split())):
            arr[i][j] = weight
            if weight > 0:
                arr_heap[i].append((1000-weight, i, j))

    weight = 0
    visited = "2 1"
    min_id = min_sum = 20*1000
    for j in range(n):
        tmp_sum = sum(arr[j])
        if tmp_sum <= min_sum:
            min_sum = tmp_sum
            min_id = j

        # res, arr_heap = get_long_edge(arr_heap, j)
        # print(j, res)
        # if res[0] >= weight:
        #     weight = res[0]
        #     visited = res[1]
    print(min_sum, min_id)
    (weight, visited), arr = get_long_edge(arr_heap, min_id)

    print(weight)
    print(visited)
    print(sum_j)

