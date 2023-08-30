def solution(n, words):
#     n번째 사람이 ㅌ번쨰 말 할때 틀린다
    answer = [0, 0]
    
#     마지막, 1,2,3,4....
    mans = [0 for _ in range(n)]
    used = []
    last_spell = ''
    
    seq = 0
    
    for word in words:
        seq += 1
#         현재 사람에게 차례 + 1 -> 자신이 몇번 말했는지
        mans[seq % n] += 1
    
        if last_spell == '':
            last_spell = word[len(word) - 1]
            used.append(word)
            continue
        
#         사용된 단어인 경우
        if word in used:
            # print(f'same word! word = {word}')
            answer = [n if seq % n == 0 else seq % n, mans[seq % n]]
            break
        else:
#             마지막 단어 설정
#             유효성 검사 통과
            if last_spell == word[0]:
                last_spell = word[len(word) - 1]
            else:
                # print(f'wrong word! last_spell = {last_spell}, word = {word}')
                answer = [n if seq % n == 0 else seq % n, mans[seq % n]]
                break
                
        used.append(word)

    return answer