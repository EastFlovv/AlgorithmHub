# n진수 변환
def decimal_to_binary(num, flag):
    if num == 0:
        return '0'
    
    over_ten = ['A', 'B', 'C', 'D', 'E', 'F']
    
    cur_num = num
    
    ans = []
    
    while(cur_num > 0):
        val, remain = divmod(cur_num, flag)
        cur_num = val
        
        if remain >= 10:
            ans.append(over_ten[remain-10])
        else:
            ans.append(str(remain))
    
    return ''.join(ans[::-1])

# 만약 2진수 10이 온다면...
# 1010 -> 이중 자신의 차례에 사용하는 것들을 리스트업 하여 원본에 더할것 
# -> 원본의 길이가 최대치 이상이면 잘라서 반환 혹은 원본의 길이가 최대치에 달하면 그대로 리턴

# 입력된 binary, 정답의 최대길이, 내 순서, 현재 순서, 전체 인원, 정답 배열
def make_answer(binary, max_len, my_seq, cur_seq, total_men, answer):
    # print(f'make_answer :::: binary = {binary}')
    seq = cur_seq
    
    for x in binary:
        
        if seq == my_seq:
            answer.append(x)
        
        seq += 1
        if seq > total_men:
            seq = 1
        
        if len(answer) == max_len:
            return seq
        
    return seq

def solution(n, t, m, p):
    
    answer = []
    
    num = 0
    seq = 1
    while(len(answer) < t):
        
        binary = decimal_to_binary(num, n)
        # print(f'')
        # print(f'cur_num = {num}, binary = {binary}')
        seq = make_answer(binary, t, p, seq, m, answer)
        # print(f'my_seq = {p}, cur_seq = {seq}, cur_answer = {"".join(answer)}')
        num += 1
    
    # print(''.join(answer))
    
    # answer = ''
    return ''.join(answer)