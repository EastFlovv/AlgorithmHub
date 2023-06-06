def rotate(board):
    for i in range(len(board)):
        line = []
        for j in range(len(board), 0, -1):
            line.append(board[j-1][i])
        board[0][i] = line
    return board[0]


loop = int(input())

for tc in range(loop):
    size = int(input())
    board = [['' for _ in range(3)] for _ in range(size)]
    tmp = [[] for _ in range(size)]

    for i in range(size):
        tmp[i] = input().strip().split(' ')
        # board[i] = input().strip().split(' ')

    for i in range(3):
        tmp = rotate(tmp)

        for j in range(size):
            board[j][i] = ''.join(tmp[j])

    print(f'#{tc+1}')
    for i in range(size):
        print(' '.join(board[i]))



