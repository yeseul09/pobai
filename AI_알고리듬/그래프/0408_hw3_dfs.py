# DFS

import sys
sys.setrecursionlimit(1000000)

def find_list(n_node, n_edge):
    adj_list = [[] for _ in range(n_node)]
    for j in range(n_edge):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        adj_list[end].append(start)
        #print(adj_list)
    for j in adj_list:
        j.sort()
        
    return adj_list

def dfs(ad_list, node_name, visited_list):
    if node_name in visited_list:
        return
        
    visited_list.append(node_name)
    for node in ad_list[node_name]:
        dfs(ad_list, node, visited_list)
    return visited_list
        
test_num = int(input())
for i in range(test_num):
    n_node, n_edge = map(int, input().split())
    
    # 인접리스트 구하기
    adj_list = find_list(n_node, n_edge)

    # DFS 탐색
    visited_list = []
    visited_list = dfs(adj_list, 0, visited_list)
    print(*visited_list)

        