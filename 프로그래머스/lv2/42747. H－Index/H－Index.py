def solution(citations):
    
#     발표한 논문의 수만큼 h-index를 가질 수 있다
#     그렇다면... 논문을 정렬한 후
#     현재 인덱스(+1)보다 크거나 
# 0 1 3 5 6
# 0 1 2 3 4 i
# 1 2 3 4 5 len

    citations.sort()
    
    ans = 0
    
    if citations[0] >= len(citations):
        ans = len(citations)
    else:
        for i in range(1, len(citations)):
            if citations[len(citations) - i] >= i:
                ans = i

    return ans