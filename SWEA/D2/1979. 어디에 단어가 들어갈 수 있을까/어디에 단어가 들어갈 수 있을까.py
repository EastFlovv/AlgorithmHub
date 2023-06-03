loop = int(input())

for tc in range(loop):
    size, word = map(int, input().strip().split(' '))

    board = [[] for _ in range(size)]
    for i in range(size):
        board[i] = list(map(int, input().strip().split(' ')))

    # init fin

    # 각 이전 값 기억을 위한 변수
    left = 0
    top = 0

    # 정답
    ans = 0

    for i in range(size):
        for j in range(size):
            # 각 이전 값을 기억
            if i != 0:
                top = board[i-1][j]
            else:
                top = 0
            if j != 0:
                left = board[i][j-1]
            else:
                left = 0

            # 이전 값이 막혔을 때
            if board[i][j]:
                if not left:
                    cnt = 0
                    pos = j
                    # 끝까지 검사
                    while pos < size:
                        # 1이면 cnt 증가
                        if board[i][pos]:
                            pos += 1
                            cnt += 1
                        # 0이 나오면 멈춤
                        else:
                            break
                    # cnt와 word가 같으면 답을 추가
                    if cnt == word:
                        ans += 1

                if not top:
                    cnt = 0
                    pos = i
                    # 끝까지 검사
                    while pos < size:
                        # 1이면 cnt 증가
                        if board[pos][j]:
                            pos += 1
                            cnt += 1
                        # 0이 나오면 멈춤
                        else:
                            break
                    # cnt와 word가 같으면 답을 추가
                    if cnt == word:
                        ans += 1

    print(f'#{tc+1} {ans}')