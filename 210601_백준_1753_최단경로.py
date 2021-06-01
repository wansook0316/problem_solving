import sys
import heapq

sys.setrecursionlimit(10 ** 6)
INF = 1e7
input = sys.stdin.readline
graph = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]

v, e = map(int, input().split())
start = int(input())
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 갱신된 녀석들 중 가장 작은 거리를 가지고 있는 녀석 추출
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        # 이걸 해주는 이뉴는 우선순위 큐를 사용하기 때문에
        # 더 짧은 노드를 기준으로 다른 노드를 탐색하다가 업데이트했던 거리보다 작은 것이 나왔을 수 있기 때문임
        # 만약에 순차적으로 q에 담겨서 진행했다면 안그랬겠지

        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))  # 탐색해볼 가치가 있음


for d in distance:
    if d == INF:
        print("INF")
    else:
        print(d)
