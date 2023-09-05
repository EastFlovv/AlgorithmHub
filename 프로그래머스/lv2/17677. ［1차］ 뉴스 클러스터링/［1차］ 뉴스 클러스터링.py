import math

def len_intersection(s1, s2):
    result = []
    for x in s2:
        if x in s1:
            s1.remove(x)
            result.append(x)
    
    # print(result)
    return len(result)

def len_union(s1, s2):
    # result = []
    
    # print('sort')
    # s1.sort()
    # s2.sort()
    # print(s1)
    # print(s2)
    
    k = 0
    
    for x in s1:
        if x in s2:
            k += 1
            s2.remove(x)
    
    # print(f'union result is.... {len(s1) - k + len(s2) + k}')
    
    # print(s1, s2, result)
    return len(s1) - k + len(s2) + k

def solution(str1, str2):
    
    tmp_s1 = str1.lower()
    tmp_s2 = str2.lower()
    
    s1 = []
    s2 = []
    
    for i in range(len(tmp_s1) - 1):
        if tmp_s1[i].isalpha() and tmp_s1[i+1].isalpha():
            s1.append(tmp_s1[i] + tmp_s1[i+1])
            
    for i in range(len(tmp_s2) - 1):
        if tmp_s2[i].isalpha() and tmp_s2[i+1].isalpha():
            s2.append(tmp_s2[i] + tmp_s2[i+1])
    
    # print(s1)
    # print(s2)
    
    answer = 0
    
#     # print(len_union(s1.copy(), s2.copy()))
    
    union = len_union(s1.copy(), s2.copy())
    intersection = len_intersection(s1.copy(), s2.copy())
    
    # print(union, intersection)
    
    answer = 65536 if intersection == union else math.floor(intersection / union * 65536)
#     answer = int(intersection / union * 65536 // 1)
    return answer