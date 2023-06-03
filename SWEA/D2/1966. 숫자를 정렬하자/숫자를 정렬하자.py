loop = int(input())

for tc in range(loop):
    size = int(input().strip())

    intArr = list(map(int, input().strip().split(' ')))
    intArr.sort()
    intArr = list(map(str, intArr))
    print(f'#{tc+1} {" ".join(intArr)}')
