loop = int(input())

for tc in range(loop):
    input()
    list1 = list(map(int, input().split(' ')))
    list2 = list(map(int, input().split(' ')))

    if len(list1) > len(list2):
        list1, list2 = list2, list1

    innerLoop = len(list2) - len(list1) + 1

    ans = 0

    for i in range(innerLoop):
        curMax = 0
        for j in range(len(list1)):
            curMax += list1[j] * list2[j + i]
        ans = max(curMax, ans)

    print(f'#{tc+1} {ans}')