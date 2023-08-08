# 만약 이 배열을... 우선순위 큐로 만든다면?

# 1234
# 34567
# 45
# 45678
# 56789 10 11 12
# 10 11 12 13 14
# 11 12 13

# 즉 최소 2개 구간이 겹쳐야 발사할 수 있다

# 1234
# 34567

# 45
# 45678

# 56789 10 11 12
# 10 11 12 13 14
# 11 12 13

# 시작 값 1
# 끝값 4

# 두 수가 겹치면
# 시작값 3
# 끝값 4 (겹치는 범위 내에서)

# 두 수가 겹치지 않으므로
# 시작 값 4
# 끝값 5
# 다음것도 포함

# 시 5 끝 12
# 시 10 끝 12
# 시 11 끝 12

# 즉 상대의 시작값 - 내 끝값의 차이가 0보다 크다면...

import heapq

def solution(targets):
    
    hip = []
    for target in targets:
        heapq.heappush(hip, target)
    
    
    ans = 1
    start, end = heapq.heappop(hip)
    while(len(hip) > 0):
        atk_start, atk_end = heapq.heappop(hip)
        
        if end - atk_start > 0:
            start = atk_start
            end = atk_end if atk_end < end else end
        else:
            start = atk_start
            end = atk_end
            ans += 1
    
    # answer = 0
    return ans