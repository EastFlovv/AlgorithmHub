def is_vip(shop_list):
    # print(shop_list)
    for key in shop_list.keys():
        if shop_list[key] > 0:
            return False
    return True

def solution(want, number, discount):
    
# want는 원하는 항목
# number는 want의 인덱스에 맞추어 원하는 항목의 갯수를 말함
# discount는 매일 할인하는 항목을 나열한다

    shop_list = {}
    ans = 0

    for i in range(len(want)):
        shop_list[want[i]] = number[i]
#     init

    for i in range(10):
        if discount[i] in shop_list:
                shop_list[discount[i]] -= 1
        
    if is_vip(shop_list):
        ans += 1
    
    for i in range(10, len(discount)):
        if discount[i - 10] in shop_list:
                shop_list[discount[i - 10]] += 1

        if discount[i] in shop_list:
                shop_list[discount[i]] -= 1
                
        if is_vip(shop_list):
            ans += 1
    
    return ans