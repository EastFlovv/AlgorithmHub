# n미터의 벽을 1미터씩 n개의 섹션으로 나눈다...
# 번호는 1~n
# 롤러의 길이는 m
# 페인트 칠 규칙
# 롤러가 벽에서 나가면 안됨
# 구역의 일부분만 포함되도록 칠하면 안됨??????? -> 즉 1번 구역의 일부를 칠하는것은 안됨 1번에 손대면 1번을 모두 채워야 함
# 페인트 칠을 최소화 할것

# 8미터 벽
# 4미터 자리 롤러
# 2,3,6번에 칠하기로 했다...

# 2에서 칠하면
# 2,3,4,5 or 1,2,3,4 + 6 -> 2회
# 5미터에 4미터 롤러 1,3번 -> 1회

# 아마도 슬라이딩 윈도우에 해당할것 같음...
def solution(n, m, section):
    
    cur_brush_end = -1
    cur_brush = -1
    ans = 0
    
    for pos in section:
#         현재 위치가 이미 칠해진 부분이면 continue
        if pos < cur_brush_end:
            continue
#         아직 안칠했으면 현재 위치로부터 m길이만큼 칠하고 ans+1
        elif pos > cur_brush:
            cur_brush = pos
            cur_brush_end = pos + m
            ans += 1
    
    # answer = 0
    return ans