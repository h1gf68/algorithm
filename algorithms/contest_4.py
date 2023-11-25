import itertools as it
import math
import time


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


def get_comb2(arr, n, first, segm=2, s=set([5]), v="5 ", counter=1):
    if counter == n:
        print(v)

    for i in range(n):
        if i != first and i not in s:
            segm = 2 ** (segm % 2)
            get_comb2(arr, n, first, segm, s|{i}, v+str(i)+" ", counter+1)


import itertools


def get_comb(arr, n):
    max_weight = 0
    parts = ""
    counter = 0
    half = 2 ** n // 2
    for p in itertools.product("21", repeat=n):
        a = []
        b = []
        for i in range(n):
            if p[i] == '2':
                a.append(i)
            else:
                b.append(i)
        weight = get_long(arr, n, p, a, b)
        if weight > max_weight:
            max_weight = weight
            parts = p
        counter += 1
        if counter > half:
            return str(max_weight), " ".join(parts)

    return str(max_weight), " ".join(parts)


def get_long(arr, n, visited, a, b):
    weight = 0
    for i in a:
        for j in b:
            weight += arr[i][j]
    return weight


# if __name__ == "__main__":
#     n = int(input().strip())
#     arr = [[0 for _ in range(n)] for _ in range(n)]
#
#     for i in range(n):
#         arr[i] = list(map(int, input().strip().split()))
#
#     print("\n".join(get_comb(arr, n)))

# ---------------------------------------------------------------

import itertools

def get_min_cycle(graph):
    min_dist = []
    n = len(graph)
    for p in itertools.permutations(range(n)):
        if p[0] == 0:
            prev = 0
            dist = 0
            counter = 1
            for v in p:
                if v == 0:
                    continue
                if graph[prev][v] == 0:
                    break
                counter += 1
                dist += graph[prev][v]
                # print(p, prev, v, dist)
                prev = v
            if counter == n:
                dist += graph[p[-1]][0]
                min_dist.append(dist)
    return min(min_dist) if min_dist else -1



# if __name__ == "__main__":
#     n = int(input().strip())
#     graph = [[0 for _ in range(n)] for _ in range(n)]
#
#     for i in range(n):
#         graph[i] = list(map(int, input().strip().split()))
#     # start = time.time()
#     print(get_min_cycle(graph))
#     # print(time.time()-start)

# --------------------------------------------------------------


def gen_brackets(count, d, stack=[], s=''):
    if count % 2:
        print()
        return

    if len(s) == count:
        print(s)
        return

    if len(stack) < count-len(s):
        gen_brackets(count, d, stack+['('], s + '(')
    if len(stack) < count-len(s):
        gen_brackets(count, d, stack+['['], s + '[')

    if len(stack) and d.get(stack[-1]) == ')':
        gen_brackets(count, d, stack[:-1], s + ')')
    if len(stack) and d.get(stack[-1]) == ']':
        gen_brackets(count, d, stack[:-1], s + ']')


if __name__ == "__main__":
    n = int(input().strip())
    d = {
        '(': ')',
        '[': ']',
    }
    gen_brackets(n, d)