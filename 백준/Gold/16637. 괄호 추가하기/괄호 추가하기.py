# 입력
N = int(input())  # 문자열 길이
ME = input().strip()  # 수식 문자열

# 최대 결과 저장용
result = -2**31

# 계산 함수
def calc(a, op, b):
    a, b = int(a), int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

# DFS 함수 정의
def dfs(index, current_value):
    global result

    # 종료 조건: 수식 끝까지 왔을 때
    if index >= N:
        result = max(result, current_value)
        return

    # 현재 연산자와 피연산자 사용하여 계산
    if index == 0:
        dfs(index + 2, int(ME[0]))  # 첫 숫자부터 시작
    else:
        operator = ME[index - 1]
        next_num = int(ME[index])
        
        # 괄호 없이 계산
        new_val = calc(current_value, operator, next_num)
        dfs(index + 2, new_val)

        # 괄호 사용: 다음 연산이 가능한 경우
        if index + 2 < N:
            next_operator = ME[index + 1]
            next_next_num = int(ME[index + 2])
            # 괄호 내부 먼저 계산
            bracket_val = calc(next_num, next_operator, next_next_num)
            # 현재 값과 괄호 결과를 계산
            new_val_with_bracket = calc(current_value, operator, bracket_val)
            dfs(index + 4, new_val_with_bracket)

# DFS 시작
dfs(0, 0)

# 결과 출력
print(result)
