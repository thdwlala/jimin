'''n = int(input())  # 정점 수
m = int(input())  # 간선 수

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    #sort(): 오름차순으로 정리하는 함수
for node in graph: #key 추출
    graph[node].sort()'''

graph= {
        1:[2,5],
        2:[1,3,5],
        3:[2],
        4:[7],
        5:[1,2,6],
        6:[5],
        7:[4]
    }

def defs(graph,start_node):
    stack =list()
    #리스트를 함수형태로 써도 빈리스트 생성됨
    visited = list()

    stack.append(start_node)

    while stack: #stack이 비어있지 않다면
        node = stack.pop()
        if node not in visited:
            stack.extend(reversed(graph[node]))
            visited.append(node)

    return len(visited)-1 #시작 노드를 제외하고 숫자세기

print(defs(graph,1))