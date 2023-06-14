import sys
import heapq
# 다익스트라 알고리즘
# n*n칸에서 최소 값으로 좌상단에서 우하단까지 이동하기
# 이동은 어떤 방향이던 가능

dw = [1, -1, 0, 0]
dh = [0, 0, 1, -1]
tc = 1

def get_input():
    return sys.stdin.readline().strip()

while True:
    size = int(get_input())
    if size == 0:
        break

    board = [[] for _ in range(size)]
    for i in range(size):
        board[i] = list(map(int, get_input().split(' ')))

    w = 0
    h = 0

    djik = [[float('inf') for _ in range(size)] for _ in range(size)]
    djik[0][0] = board[0][0]
    # djik[0][1] = board[0][1]
    # djik[1][0] = board[1][0]

    que = []
    que.append((board[0][0], w, h))

    while len(que) > 0:
        val, pw, ph = que.pop(0)
#         네 방향을 검사하여 다음 위치로 이동 시키기?
        for i in range(4):
            nw = dw[i] + pw
            nh = dh[i] + ph
            if 0 <= nw < size and 0 <= nh < size:
#               검증 과정 수행?
#               해당 과정에서 이루어져야 할것
#               1. 현재 자신의 위치와 다음 위치의 값을 합친다
                n_val = val + board[nh][nw]
#               2. 합친 값이 이전 값보다 작으면 교체한다
                if djik[nh][nw] > n_val:
                    djik[nh][nw] = n_val
    #               3. 큐에 삽입한다?
    #               4. 큐를 우선순위 큐로 만들고 싶다
                    heapq.heappush(que, (n_val, nw, nh))
    print(f'Problem {tc}: {djik[size-1][size-1]}')
    tc += 1