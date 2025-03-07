N = int(input())

S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

min_difference = 1e9

visited = [False] * N

def backTracking(depth):
    if len(visited) == depth:
        start_team_score = 0
        link_team_score = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_team_score = start_team_score + S[i][j]
                elif not visited[i] and not visited[j]:
                    link_team_score = link_team_score + S[i][j]
        global min_difference
        min_difference = min(min_difference, abs(start_team_score - link_team_score))
        return
    
    visited[depth] = True
    backTracking(depth + 1)
    visited[depth] = False
    backTracking(depth + 1)
    return

backTracking(0)
print(min_difference)
