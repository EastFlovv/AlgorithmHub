import heapq

def mix(food1, food2):
    return food1 + food2 * 2

def solution(scoville, K):
    answer = 0
    
    foods = []
    
    for food in scoville:
        heapq.heappush(foods, food)
        
    while(True):
        if foods[0] >= K:
            break
        
        if len(foods) == 1:
            answer = -1
            break
            
        food1 = heapq.heappop(foods)
        food2 = heapq.heappop(foods)
        
        new_food = mix(food1, food2)
        
        heapq.heappush(foods, new_food)
        
        answer += 1
        
        
    return answer