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

def dfs(family, a, b):
    stack = []
    visited = []
    stack.append((a, 0))  

    while stack:
        node, sum = stack.pop() #(현재 노드, 누적 촌수)
        if node == b:
            return sum
        if node not in visited:
            visited.append(node)
            for neighbor in reversed(family[node]):
                 stack.append((neighbor, sum + 1))
                 print(stack)
               
    return -1  # 연결이 없을 경우 -1 반환

print(dfs(family,a,b))








