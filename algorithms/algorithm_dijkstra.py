import math
import heapq
import queue
import time
import sys

import memory_profiler


def dijkstra(arr, n, s, f, m):
    dist = [m for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    dist[s] = 0
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

    return dist[f] if dist[f] < m else -1


def dijkstra_timing(arr, n, s, f, m):
    dist = [m for _ in range(n + 1)]
    dist[s] = 0
    visited = [False for _ in range(n + 1)]
    visited[0] = True
    l = [(0, s, 0)]
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
    return dist[f] if dist[f] < m else -1


def dijkstra_path(arr, n, s, f, m):
    if s == f:
        return s

    dist = [m for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    path = [-1 for _ in range(n + 1)]
    dist[s] = 0
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
    res = [f]
    while path[f] != -1:
        res.append(path[f])
        f = path[f]
    return " ".join(map(str, res[::-1])) if len(res) > 1 else -1


def dfs(graph, tv, visited, curr_town, dist, goal_town):
    visited[curr_town] = True
    for town_, dist_, t_ in graph[curr_town]:
        if not visited[town_]:
            dist += dist_
            if curr_town > goal_town:
                tab = tv[town_][0] + dist / tv[town_][1]
                tba = tv[goal_town][0] + dist / tv[goal_town][1]
                graph[town_].append((goal_town, dist, tab))
                graph[goal_town].append((town_, dist, tba))
                dfs(town_, dist, goal_town)
            else:
                dfs(town_, dist_, goal_town)




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


def bfs(counter, graph, graph_firstly, town_dist):
    q = queue.Queue()
    q.put(town_dist)
    # visited = [0 for _ in range(len(graph))]
    # visited[0] = 1
    goal_town = town_dist[0]

    while not q.empty():
        town, dist, prev_town = q.get()
        # visited[town] = 1
        for town_, dist_ in graph_firstly[town]:
            # if not visited[town_]:
            if town_ != prev_town:
                counter +=1
                # print(goal_town, " -- ", town, dist, visited[town], "---", town_, dist_, visited[town_])
                d = dist + dist_
                q.put((town_, d, town))

                if goal_town > town_:
                    graph[goal_town][town_] = d
                if goal_town < town_:
                    graph[town_][goal_town] = d
    return graph, counter


if __name__ == "__main__":
    n = int(input().strip())

    tv = [() for _ in range(n + 1)]
    for i in range(1, n + 1):
        t, v = map(int, input().strip().split())
        tv[i] = (t, v)

    graph = [[math.inf for _ in range(i + 1)] for i in range(n + 1)]
    graph_firstly = [[] for _ in range(n + 1)]

    for _ in range(1, n):
        a, b, s = map(int, input().strip().split())
        graph_firstly[a].append((b, s))
        graph_firstly[b].append((a, s))

    sec = time.time()
    counter = 0
    for i in range(1, n + 1):
        graph, counter = bfs(counter, graph, graph_firstly, (i, 0, 0))
    print(time.time()-sec, counter)

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
