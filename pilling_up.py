from collections import deque

for _ in range(int(input())):
    cubes = int(input())
    row = deque(input().split())
    for _ in range(cubes):
        if (int(row[0]) == int(max(row)) or int(row[-1]) == int(max(row))):
            row.popleft() if row[0] >= row[-1] else row.pop()
        else:
            break
    if len(row) != 0:
        print("No")
    else:
        print("Yes")
#todo