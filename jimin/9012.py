
#괄호 짝 검사

def check_brackets(text):
    stack = []

    # 문자열 하나씩 반복
    for char in text:

        # 여는 괄호를 먼저 스택에 추가
        if char == "(":
            stack.append(char)
        # 닫는 괄호가 나왔을 때 pop하기 ->짝 맞춰서 빈스택 만들기

        elif char == ")":
            # 예외1) 스택이 비어있는데 닫는 괄호가 나오면 NO
            if not stack:
                return "NO" 
            
            stack.pop()
    #마지막에 스택이 비어있으면 YES, 스택이 남아있으면 NO
    
    if not stack:
        return "YES"
    else:
        return "NO"

print(check_brackets("(())())"))
print(check_brackets("(((()())()"))
print(check_brackets("(()())((()))"))
print(check_brackets("((()()(()))(((())))()"))
print(check_brackets("()()()()(()()())()"))
print(check_brackets("(()((())()("))