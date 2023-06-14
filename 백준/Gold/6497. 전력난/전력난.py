import sys
import heapq

# 집 수, 길 수
# a,b,c 제공
# 절약할 수 있는 최대 비용을 출력
# 모든 cost를 더하고, 크루스칼을 통해 만든 값을 차감하여 리턴

parents = []
total = 0
cost = 0
heap = []

def get_input():
    val = sys.stdin.readline().strip()
    return val

def get_head(node):
    global parents
    if parents[node] != node:
        parents[node] = get_head(parents[node])
    return parents[node]

def union_head(head1, head2):
    global parents
    a = get_head(head1)
    b = get_head(head2)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def clear_val():
    global parents, total, cost, heap
    parents = []
    total = 0
    cost = 0
    heap = []

while True:
    n, m = map(int, get_input().split(' '))

    # 0 0 이면 break
    if n == m == 0:
        break

    parents = [i for i in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, get_input().split(' '))
        heapq.heappush(heap, (c, a, b))

    while len(heap) > 0:
        c, a, b = heapq.heappop(heap)
        head1 = get_head(a)
        head2 = get_head(b)
        total += c
        if head1 != head2:
            union_head(head1, head2)
            cost += c

    print(total - cost)
    clear_val()