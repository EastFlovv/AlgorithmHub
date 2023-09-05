def solution(s):
    
# 2 1 3 4
# 2 1 3 4
# 즉 1개인것 부터 구해서 해야 한다...
# s의 길이는 1백만 이므로 반복문 1회에 끝내야함
# 즉 나온 횟수가 중요하다
# 나온 횟수가 적은것 부터 끝에 위치함...
# s는 문자열이다...

    braket_off = list(map(int, (s.replace('{', '')).replace('}', '').split(',')))
    # print(braket_off)
    
    num_dict = {}
    
    for num in braket_off:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    answer = [0 for _ in range(len(num_dict))]
    
    for key in num_dict.keys():
        answer[len(answer) - num_dict[key]] = key
    
    return answer