from decimal import Decimal

X, Y = map(int, input().split()) # 게임 횟수, 이긴 게임

Z = int(Decimal(Y) / Decimal(X) * 100) # 현재 승률

max = 1000000001
min = 0

isChanged = False # 승률 바뀐 여부

result = 0
while min < max:
    win_num = int((max + min) / 2)
    new_Z = int(Decimal(Y + win_num) / Decimal(X + win_num) * 100) # 새로운 승률

    # 승률이 변한 경우 더 낮은 값으로 승률이 변할 수 있는지 확인(이진 탐색)
    if(Z != new_Z):
        max = win_num
        result = win_num
        isChanged = True
    # 승률이 변하지 않은 경우 더 높은 갚으로 승률이 변할 수 있는지 확인
    else:
        min = win_num + 1

if(isChanged): print(result)
else : print(-1)
