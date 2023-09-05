def recursive_comb(arr, clothes, left):
    
    val = 0
    if left == 0:
        # print(arr)
        val = 1
        for i in range(len(arr)):
            if arr[i]:
                val *= clothes[i]
        return val
    
    for i in range(len(arr)):
        # print(f'recursive sequence >>> {i}')
        if arr.count(True) == 0:
            arr[i] = True
            left -= 1
            val += recursive_comb(arr, clothes,left)
            arr[i] = False
            left += 1
        
        elif not arr[i] and arr.index(True) > i:
            arr[i] = True
            left -= 1
            val += recursive_comb(arr, clothes,left)
            arr[i] = False
            left += 1
            
    return val

def solution(clothes):
    
# 옷을 입는데...
# 슬릇당 옷의 종류는 정해져 있다
# 옷을 입는 경우의 수를 출력

# 4 1 1 1의 경우
# 4개 -> 4 * 1 * 1 * 1 = 4
# 3개 -> 4 + 4 + 4 + 1 = 13
# 2개 -> 4 4 4 1 1 1 = 15
# 1개 -> 7 = 7

# 11 13 15 24 25 49?
# 3의 경우 4 - 1
# 2 1의 경우 = 3 * 2 - 1


# 옷을 입지 않는 경우의 수를 추가
# 5 2 2 2
# 5 * 2 * 2 * 2 = 8 * 5 = 40 - 1
    
# 의상의 종류는 몇개인지 알 수 없다
# 해시를 통해 의상의 수를 저장
# 해시의 크기를 통해 배열을 할당
# 각 배열에 의상의 종류를 집어 넣고...
# 슬라이드 윈도우 방식을 사용하여 의상의 조합수를 센다

    clothes_dict = {}

    for comb in clothes:
        wear = comb[0]
        kind = comb[1]
        
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 2
    
    clothes_arr = [0 for _ in range(len(clothes_dict))]
    # comb_arr = [False for _ in range(len(clothes_dict))]
    
    ans = 1
    for key in clothes_dict.keys():
        # clothes_arr[idx] = clothes_dict[key]
        ans *= clothes_dict[key]
    ans -= 1
        
        
        
        
        
        
    # ans = 0
    # for i in range(1, len(comb_arr)+1):
    #     print(i)
    #     ans += recursive_comb(comb_arr, clothes_arr, i)
    
    
    # print(ans)
    
# 2 1
# 3
# 
    
    
    
    
    # answer = 0
    return ans