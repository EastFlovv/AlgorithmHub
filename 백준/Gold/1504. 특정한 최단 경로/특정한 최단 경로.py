import sys
import heapq

INF = 1000000000

def get_input():
    return sys.stdin.readline().strip()

def dijkstra(start):
    distance = [INF for x in range(n+1)]
    distance[start] = 0

    que = []
    heapq.heappush(que, (start, 0))

    while que:
        node, dist = heapq.heappop(que)

        for next_node in relation[node]:
            if dist + next_node[1] < distance[next_node[0]]:
                distance[next_node[0]] = dist + next_node[1]
                heapq.heappush(que, (next_node[0], dist + next_node[1]))
    return distance


# 정점, 간선
n, e = map(int, get_input().split(' '))

relation = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, get_input().split(' '))
    relation[a].append((b, c))
    relation[b].append((a, c))

v1, v2 = map(int, get_input().split(' '))

original = dijkstra(1)
v1distance = dijkstra(v1)
v2distance = dijkstra(v2)

case1 = original[v1] + v1distance[v2] + v2distance[n]
case2 = original[v2] + v2distance[v1] + v1distance[n]

ans = min(case1, case2)
print(ans if ans < INF else -1)