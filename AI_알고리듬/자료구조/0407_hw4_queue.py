import collections

test_num = int(input())
for i in range(test_num):
    n_list = input().split()
    n_list = [int (i) for i in n_list]
    queue = collections.deque([])
    for i in n_list:
        if i > 0:
            queue.append(i)
        elif i == -1:
            print_num = queue.popleft()
            print(print_num, end = ' ')