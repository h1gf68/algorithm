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



if __name__ == "__main__":
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
    graph2 = [[math.inf for _ in range(n + 1)] for i in range(n + 1)]
    visited = [False for _ in range(n+1)]
    for i in range(1, n + 1):
        graph2 = dfs(graph2, graph_firstly, visited, i, i, 0, 0)


    time_, path_ = dijkstra_sled_quick(graph2, tv, 1)
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