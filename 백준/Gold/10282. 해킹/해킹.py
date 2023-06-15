import heapq
import sys

def get_input():
    return sys.stdin.readline().strip()

INF = float('inf')

loop = int(get_input())

for tc in range(loop):
    n, d, s = map(int, get_input().split(' '))

    relation = [[] for _ in range(n+1)]

    for i in range(d):
        a, b, c = map(int, get_input().split(' '))
        # b가 감염되면 c초 뒤 a가 감염
        relation[b].append((a, c))

    que = []
    heapq.heappush(que, (s, 0))
    time = [INF] * (n + 1)
    time[s] =  0

    while que:
        node, cost = heapq.heappop(que)

        # if cost > time[node]:
        #     continue
        
        # 다음 노드를 탐색
        for tmp in relation[node]:
            # tmp[0] -> 다음 노드, tmp[1] -> 다음 노드 감염에 소모될 시간
            infect = cost + tmp[1]
            # 다음 노드에 소모되는 시간이 현재 기록된것 보다 작으면 진입
            if time[tmp[0]] > infect:
                time[tmp[0]] = infect
                heapq.heappush(que, (tmp[0], infect))

    time = [x for x in time if x < INF]
    time.sort()
    print(len(time), time[len(time)-1])