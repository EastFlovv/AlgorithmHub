def solution(n):
    
    arr = [0 for _ in range(100001)]
    
    arr[1] = 1
    
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    
    answer = arr[n]
    return answer % 1234567