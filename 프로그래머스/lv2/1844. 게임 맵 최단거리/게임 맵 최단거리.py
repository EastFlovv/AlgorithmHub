# 다음 위치를 반환하는 함수, 이동 할 수 없으면 -1, -1을 반환
def next_pos(cur_x, cur_y, x, y, max_x, max_y):
    ret = 0
    
    ret_x = cur_x + x
    ret_y = cur_y + y
    if 0 <= ret_x < max_x and 0 <= ret_y < max_y:
        ret = (ret_x, ret_y)
    else:
        ret = (-1, -1)
    
    return ret

# 지도에 값을 입력하는 함수, 현재 값이 지도의 값보다 작을때만 값을 넣는다
def set_move(board, cur_x, cur_y, move):
    cur_val = board[cur_x][cur_y]
    
    if move < cur_val:
        board[cur_x][cur_y] = move
        return True
    else:
        return False
    
# 방문 좌표를 저장하는 함수
def add_visit(cur_x, cur_y, arr):
    new_arr = arr.copy()
    node = (cur_x, cur_y)
    new_arr.append(node)
    return new_arr

# maps 초기화
def board_init(maps, max_x, max_y):
    board = [[0 for _ in range(max_y)] for _ in range(max_x)]
    
    for i in range(max_x):
        for j in range(max_y):
            if maps[i][j] == 0:
                # print(f'maps[{i}][{j}] == 0 board[{i}][{j}] == -1')
                board[i][j] = -1
                # print(board)/
            else:
                board[i][j] = 100000
    return board

# 다음 노드에 접근 가능한지 보는 함수
def accessable(board, cur_x, cur_y, visit):
    if board[cur_x][cur_y] == -1 or (cur_x, cur_y) in visit:
        return False
    return True

def solution(maps):
#     x = i, y = j
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    max_x = len(maps)
    max_y = len(maps[0])
    
    board = board_init(maps, max_x, max_y)
    
    # print('board')
    # print(board)
    
    cur = (0, 0, 1, [(0,0)])
    que = []
    que.append(cur)
    
    while(len(que) > 0):
#         노드에서 값을 추출
        cur_x, cur_y, move, visit = que.pop(0)
        
#         현재 노드의 움직임 값이 목표 도착값 보다 크거나 같으면 패스
        if move >= board[max_x-1][max_y-1]:
            continue
#         다음 움직임
        next_move = move + 1
#         4방 탐색
        for i in range(4):
#           새 좌표를 구한다
            new_x, new_y = next_pos(cur_x, cur_y, dx[i], dy[i], max_x, max_y)
#           새 좌표가 유효하지 않으면 패스
            if new_x == -1:
                continue
#           새 좌표가 접근 가능하면(지도에서 움직일 수 있으면) 아래의 프로세스를 실행
            if accessable(board, new_x, new_y, visit):
#                 board에 최소 움직임 값을 기록 -> 현재가 최소가 아니면 패스함
                if set_move(board, new_x, new_y, next_move):
#                   방문 했기 때문에 방문 기록을 추가한다
                    new_visit = add_visit(new_x, new_y, visit)
#                     새 노드에 다음 좌표와 움직임 값, 그리고 방문기록을 추가
                    new_node = (new_x, new_y, next_move, new_visit)
#                     새 노드를 큐에 넣는다
                    que.append(new_node)
    
#     print(board)
    
    answer = -1 if board[max_x-1][max_y-1] == 100000 else board[max_x-1][max_y-1]
    return answer



# bfs로 하여 이동한다.
# 각 bfs마다 이전 이동에 대한 기록을 갖고 있어야한다
# 그렇다면 튜플은 현재 좌표, 방문 좌표, 이동한 거리 세가지 정보를 갖고 있어야함