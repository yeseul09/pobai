# BFS
from collections import deque

def find_list(n_node, n_edge):
    adj_list = [[] for _ in range(n_node)]
    for j in range(n_edge):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        #adj_list[end].append(start)
        #print(adj_list)
    for j in adj_list:
        j.sort()
        
    return adj_list

def bfs(ad_list, node_name, visited_list):
    queue = deque([node_name])
    visited_list.append(node_name)
    while queue:
        v = queue.popleft()
        for i in ad_list[v]:
            if i not in visited_list:
                queue.append(i)
                visited_list.append(i)
    return visited_list
        
test_num = int(input())
for i in range(test_num):
    n_node, n_edge = map(int, input().split())
    
    # 인접리스트 구하기
    adj_list = find_list(n_node, n_edge)

    # DFS 탐색
    visited_list = []
    visited_list = bfs(adj_list, 0, visited_list)
    print(*visited_list)

        