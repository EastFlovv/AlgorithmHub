import heapq

def solution(n, works):
    answer = 0
    
# 우선 순위 큐를 사용

    hip = []
    for x in works:
        heapq.heappush(hip, x * -1)
    
    
    for i in range(n):
        work = heapq.heappop(hip)
        work += 1
        heapq.heappush(hip, work)
    
    for work in hip:
        if work < 0:
            answer += work * work
        
    return answer



# 퇴근까지 4시간 -> 즉 4만큼의 일을 줄일 수 있다
# 현재 업무는 4 3 3만큼 남음
# 야근 피로도는... 0 + 9 + 9
# 16 + 4 | 4 + 4 + 4 = 12
# 일종의 평탄화 작업 but... 1의 경우에는 피로도가 1이기 때문에 1일 때는 0으로 줄이지 않는다
# 즉 제곱이 피로도 이므로 평탄화 작업을 통해 값을 줄이되 1까지만 줄이고 그 이후에 0으로 줄임

