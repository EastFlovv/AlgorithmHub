loop = int(input())

for tc in range(loop):
    orders = int(input())

    spd = 0
    dis = 0

    for _ in range(orders):
        str = input().strip()



        if str != '0':
            order, amount = map(int, str.split(' '))

            if order == 1:
                spd += amount
            else:
                spd = 0 if spd - amount < 0 else spd - amount

        dis += spd
    print(f'#{tc+1} {dis}')
