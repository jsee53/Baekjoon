N, B = map(int,input().split())

def format(num):
    if num < 10: return str(num)
    else: return chr(num + 55)


result = ""
while N >= B:
    result = format(int(N % B)) + result
    N = (N - N % B) / B

if(not N == 0):
    result = format(int(N % B)) + result
    N = (N - N % B) / B

print(result)