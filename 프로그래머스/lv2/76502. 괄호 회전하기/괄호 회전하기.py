def solution(s):
    
    open_braket = ['(', '{', '[']
    ans = 0
#     시작 인덱스
    for i in range(len(s)):
        
        stack = []
        
        for j in range(len(s)):
            idx = (i + j) % len(s)
            if len(stack) == 0 or s[idx] in open_braket:
                stack.append(s[idx])
            else:
                if s[idx] == ')' and stack[len(stack) - 1] == '(':
                    stack.pop()
                if s[idx] == '}' and stack[len(stack) - 1] == '{':
                    stack.pop()
                if s[idx] == ']' and stack[len(stack) - 1] == '[':
                    stack.pop()
        if len(stack) == 0:
            ans += 1
    # print(ans)
    
    # answer = -1
    return ans