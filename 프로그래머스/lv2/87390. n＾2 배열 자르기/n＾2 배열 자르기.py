def solution(n, left, right):
    
    answer = []
    
    for x in range(left, right+1):
        val = x // n
        rest = x % n
        
        if val >= rest:
            answer.append(val + 1)
        else:
            answer.append(rest + 1)
    
    return answer


# n의 갯수만큼 나눈다?
# left가 2 인 경우
# left와 right를 이용하여.... 값을 구한다?
# 2의 경우
# 7 % n(4) = 1 // 3 => 4

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 % 4
# 0 0 0 0 1 1 1 1 2 2 2  2  3  3  3  3  몫 => 몫이 나머지보다 크거나 같을 경우... 몫 + 1이 값이다
# 0 1 2 3 0 1 2 3 0 1 2  3  0  1  2  3  나머지 => 나머지가 몫보다 크다면... 나머지 + 1의 값을 갖는다
# 1 2 3 4 2 2 3 4 3 3 3  4  4  4  4  4

# 1 2 3 4
# 2 2 3 4
# 3 3 3 4
# 4 4 4 4