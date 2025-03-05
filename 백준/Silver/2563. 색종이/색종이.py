N = int(input())

confetti = []
drawing_paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    confetti.append(list(map(int, input().split())))

for i in confetti:
    for width_tile in range(i[0] - 1, min(i[0] + 9, 99)):
        for height_tile in range(i[1] - 1, min(i[1] + 9, 99)):
            drawing_paper[width_tile][height_tile] = drawing_paper[width_tile][height_tile] + 1

result = 0
for i in range(100):
    for j in range(100):
        if(drawing_paper[i][j] > 0):
            result = result + 1

print(result)