import heapq

def solution(k, tangerine):
    
# 각 귤의 사이즈를 잰 뒤
# 각 귤 사이즈가 가장 많은 놈부터 뺀다
# 그렇다면...
# 배열에 튜플 형태로 담아서
# 저장한다?
# 우선 순위 큐를 사용할것

    packing_left = k

    hip = []
    
    tang_amount = {}
    
    ans = 0
    
#     갯수를 세어서 딕셔너리에 저장
    for x in tangerine:
        if x not in tang_amount:
            tang_amount[x] = 1
        else:
            tang_amount[x] += 1
    
#     최대 힙
    for key in tang_amount.keys():
        heapq.heappush(hip, (tang_amount[key] * -1, key))
    
    while(packing_left > 0):
        amount, tang = heapq.heappop(hip)
        packing_left -= (amount * -1)
        ans += 1
    
    # answer = 0
    return ans