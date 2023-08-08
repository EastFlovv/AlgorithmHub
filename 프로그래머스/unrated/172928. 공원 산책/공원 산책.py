# 이중배열, 현재위치, 4방위, 거리(str)
def move_dog(board, cur_pos, direction, distance):
    dis = int(distance)
#     현재 위치
    ci, cj = cur_pos
#     이동 방향
    mi = 0
    mj = 0
    if direction == 'N':
        mi = -1
    elif direction == 'S':
        mi = 1
    elif direction == 'W':
        mj = -1
    else:
        mj = 1
    
    for i in range(dis):
#         이동
        ci += mi
        cj += mj
        
#         만약 실패조건을 만난다면 원래 위치를 전송
        if 0 > ci or 0 > cj or len(board) == ci or len(board[0]) == cj:
            return cur_pos
        elif board[ci][cj] == 'X' :
            return cur_pos
#     실패하지 않는다면 변경된 위치를 전송
    return (ci, cj)

def solution(park, routes):
    
# park -> 공원 배열
# routes -> 명령 배열
# 명령은 수행 불가능하면 실행하지 않는다

# 3*3 ~ 50*50
# 시작지는 S, 이동 가능은 O, 이동 불가는 X
# 명령은 최대 50개
# 명령 NSWE각 4방위
# 최대 9칸 이동함

# 리턴은 최종 좌표의 위치를 반환

#     실제로 사용할 맵
    board = [[] for _ in range(len(park))]
#     현재 로봇의 위치
    cur_pos = (0, 0)

    for i in range(len(park)):
        blocks = list(park[i])
        board[i] = blocks
        for j in range(len(blocks)):
            if blocks[j] == 'S':
                cur_pos = (i, j)
#     board, cur_pos를 설정

#     명령을 수행
    for order in routes:
        
        direction, distance = order.split(' ')
        
#         유효성을 검사하는 함수가 필요하다
        cur_pos = move_dog(board, cur_pos, direction, distance)
    
    answer = [cur_pos[0], cur_pos[1]]
    return answer