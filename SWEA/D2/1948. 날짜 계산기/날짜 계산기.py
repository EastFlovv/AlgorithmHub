from functools import reduce

# 1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31

loop = int(input().strip())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(loop):
    month_1, day_1, month_2, day_2 = map(int, input().strip().split(' '))

    # 메모리 초과 
    # ans = (reduce(lambda acc, val: acc + val, days[0: month_2 - 1]) + day_2) - (reduce(lambda acc, val: acc + val, days[0: month_1 - 1]) + day_1) + 1
    ans = (sum(days[0:month_2 - 1]) + day_2) - (sum(days[0:month_1 - 1]) + day_1) + 1

    print(f'#{tc+1} {ans}')