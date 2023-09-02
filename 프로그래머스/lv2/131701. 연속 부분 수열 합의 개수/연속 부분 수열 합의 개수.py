def solution(elements):
    
# 길이가 1일때 -> 자기 자신을 삽입
# 길이가 2일떄 자기 자신과 자신에게서 + 1된 위치의 값을 더함
# 길이가 3일때 2의 자신 위치 값과 자신에게서 + 2된 위치의 값을 더함

    value_set = set()
    
    value_board = [[0 for _ in range(len(elements))] for _ in range(len(elements))]
    
    for slide in range(len(elements) - 1):
        for idx in range(len(elements)):
            if slide == 0:
                value_board[slide][idx] = elements[idx]
            # elif slide + 1 == len(elements):
            else:
                value_board[slide][idx] = value_board[slide - 1][idx] + value_board[0][(idx + slide) % len(elements)]
            value_set.add(value_board[slide][idx])
    
    
    value_set.add(sum(elements))
    # print(value_board)
    # print(value_set)
    # print(len(value_set))
    
    answer = len(value_set)
    return answer