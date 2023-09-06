def dfs(numbers, target, idx, cur_val):
    # print(f'idx = {idx}, cur_val = {cur_val}')
#     end condition
    if idx == len(numbers):
        if cur_val == target:
            return 1
        else:
            return 0
    
    
    ans = 0
#     cur_val 변경
    p_val = cur_val + numbers[idx]
    m_val = cur_val - numbers[idx]
    idx += 1
#     재귀
    ans += dfs(numbers, target, idx, p_val)
    ans += dfs(numbers, target, idx, m_val)
#     인덱스 낮추기
    idx -= 1
    
    return ans
    
    
    


def solution(numbers, target):
    
    answer = dfs(numbers, target, 0, 0)
    
    # answer = 0
    return answer