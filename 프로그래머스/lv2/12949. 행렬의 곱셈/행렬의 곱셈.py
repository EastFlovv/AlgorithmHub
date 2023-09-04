def solution(arr1, arr2):
    
# 행렬곱
# l * x | x * m = l * m
# 
# 1 4   3 3     1....4 arr의 ver | arr2의 hor
# 3 2   3 3     
# 4 1           

# [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
# [[5, 4], [2, 4], [3, 1]]

# 2 3 2         5 4
# 4 2 4         2 4
# 3 1 4         3 1

# -> 10 6 6 -> 22
                    
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            # print(f'idx {i}, {j}')
#             arr1에선 행을 탐색
            
            # print(f' >>>>>>>>>> {len(arr1)}, {len(arr2)}')
    
            for a1 in range(len(arr1[0])):
#               arr2에선 열을 탐색
                for a2 in range(len(arr2)):
                    
                    # print(f'::::::::::: {a1}, {a2}')
        
#                     같은 인덱스일때만 사용
                    if a1 == a2:
                        answer[i][j] += arr1[i][a1] * arr2[a2][j]
                        # print(f'{arr1[i][a1]} * {arr2[a2][j]} = {arr1[i][a1] * arr2[a2][j]}')
    
    # print(answer)
    return answer