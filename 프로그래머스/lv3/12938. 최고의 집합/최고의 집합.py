def solution(n, s):
    
    answer = []
    
    left_val = s
    left_slut = n
    
    for i in range(n):
        val, remain = divmod(left_val, left_slut)
        if val == 0:
            answer = [-1]
            return answer
        else:
            answer.append(val)
            left_val = left_val - val
            left_slut -= 1
    
    
    # not_answer = [-1]
    # answer = []
    
#     val, remain = divmod(s, n)
    
#     if val > 0:
#         answer = [val for _ in range(n)]
#         idx = n-1
#         while(remain > 0):
#             answer[idx] += 1
#             remain -= 1
#     else:
#         answer = [-1]
    
    # print(answer)
    
    return answer



# 18 . 5
# 3 - 15 - 4
# 3 3 - 12 - 3
# 3 3 4 - 8 - 2
# 3 3 4 4 4

