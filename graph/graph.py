def floyd_warshall(graph):
    n = len(graph)
    INF = float('inf')

    # 初始化最短距離矩陣，初始時與相鄰矩陣相同
    dist = [row[:] for row in graph]

    # 將 -1 轉換為無限大
    for i in range(n):
        for j in range(n):
            if dist[i][j] == -1:
                dist[i][j] = INF

    # 以每個節點為中間點，更新所有節點之間的最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# 讀取輸入
# 輸入矩陣的行數和列數
rows = int(input("請輸入矩陣的行數："))
#cols = int(input("請輸入矩陣的列數："))

# 創建一個空的矩陣
matrix = []

# 根據輸入的行數和列數動態輸入矩陣元素
for i in range(rows):
    row = list(map(int, input(f"請輸入第 {i+1} 行的元素，用空格分隔：").split()))
    matrix.append(row)

"""
# 印出輸入的矩陣
for row in matrix:
    print(' '.join(map(str, row)))
"""
# 呼叫佛洛伊德最短路徑演算法
result = floyd_warshall(matrix)

# 輸出最短距離矩陣
for row in result:
    # 將無限大轉換為 -1
    formatted_row = ['-' if val == float('inf') else str(val) for val in row]
    print(' '.join(formatted_row))
