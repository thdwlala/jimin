from collections import deque

'''row, col = map(int, input().split())
map_data= []

for i in range(row):
    data=list(map(int,input().split()))
    map_data.append(data)'''
row =4
col =6
map_data =[
    [1,0,1,1,1,1],
    [1,0,1,0,1,0],
    [1,0,1,0,1,1],
    [1,1,1,0,1,1]
]

def bfs(map_data):
        #상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    #start_node 설정
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()

        # 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < row and 
                0 <= ny < col and 
                map_data[nx][ny] == 1     #1일때 이동
            ):
                #지나가는 자리마다 1을 더해 칸 수를 저장
                map_data[nx][ny] = map_data[x][y] + 1
                queue.append((nx, ny))  

    #0부터 시작하니까 -1
    return map_data[row-1][col-1]



print(bfs(map_data))