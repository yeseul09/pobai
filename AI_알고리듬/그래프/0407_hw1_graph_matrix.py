test_num = int(input())
for i in range(test_num):
    n_node, n_edge = map(int, input().split())
    adj_list = [[0] * n_node for _ in range(n_node)] 
    for j in range(n_edge):
        start, end, weight = map(int, input().split())
        #print(start, end, weight)
        adj_list[start][end] = weight
        #print(adj_list)
    for j in adj_list:
        print(*j)