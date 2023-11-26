import math

def dijkstra_slow(arr, n, start, finish, m):
    dist = [m for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    dist[start] = 0
    visited[0] = True
    for _ in range(n):
        m_ = m
        for j in range(1, n + 1):
            if not visited[j] and dist[j] < m_:
                m_ = dist[j]
                id_m = j
        for g, e in arr[id_m]:
            if dist[g] > dist[id_m] + e:
                dist[g] = dist[id_m] + e
        visited[id_m] = True

    return dist[finish] if dist[finish] < m else -1

def dijkstra_slow_input():
    n, s, f = map(int, input().strip().split())
    arr = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        line = input().strip().split()
        for j in range(1, len(line) + 1):
            if i != j and int(line[j-1]) != -1:
                arr[i].append((j, int(line[j - 1])))
    print(dijkstra_slow(arr, n, s, f, math.inf))


import math
def dijkstra_slow_path(arr, n, start, finish, m):
    if start == finish:
        return start

    dist = [m for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    path = [-1 for _ in range(n+1)]
    dist[start] = 0
    visited[0] = True
    for _ in range(n):
        m_ = m
        for j in range(1, n + 1):
            if not visited[j] and dist[j] < m_:
                m_ = dist[j]
                id_m = j
        for g, e in arr[id_m]:
            if dist[g] > dist[id_m] + e:
                dist[g] = dist[id_m] + e
                path[g] = id_m
        visited[id_m] = True
    res = [finish]
    while path[finish] != -1:
        res.append(path[finish])
        finish = path[finish]
    return " ".join(map(str, res[::-1])) if len(res) > 1 else -1

def dijkstra_slow_path_input():
    n, s, f = map(int, input().strip().split())
    arr = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        line = input().strip().split()
        for j in range(1, len(line) + 1):
            if i != j and int(line[j-1]) != -1:
                arr[i].append((j, int(line[j - 1])))

    print(dijkstra_slow_path(arr, n, s, f, math.inf))


import math
import heapq
def dijkstra_quick(arr, n, s, f, m):
    dist = [m for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    dist[s] = 0
    l = [(0, s)]
    heapq.heapify(l)
    visited[0] = True
    while l:
        m_, id_m = heapq.heappop(l)
        if visited[id_m]:
            continue
        for g, e in arr[id_m]:
            if visited[g]:
                continue
            if dist[g] > dist[id_m] + e:
                dist[g] = dist[id_m] + e
                heapq.heappush(l, (dist[g], g))
        visited[id_m] = True
    return dist[f] if dist[f] < m else -1

def dijkstra_quick_input():
    n, k = map(int, input().strip().split())
    arr = [[] for _ in range(n + 1)]
    for _ in range(1, k + 1):
        a, b, ln = map(int, input().strip().split())
        arr[a].append((b, ln))
        arr[b].append((a, ln))
    start, finish = map(int, input().strip().split())
    print(dijkstra_quick(arr, n, start, finish, math.inf))


import math
import heapq
def dijkstra_timing(arr, n, start, finish, m):
    dist = [m for _ in range(n + 1)]
    dist[start] = 0
    visited = [False for _ in range(n + 1)]
    visited[0] = True
    l = [(0, start, 0)]
    heapq.heapify(l)

    while l:
        m_, id_m, ct = heapq.heappop(l)
        if visited[id_m]:
            continue
        for b, at, bt in arr[id_m]:
            if visited[b]:
                continue
            if dist[b] > bt and at >= ct:
                dist[b] = bt
                heapq.heappush(l, (dist[b], b, bt))
        visited[id_m] = True
    return dist[finish] if dist[finish] < m else -1

def dijkstra_timing_input():
    n = int(input().strip())
    start, finish = map(int, input().strip().split())
    r = int(input().strip())

    arr = [[] for _ in range(n + 1)]
    for _ in range(1, r + 1):
        a, at, b, bt = map(int, input().strip().split())
        arr[a].append((b, at, bt))

    print(dijkstra_timing(arr, n, start, finish, math.inf))


import sys
import math
import heapq
def dijkstra_sled_quick(graph, tv, start):
    l = [(0, start)]
    heapq.heapify(l)
    m = math.inf
    n = len(graph)
    time_ = [m for _ in range(n)]
    time_[start] = 0
    visited = [False for _ in range(n)]
    visited[0] = True
    path = [-1 for _ in range(n)]
    while l:
        t, town = heapq.heappop(l)
        if visited[town]:
            continue
        for town_ in range(2, len(graph)):
            if visited[town_]:
                continue
            if town > town_:
                dist_ = graph[town][town_]
            else:
                dist_ = graph[town_][town]
            t_ = tv[town_][0] + dist_ / tv[town_][1]
            t_ += time_[town]
            if time_[town_] > t_:
                time_[town_] = t_
                heapq.heappush(l, (time_[town_], town_))
                path[town_] = town
        visited[town] = True

    return time_, path


def dfs(graph, graph_firstly, visited, goal_town, town, dist, prev_town, counter=1):
    counter += 1
    visited[town] = True
    for town_, dist_ in graph_firstly[town]:
        if town_ != prev_town:
            graph[goal_town][town_] = dist + dist_
            dfs(graph, graph_firstly, visited, goal_town, town_, dist+dist_, town, counter)

    return graph


def dijkstra_sled_input():
    n = int(input().strip())

    tv = [() for _ in range(n + 1)]
    for i in range(1, n + 1):
        t, v = map(int, input().strip().split())
        tv[i] = (t, v)

    graph_firstly = [[] for _ in range(n + 1)]
    for _ in range(1, n):
        a, b, s = map(int, input().strip().split())
        graph_firstly[a].append((b, s))
        graph_firstly[b].append((a, s))

    sys.setrecursionlimit(3000)
    graph = [[math.inf for _ in range(n + 1)] for i in range(n + 1)]
    visited = [False for _ in range(n+1)]
    for i in range(1, n + 1):
        graph = dfs(graph, graph_firstly, visited, i, i, 0, 0)
    time_, path_ = dijkstra_sled_quick(graph, tv, 1)
    ind = t = 0
    for i in range(1, len(time_)):
        if t < time_[i]:
            t = time_[i]
            ind = i
    path = [ind]
    while path_[ind] != -1:
        path.append(path_[ind])
        ind = path_[ind]

    print('{:.10f}'.format(t))
    print(" ".join(map(str, path)))


if __name__ == "__main__":
    # dijkstra_slow_input()
    # dijkstra_slow_path_input()
    # dijkstra_quick_input()
    # dijkstra_timing_input()
    dijkstra_sled_input()