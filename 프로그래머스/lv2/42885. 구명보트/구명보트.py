def solution(people, limit):
    
    people.sort()
    people.reverse()
    
    ans = 0
    
    left = 0
    right = len(people) - 1
    
    while(left <= right):
        cur = limit
        
        ans += 1
        
        cur -= people[left]
        
        # print(f'{people[left]} escape')
        
        if people[right] <= cur:
            # print(f'{people[right]} escape')
            right -= 1
        left += 1
        
        # print('---------------------')
        
            
    return ans