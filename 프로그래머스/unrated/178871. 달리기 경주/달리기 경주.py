def solution(players, callings):
    name_rank = {}
    rank_name = {}
    
#     딕셔너리에 저장
    for i in range(len(players)):
        name_rank[players[i]] = i
        rank_name[i] = players[i]
    
#     승자의 이름만 안다
    for call in callings:
#         승자의 랭킹 추출
        winner_rank = name_rank[call]
#         패자의 랭킹 추출
        loser_rank = winner_rank - 1
#         패자의 이름 추출
        loser = rank_name[loser_rank]
    
#         두 사람의 랭킹을 변경하되 두 딕셔너리에서 모두 변경
        name_rank[call], name_rank[loser] = name_rank[loser], name_rank[call]
        rank_name[winner_rank], rank_name[loser_rank] = rank_name[loser_rank], rank_name[winner_rank]
        
    answer = ['' for _ in range(len(players))]
#     랭크가 키인 딕셔너리에서 추출
    for rank in rank_name.keys():
#         배열의 각 위치에 이름 삽입
        answer[rank] = rank_name[rank]
    
    return answer
    

        
#     실패코드
#     for player in callings:
#         winner = players.index(player)
#         loser = winner - 1
#         swap(players, winner, loser)
        
#     return players
    


# 배열의 실제 내용을 바꿔주는 함수
# def swap(players, winner, loser):
#     players[winner], players[loser] = players[loser], players[winner]
    

# 시간 초과
# 전체 유저의 등수를 직접 접근해야한다
# 딕셔너리 사용


