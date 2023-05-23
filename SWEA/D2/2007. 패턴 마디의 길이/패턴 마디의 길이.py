loop = int(input())

for tc in range(loop):
    input_str = input()

    for i in range(10):
        slide = i + 1
        tmp1 = input_str[0:slide]
        tmp2 = input_str[slide: slide*2]
        # print(f'{tmp1} | {tmp2}')
        if tmp1 == tmp2:
            print(f'#{tc+1} {slide}')
            break

