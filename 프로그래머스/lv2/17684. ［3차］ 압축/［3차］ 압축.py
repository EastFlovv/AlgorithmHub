import string

def solution(msg):
    
    words = list(string.ascii_uppercase)
    
    answer = []
    
    # for i in range(len(msg)):
    i = 0
    while(i < len(msg)):
        word = msg[i]
        prev = word
        # print(f'start is {word}')
        idx = i
        
        while(word in words):
            idx += 1
            prev = word
            if idx == len(msg):
                break
            word += msg[idx]
        
        # print(prev, word, word in words)
        answer.append(words.index(prev) + 1)
        if word not in words:
            words.append(word)
        
        
        
        # print(words)
        
        i += len(prev)
        
        
        # print(answer)
        # print(words)
        
        
    
    
    return answer


# 현재 입력 -> 있는지 여부
# 즉 현재 입력을 찾기 위해선
# 한 글자 확인후... -> 한 글자를 더 붙여서 그 글자가 있는지 확인 해야 함
# 없을 때 까지 확인한 후
# 있는것 + 없는것 더해서 다음 사전으로 더함
# 현재까지 있는것을 정답에 추가

# kakao의 경우
# k -> ka 추가
# a -> ak 추가
# k -> ka -> kao 추가
# ka를 했으므로 a는 패스
# o -> 끝