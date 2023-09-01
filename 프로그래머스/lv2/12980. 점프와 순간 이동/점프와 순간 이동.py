def solution(n):
    val = n
    ans = 0
    
    while(val > 0):
        
        if val % 2 == 1:
            val -= 1
            ans += 1
        else:
            val /= 2
            

    return ans