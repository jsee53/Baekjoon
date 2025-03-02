import math

N = input()

need_set = []
for i in N:
    need_set.append(i)
    
num_6 = need_set.count('6')
num_9 = need_set.count('9')

num_max = 0 # 6, 9를 제외하고 가장 많이 나온 수의 개수
for i in map(str, range(10)):
    if(i != '6' and i!= '9'):
        num_max = max(num_max, need_set.count(i))
        
num_6and9 = math.ceil((num_6 + num_9) / 2)

print(max(num_max, num_6and9))