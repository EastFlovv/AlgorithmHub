# import math

def solution(triangle):
    # max_val = triangle[0][0]
    
    for i in range(len(triangle)):
        if i == 0:
            continue
        for j in range(len(triangle[i])):
            cur_val = triangle[i][j]
            
            if j == 0:
                cur_val = max(triangle[i-1][j] + cur_val, cur_val)
            elif j == i:
                cur_val = max(triangle[i-1][j-1] + cur_val, cur_val)
            else:
                cur_val = max(triangle[i-1][j-1] + cur_val, triangle[i-1][j] + cur_val)
            
            triangle[i][j] = cur_val
            
            # max_val = max(max_val, cur_val)
    
    return max(triangle[len(triangle) - 1])