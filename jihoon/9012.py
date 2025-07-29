N = int(input())

for _ in range(N):
    string = input()
    stack = list()
    answer = "YES"
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                answer = "NO"
            else:
                stack.pop()

    if len(stack) != 0:
        answer = "NO"

    print(answer)