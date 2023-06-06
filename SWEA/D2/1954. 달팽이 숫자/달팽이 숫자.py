def changeDir(idir, jd):
    if idir == 0 and jd == 1:
        idir = 1
        jd = 0
    elif idir == 1 and jd == 0:
        idir = 0
        jd = -1
    elif idir == 0 and jd == -1:
        idir = -1
        jd = 0
    else:
        idir = 0
        jd = 1
    return [idir, jd]

loop = int(input())

for tc in range(loop):
    size = int(input())

    board = [[0 for _ in range(size)] for _ in range(size)]
    # visit = [[False for _ in range(size)] for _ in range(size)]

    direction = 'l'
    num = 1
    i = 0
    j = 0

    idir = 0
    jdir = 1
    while num <= size ** 2:
        board[i][j] = num
        num += 1
        if i + idir == size or j + jdir == size or i + idir == -1 or j + jdir == -1 or board[i + idir][j + jdir] != 0:
            idir, jdir = changeDir(idir, jdir)
        i += idir
        j += jdir

    print(f'#{tc+1}')
    for i in range(len(board)):
        print(' '.join(map(str, board[i])))