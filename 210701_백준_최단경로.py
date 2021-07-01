import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        now_cost, now_node = heapq.heappop(q)

        if now_cost > distance[now_node]:
            continue

        for next_node, weight in graph[now_node]:
            next_cost = now_cost + weight
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(q, [next_cost, next_node])


if __name__ == "__main__":
    INF = int(1e7)
    V, E = map(int, input().split())
    s = int(input())
    graph = [[] for _ in range(V + 1)]
    distance = [INF] * (V + 1)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])
    dijkstra(s)

    for i in range(1, len(distance)):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])