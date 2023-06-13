import sys
import heapq

parents = []
heap = []
cost = 0

def initParents(n):
    global parents
    parents = [i for i in range(n+1)]

def getParents(com):
    if parents[com] == com:
        return com
    return getParents(parents[com])

def setParents(head, target):
    for i in range(len(parents)):
        if parents[i] == target:
            parents[i] = head

n = int(sys.stdin.readline().strip())
initParents(n)

m = int(sys.stdin.readline().strip())
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split(" "))
    heapq.heappush(heap, (c, a, b))

while(len(heap) > 0):
    tmp = heapq.heappop(heap)
    head1 = getParents(tmp[1])
    head2 = getParents(tmp[2])

    if head1 != head2:
        if head1 < head2:
            setParents(head1, head2)
        else:
            setParents(head2, head1)
        cost += tmp[0]

print(cost)