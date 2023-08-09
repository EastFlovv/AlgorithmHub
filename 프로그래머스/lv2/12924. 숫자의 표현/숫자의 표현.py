def solution(n):
    
    start = 1
    end = 2
    
    cur_val = start + end
    ans = 0
    
    if n == 1:
        return 1
    
    while(start <= n):
        # print(f'loop start:::: {start} {end} {cur_val} {ans}')
#       합이 맞으면 답을 늘리고 start를 빼고 다음 수로 넘김
        if cur_val == n:
            ans += 1
            cur_val -= start
            start += 1
#       현재까지 합이 n보다 작으면 end를 늘리고 더함, 단 end는 n을 넘을 수 없음
        elif cur_val < n and end <= n:
            end += 1
            cur_val += end
#       현재까지 합이 n보다 크면 start를 빼고 다음 수로 넘어감
        elif cur_val > n:
            cur_val -= start
            start += 1
            
        # print(f'start = {start}, end = {end}, cur_val = {cur_val}, ans = {ans}')
        
    return ans