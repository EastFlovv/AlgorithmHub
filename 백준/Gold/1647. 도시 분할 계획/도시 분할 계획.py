import sys
import heapq

# n개의 집, m개의 길
# 유지비 c
# 마을을 두개로 분리 -> 즉 입력은 하나의 head를 가지는데 이를 두개로 분리
# 분리 된 마을간 경로를 다 삭제
# 유지비의 합을 최소로

# 크루스칼 알고리즘을 통해 최소 신장 트리를 구현한 뒤에
# 가장 cost긴 길을 삭제하고 나머지의 합을 구한다

# 즉 최소 신장 트리를 구현하면서 현재 나온 값 중 가장 큰 값을 삭제할것

def getInput():
    return sys.stdin.readline().strip()

def getHead(node):
    global parents
    if parents[node] != node:
        parents[node] = getHead(parents[node])
    return parents[node]

# def setHead(head, target):
#     global parents
#     for i in range(len(parents)):
#         if parents[i] == target:
#             parents[i] = head

def union_parent(a, b):
    global parents
    a = getHead(a)
    b = getHead(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n, m = map(int, getInput().split())
heap = []
parents = [i for i in range(n + 1)]
cost = 0
curMax = 0

for _ in range(m):
    a, b, c = map(int, getInput().split(' '))
    heapq.heappush(heap, (c, a, b))

while len(heap) > 0:
    tmp = heapq.heappop(heap)
    head1 = getHead(tmp[1])
    head2 = getHead(tmp[2])

    if head1 != head2:
        union_parent(head1, head2) if head1 < head2 else union_parent(head2, head1)
        cost += tmp[0]
        if tmp[0] > curMax:
            curMax = tmp[0]

print(cost - curMax)