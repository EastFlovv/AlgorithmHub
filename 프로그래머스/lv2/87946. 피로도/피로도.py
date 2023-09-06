def dfs(k, dungeons, visited):
    
    # print(f'visited = {visited}')
    
    val = 0
    
    for i in range(len(dungeons)):
        if visited[i]:
            continue
        
        dungeon = dungeons[i]
        # print(dungeon[0])
        if dungeon[0] > k:
            continue
            
#       던전 진입
        k -= dungeon[1]
        visited[i] = True
        
        val = max(val, dfs(k, dungeons, visited))
        k += dungeon[1]
        visited[i] = False
    
    val = max(val, visited.count(True))
    
    return val
    

def solution(k, dungeons):
    
# dfs

    visited = [False for _ in range(len(dungeons))]
    
    # print()
    
    
    
    answer = dfs(k, dungeons, visited)
    return answer