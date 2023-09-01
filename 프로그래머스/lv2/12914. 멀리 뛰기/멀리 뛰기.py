def solution(n):
    arr = [0 for _ in range(2000)]
    arr[0] = 1
    arr[1] = 2
    
    for i in range(2, len(arr)):
        arr[i] = (arr[i-1] + arr[i-2]) % 1234567
    answer = arr[n-1] 
    return answer