def solution(priorities, location):
    
# 실제로 구현하기?
# queue를 그대로 구현하기...
# 해당 배열을 인덱스와 함께 튜플 형태로 저장
# queue를 이용하여 해당 인덱스가 빠질 때 까지 사용
# 그렇다면...
# max값을 구하여..? 배열을 만든다?
    
    nums = [0 for i in range(101)]
    
    que = []
    for i in range(len(priorities)):
        que.append((priorities[i], i))
        nums[priorities[i]] += 1
        
    answer = 0
        
    for num in range(100, 0, -1):
        flag = False
        while(nums[num] > 0):
            p, idx = que.pop(0)
            # print(f'{p}, {idx}')
            
            if p == num:
                # print(f'idx {idx} remove')
                nums[num] -= 1
                answer += 1
                
                if idx == location:
                    flag = True
                
            else:
                que.append((p, idx))
            
            if flag:
                break
        if flag:
            break
    
    return answer