def solution(land):
    # answer = 0
    
    before = [0 for _ in land[0]]
    
    # print(before)
    
    for i in range(len(land)):
        # print(f'bef: {before}')
        # print(f'cur: {land[i]}')
        for j in range(len(land[i])):
            tmp_max = 0
            for k in range(len(before)):
                if k == j:
                    continue
                
                if before[k] + land[i][j] >= tmp_max:
                    # print(f'land[{i}][{j}] = {land[i][j]}, before[{k}] = {before[k]}')
                    tmp_max = before[k] + land[i][j]
                    
            land[i][j] = tmp_max
        # print(f'aft: {land[i]}')
        before = land[i]
    
    # print(land)
    
    return max(land[-1])