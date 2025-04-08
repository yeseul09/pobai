test_num = int(input())
for i in range(test_num):
    n_list = input().split()
    n_list = [int (i) for i in n_list]
    new_list = []
    for i in n_list:
        if i > 0:
            new_list.append(i)
        elif i == -1:
            print(new_list[-1], end = ' ')
            new_list.pop()     