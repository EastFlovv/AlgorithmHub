# 재귀를 통해 단어를 만들고 배열에 넣는다
def make_words(words, pos, spells, word):
#     종료 조건
    if pos == 5:
        tmp = ''.join(word)
        if tmp not in words:
            words.append(tmp)
        return
    
    for spell in spells:
        word[pos] = spell
        make_words(words, pos+1, spells, word)
    


def solution(word):
    
    spells = ['', 'A', 'E', 'I', 'O', 'U']
    words = []
    tmp_word = ['', '', '', '', '']
    
    make_words(words, 0, spells, tmp_word)
    words.sort()
    
    # print(words.index(word))
    
    answer = words.index(word)
    return answer


# 배열 ['', '', '', '', ''] 에서 출발 하여 앞부터 하나씩 채운다
# 논리 앞부터 검사하여 빈 공간이 있는지 체크한다
# 빈 공간이 있는 경우 A를 넣는다
# 




# case 2
# 재귀 반복문을 사용하여 모든 단어를 만들고 배열에 넣는다
# 배열을 정렬한다
# index를 찾아낸다