from collections import deque

result = deque()
for _ in range(int(input())):
    command = input().split()
    eval("result.{}({})".format(*command)) if len(command) > 1 else eval(
        "result.{}()".format(*command))
print(*result)
