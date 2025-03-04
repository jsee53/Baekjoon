A, B, N = map(int, input().split())

remain = A % B


result = 0
for i in range(N):
    remain = remain * 10
    
    result = int(remain / B)

    remain = remain % B

print(result)