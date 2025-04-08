import heapq

test_num = int(input())
for i in range(test_num):
    n_num = int(input())
    n_list = list(map(int,input().split()))

    hq = []
    for i in n_list:
        if i > 0:
            heapq.heappush(hq, i)
        elif i == -1:
            print_num = heapq.heappop(hq)
            print(print_num, end = ' ')