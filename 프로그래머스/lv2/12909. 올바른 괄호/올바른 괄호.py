def solution(s):
    
    stack = []
    top = -1
    
    for braket in s:
        if braket == '(':
            stack.append('(')
            top += 1
        elif braket == ')' and top == -1:
            return False
        elif braket == ')' and stack[top] == ')':
            return False
        else:
            stack.pop(top)
            top -= 1
    
    return True if top == -1 else False
    
    
        
#     return True