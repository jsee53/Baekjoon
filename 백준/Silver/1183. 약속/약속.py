import sys, math

N = int(input())

M = []
for _ in range(N):
    a, b = map(int, input().split())
    M.append(a-b)

# 홀수의 경우 최소값 1개
if(N % 2 == 1):
    print(1)
    sys.exit()
    
# 짝수의 경우 중앙에 존재하는 범위만큼 최소값 존재
M.sort()
print(M[math.floor(N/2)] - M[math.floor(N/2) - 1] + 1) # N = 1인 경우는 홀수이므로 위에서 처리(에외처리 필요 x)