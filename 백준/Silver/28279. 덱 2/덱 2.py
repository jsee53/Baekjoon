import sys
from collections import deque

N = int(input())

store = deque()
result = []

for _ in range(N):
    command = sys.stdin.readline().split()

    command[0] = int(command[0])
    
    if command[0] == 1:
        store.appendleft(command[1])
    elif command[0] == 2:
        store.append(command[1])
    elif command[0] == 3:
        if store:
            result.append(store.popleft())
        else:
            result.append(-1)
    elif command[0] == 4:
        if store:
            result.append(store.pop())
        else:
            result.append(-1)
    elif command[0] == 5:
        result.append(len(store))
    elif command[0] == 6:
        if store:
            result.append(0)
        else:
            result.append(1)
    elif command[0] == 7:
        if store:
            result.append(store[0])
        else:
            result.append(-1)
    elif command[0] == 8:
        if store:
            result.append(store[-1])
        else:
            result.append(-1)

for i in result:
    print(i)
