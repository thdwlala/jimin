'''n = int(input()) #전체 사람의 수(key)
a,b=map(int,input().split()) #구하고자 하는 촌수
m = int(input()) #부모 자식 간의 관계수(노드 수)

family = {i:[] for i in range(1,n+1)}
for _ in range(m):#value
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
for node in family:
    family[node].sort()'''

family ={1: [2, 3],
         2: [1, 7, 8, 9],
         3: [1],
         4: [5, 6],
         5: [4],
         6: [4],
         7: [2],
         8: [2],
         9: [2]
                }
a,b = 7,3
if a>b:
    a,b = b,a #무조건 a가 작은 수가 나옴

def defs(family,a,b):
    sum =0
    stack =list()
    #리스트를 함수형태로 써도 빈리스트 생성됨
    visited = list()
    stack.append(a)

    while True: #stack이 비어있지 않다면
        node = stack.pop()
        if node == b:
            break
        if node not in visited:
            stack.extend(reversed(family[node]))
            visited.append(node)
            sum+=1
    return sum #시작 노드를 제외하고 숫자세기

print(defs(family,a,b))








