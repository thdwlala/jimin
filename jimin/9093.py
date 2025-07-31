from collections import deque

def reverse_words(text): #문장을 단어로 나누기
    words = text.split(" ")
    result = []
    
    for word in words: #각 단어의 알파벳 넣기 
        my_deque = deque()
        for char in word:
            my_deque.append(char)
        print(my_deque)

        #역순으로 저장
        reverse = []
        while my_deque:
            # popleft()로 첫 번째 요소를 꺼내 리스트의 앞에 추가하면 역순이 됨
            reverse.insert(0, my_deque.popleft())
            print(reverse) #->리스트 안에 각각의 요소들고 저장되어 있음
            
        # 뒤집힌 문자들 하나의 단어로 만들기
        reversed_word = "".join(reverse)
        
        # 결과 리스트에 뒤집힌 단어 추가하기
        result.append(reversed_word)
    
    # 공백 포함해서 문장 만들기
    return " ".join(result)

text = "I am happy today We want to win the first prize"
result = reverse_words(text)
print(result) 