# 해커문제

# dfs
import sys
sys.setrecursionlimit(1000000)


# 1. 노드와 간선 수 입력받기
# 2. 인접리스트 생성
# 3. dfs로 노드를 방문하며 방문한 노드 상태 변경
# 4. 상태가 변경되지 않은 노드를 탐색 -> 이때 +1
# 5. 완료되면 출력하기

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

def dfs(adj_list, node_name):
    visited_list[node_name] = True  
    for node in adj_list[node_name]:
        if not visited_list[node]:
            dfs(adj_list, node)

test_num = int(input())
for _ in range(test_num):
    n_node, n_edge = map(int, input().split())
    visited_list = [False] * n_node
    adj_list = find_list(n_node, n_edge)
    count = 0
    
    for n in range(n_node):
        if not visited_list[n]:
            dfs(adj_list, n)
            count += 1
    print(count)