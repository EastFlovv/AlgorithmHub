import math
import heapq

def solution(fees, records):
    
    basic_time, basic_fee, extra_time, extra_fee = fees
    
    time_info = {}
    fee_info = {}
    
    for record in records:
        time, number, state = record.split(' ')
        
        hour, minute = time.split(':')
        total_minute = int(hour) * 60 + int(minute)
        
        if state == 'IN':
            time_info[int(number)] = total_minute
            if int(number) not in fee_info:
                fee_info[int(number)] = 0
        else:
            
            # print(f'num = {number}, in = {time_info[int(number)]}, out = {total_minute}, current = {total_minute - time_info[int(number)]}')
            
            fee_info[int(number)] += total_minute - time_info[int(number)]
            # print(fee_info)
            time_info[int(number)] = -1
            
    for number in time_info.keys():
        if time_info[number] >= 0:
            # print(f'{number} not exit 23:59 out')
            fee_info[number] += 23 * 60 + 59 - time_info[number]
            time_info[number] = 0

    heap = []
    
    for number in fee_info.keys():
        data = (number, fee_info[number])
        heapq.heappush(heap, data)
    
    answer = []
    
    print(fee_info)
    
    while(len(heap) > 0):
        number, fee = heapq.heappop(heap)
        ans = 0
        extra_fee_time = fee - basic_time
        if extra_fee_time > 0:
            ans += basic_fee + math.ceil(extra_fee_time/extra_time) * extra_fee
        else:
            ans = basic_fee
            
        answer.append(ans)
    
    return answer