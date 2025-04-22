T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num = input().strip()
    num_list = []

    rotation = N // 4  # 한 변의 길이

    for k in range(rotation):  # 총 회전은 N/4 번
        for i in range(4):
            part = num[i * rotation : (i + 1) * rotation]
            if part not in num_list:
                num_list.append(part)
        num = num[-1] + num[:-1]  # 시계 방향 회전

    # 정렬 시 정수로 변환하여 비교
    num_list.sort(key=lambda x: int(x, 16), reverse=True)
    print(f"#{test_case} {int(num_list[K - 1], 16)}")
