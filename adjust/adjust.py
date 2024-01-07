from heapq import heappop, heappush

def prim(graph):
    num_vertices = len(graph)
    min_spanning_tree = []
    visited = [False] * num_vertices
    heap = [(0, 0, 0)]  # (distance, start, end)

    while len(min_spanning_tree) < num_vertices - 1:
        dist, start, end = heappop(heap)

        if not visited[end]:
            visited[end] = True
            if start != end:
                min_spanning_tree.append((start, end))

            for i, weight in enumerate(graph[end]):
                if weight != -1 and not visited[i]:
                    heappush(heap, (weight, end, i))

    return min_spanning_tree

# 輸入圖形的相鄰矩陣
n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

# 使用 Prim 演算法找出最小生成樹
min_spanning_tree = prim(adj_matrix)

# 輸出結果
for edge in min_spanning_tree:
    v1, v2 = edge
    print(f"<v{v1 + 1}, v{v2 + 1}>", end=", ")
print("\b\b")  # 移除最後的逗號和空格
