def solution(cacheSize, cities):
    
# 자료구조...
# 정렬 사용?
# 리스트 내부의 정렬을 사용하기?

    cache = []
    ans = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        
        city = city.capitalize()
        
        # print(f'city = {city}')
#         먼저 시간을 계산
        if city in cache:
            ans += 1
#             자신을 빼고 넣음
            cache.remove(city)
            cache.append(city)
            
        else:
            ans += 5
#             없는것 넣을 때 공간이 남으면 그냥 넣고 아니면 앞부터 빼고 넣기
            if len(cache) == cacheSize:
                cache.pop(0)
            
            cache.append(city)
        
        # print(cache)
    
    # print(ans)
    
    # answer = 0
    return ans