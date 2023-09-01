def is_meet(man1, man2):
    if abs(man1 - man2) == 1 and man1 // 2 != man2 // 2:
        return False
    return True

def make_even(man):
    if man % 2 == 1:
        return True
    else:
        return False

def solution(n,a,b):
    
    ans = 1
    
    man1 = a
    man2 = b
    
    while(is_meet(man1, man2)):
        if make_even(man1):
            man1 += 1
        if make_even(man2):
            man2 += 1
            
        man1 /= 2
        man2 /= 2
        ans += 1
    
    # answer = 0
    return ans