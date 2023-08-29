def dec_to_reverse_bin(num):
    cur = num
    
    bits = []
    pos = 1048576
    
    for i in range(21):
        if cur - pos >= 0:
            bits.append(True)
            cur -= pos
        else:
            bits.append(False)
        
        pos /= 2

    return bits[::-1]

def add_one(bits):
    cnt = 0
    flag = True
    
    for i in range(len(bits)):
        if not flag:
            break
        else:
            if bits[i]:
                bits[i] = False
                cnt -= 1
            else:
                bits[i] = True
                flag = False
                cnt += 1
    return cnt

def solution(n):
    
    rb = dec_to_reverse_bin(n)
    cnt = rb.count(True)
    
    ans = n + 1
    nrb = dec_to_reverse_bin(ans)
    ncnt = nrb.count(True)
    
    # print(rb)
    # print(nrb)
    # print(f'cnt = {cnt}, ncnt = {ncnt}')
    
    
    while(cnt != ncnt):
        ans += 1
        ncnt += add_one(nrb)
        # print(f'cnt = {cnt}, ncnt = {ncnt}')
    
    # answer = 0
    return ans