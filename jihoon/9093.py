N = int(input())

for _ in range(N):
    string = input()
    answer = ""

    words = string.split()

    for word in words:
        stack = list()
        for char in word:
            stack.append(char)
        
        while stack:
            answer += stack.pop()
        
        answer += " "

    print(answer)