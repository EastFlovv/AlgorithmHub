def solution(s):
    
    strs = s.split(' ')
    for i in range(len(strs)):
        strs[i] = strs[i].capitalize()

    
    answer = ' '.join(strs)
    return answer