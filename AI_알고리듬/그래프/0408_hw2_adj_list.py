# 인접리스트 구하기

test_num = int(input())
for i in range(test_num):
    n_node, n_edge = map(int, input().split())
    adj_list = [[] for _ in range(n_node)]
    for j in range(n_edge):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        adj_list[end].append(start)
        #print(adj_list)
    for j in adj_list:
        j.sort()
        print(*j)
        