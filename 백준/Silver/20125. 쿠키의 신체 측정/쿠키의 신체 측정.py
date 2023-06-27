import sys

def get_input():
    return sys.stdin.readline().strip()

def get_heart():
   for i in range(size):
        for j in range(size):
            if board[i][j] == '*':
                return (i + 1, j)

def get_larm(heart_i, heart_j):
    i = heart_i
    j = heart_j - 1
    tmp = board[i][j]
    length = 0
    while tmp == '*':
        length += 1
        j -= 1
        if j == -1:
            break
        tmp = board[i][j]
    return length

def get_rarm(heart_i, heart_j):
    i = heart_i
    j = heart_j + 1
    tmp = board[i][j]
    length = 0
    while tmp == '*':
        length += 1
        j += 1
        if j == size:
            break
        tmp = board[i][j]
    return length

def get_body(heart_i, heart_j):
    i = heart_i + 1
    j = heart_j
    tmp = board[i][j]
    length = 0
    while tmp == '*':
        length += 1
        i += 1
        tmp = board[i][j]
    return length

def get_lleg(bodyend_i, bodyend_j):
    i = bodyend_i + 1
    j = bodyend_j - 1
    tmp = board[i][j]
    length = 0
    while tmp == '*':
        length += 1
        i += 1
        if i == size:
            break
        tmp = board[i][j]
    return length

def get_rleg(bodyend_i, bodyend_j):
    i = bodyend_i + 1
    j = bodyend_j + 1
    tmp = board[i][j]
    length = 0
    while tmp == '*':
        length += 1
        i += 1
        if i == size:
            break
        tmp = board[i][j]
    return length

heart_i = 0
heart_j = 0

l_arm = 0
r_arm = 0
body = 0
body_end = (0, 0)
l_leg = 0
r_leg = 0

size = int(get_input())

board = [[] for _ in range(size)]

for i in range(size):
    board[i] = list(get_input())

heart_i, heart_j = get_heart()

l_arm = get_larm(heart_i, heart_j)
r_arm = get_rarm(heart_i, heart_j)
body = get_body(heart_i, heart_j)
body_end = (heart_i + body ,heart_j)
l_leg = get_lleg(body_end[0], body_end[1])
r_leg = get_rleg(body_end[0], body_end[1])

print(heart_i+1, heart_j+1)
print(l_arm, r_arm, body, l_leg, r_leg)