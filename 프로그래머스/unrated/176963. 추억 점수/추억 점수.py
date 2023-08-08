def solution(name, yearning, photo):
    
# 사람의 수 3 ~ 100
# 이름은 name 배열
# 그리움 점수는 yearning 배열
# photo는 사진들의 이름 담긴 이차원 배열
# 순서대로 배열에 담아 return할것

# 사진의 길이는 3~100
# 100 * 100 => 10,000

#     딕셔너리로 저장
    yearning_dict = {}
    for i in range(len(name)):
#         없을 수도 있다는 조건을 통과하지 않아서 큰일날뻔...
        if i <= len(yearning):
            yearning_dict[name[i]] = yearning[i]
        else:
            yearning_dict[name[i]] = 0
    
#     정답 배열
    answer = []
#     이중 for문 사용
    for mans in photo:
        value = 0
#         그리움 점수를 딕셔너리에서 찾아서 더한다
        for man in mans:
            if man in yearning_dict:
                value += yearning_dict[man]
            
        answer.append(value)
    
    return answer