def solution(brown, yellow):
    
    ver_hor_sum = (brown - 4) / 2
    
    ver = 1
    
    ans_v = 2
    ans_h = 2
    
    while(ver <= (ver_hor_sum/2)):
        hor = ver_hor_sum - ver
        
        if ver * hor == yellow:
            ans_v += ver
            ans_h += hor
            break
        ver += 1
    
    
    answer = [ans_h, ans_v]
    return answer