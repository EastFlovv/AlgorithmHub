def solution(s):
    
    arr = list(s)
    loop = 0
    zero = 0
    
    while(len(arr) > 1):
        loop += 1
        cnt = arr.count('1')
        zero += len(arr) - cnt
        arr = list(str(bin(cnt)))[2:]
        
    answer = [loop, zero]
    return answer