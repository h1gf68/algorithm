def dinosaurs(mines, n, i, counter):
    for j in range(1, n+1):
        if (i, j) not in mines:
            if i == n:
                return counter + 1
            counter = dinosaurs(mines | mark_mines(set(), n, i, j), n, i+1, counter)
    return counter

def mark_mines(mines, n, i, j):
    mines.add((i, j))
    for x in range(1, n+1-i):
        mines.add((i+x, j))
        mines.add((i+x, j+x))
        mines.add((i+x, j-x))
    return mines

def dinosaurs_input():
    n = int(input().strip())
    print(dinosaurs(set(), n, 1, 0))


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
        weight = get_long(arr, a, b)
        if weight > max_weight:
            max_weight = weight
            parts = p
        counter += 1
        if counter > half:
            return str(max_weight), " ".join(parts)

    return str(max_weight), " ".join(parts)

def get_long(arr, a, b):
    weight = 0
    for i in a:
        for j in b:
            weight += arr[i][j]
    return weight

def get_comb_input():
    n = int(input().strip())
    arr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        arr[i] = list(map(int, input().strip().split()))

    print("\n".join(get_comb(arr, n)))


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
                prev = v
            if counter == n:
                dist += graph[p[-1]][0]
                min_dist.append(dist)
    return min(min_dist) if min_dist else -1

def get_min_cycle_input():
    n = int(input().strip())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, input().strip().split()))
    print(get_min_cycle(graph))


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

def gen_brackets_input():
    n = int(input().strip())
    d = {
        '(': ')',
        '[': ']',
    }
    gen_brackets(n, d)


if __name__ == "__main__":
    # dinosaurs_input()
    # get_comb_input()
    # get_min_cycle_input()
    gen_brackets_input()