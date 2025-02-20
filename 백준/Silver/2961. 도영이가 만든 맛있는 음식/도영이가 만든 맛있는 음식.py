import sys
from itertools import combinations

N = int(input())

ingredients = []

for i in range(N):
    ingredients.append(list(map(int, input().split())))

result = sys.maxsize
for i in range(1, N + 1):
    subsets = list(combinations(ingredients, i))

    for subset in subsets:
        S = 1 # 신맛
        B = 0 # 쓴맛
        for s, b in subset:
            S = S * s
            B = B + b
    
            result = min(result, abs(S - B))
print(result)