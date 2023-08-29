def solution(s):
    answer = -1

    # # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
    
#     스택 문제
    
    stack = []
    top = -1
    
    for x in s:
        if top == -1:
            stack.append(x)
            top += 1
        else:
            if stack[top] == x:
                stack.pop()
                top -= 1
            else:
                stack.append(x)
                top += 1
                
    print(stack)

    if len(stack) > 0:
        return 0
    else:
        return 1