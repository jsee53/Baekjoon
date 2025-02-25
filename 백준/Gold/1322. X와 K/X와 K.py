# n의 i번째 비트 반환 함수
def get_bit(n, i):
    return (n >> i) & 1

# n의 i번째 비트를 1로 변환 함수
def add_bit(n, i):
    return (1 << i) | n

# n의 i번째 비트를 0으로 변환 함수
def del_bit(n, i):
    return ~(1 << i) & n

X, K = map(int, input().split())

result = 0
digit = 0
digit_K = 0 # K의 확인 비트 자리
digit_Result = 0

while K > 0:
    if(get_bit(X, digit) == 0):
        if(get_bit(K, 0) == 1): # K의 확인할 비트가 1인 경우만 result에 1 추가
            result |= (1 << digit)
        K >>= 1 # 확인한 비트는 제거(오른쪽 시프트)
    
    digit = digit + 1

print(result)