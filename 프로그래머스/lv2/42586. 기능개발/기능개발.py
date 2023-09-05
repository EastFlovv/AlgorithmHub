import math

def solution(progresses, speeds):
    
#     7초 3초 45초
# c_time = 7
# 7, 3 -> 2
# c_time = 45
# 45 -> 1
# 2 1

    left_time = [0 for _ in range(len(speeds))]

    for i in range(len(speeds)):
        left_time[i] = math.ceil((100 - progresses[i]) / speeds[i])
    
    
    
    idx = 0
    c_time = left_time[0]
    tmp = 0
    answer = []
    
    while(idx < len(left_time)):
        if c_time >= left_time[idx]:
            tmp += 1
        else:
            answer.append(tmp)
            c_time = left_time[idx]
            tmp = 1
        idx += 1
        
    answer.append(tmp)
    
    return answer