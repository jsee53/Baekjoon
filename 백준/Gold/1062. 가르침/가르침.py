import sys
from itertools import combinations

result = 0
N, K = map(int, input().split())

essential_chars = {'a','n','t','i','c'}
essential_mask = 0

# 필수 알파벳 비트마스킹 변환
for char in essential_chars:
    essential_mask |= 1 << ord(char) - ord('a')

word_masks = []

# 입력 및 비트마스킹 변환
for i in range(N):
    word = input()[4:-4]
    word_mask = 0
    for char in word:
        word_mask |= (1 << (ord(char) - ord('a')))
    word_masks.append(word_mask)

if(K < 5):
    print(0)
    sys.exit()
if(K >= 26):
    print(N)
    sys.exit()

# 암기할 수 있는 알파벳 수
learnable_num = K - 5

# 필수 알파벳을 제외한 알파벳 비트마스킹 변환
remaining_chars = [chr(i + ord('a')) for i in range(26) if chr(i + ord('a')) not in essential_chars]

for chosen_chars in combinations(remaining_chars, learnable_num):
    current_mask = essential_mask

    for chosen_char in chosen_chars:
        current_mask |= (1 << (ord(chosen_char) - ord('a')))

    # 학습할 수 있는 단어는 모두 카운트
    count = sum(1 for word_mask in word_masks if (word_mask & current_mask) == word_mask)
    
    result = max(count, result)
print(result)