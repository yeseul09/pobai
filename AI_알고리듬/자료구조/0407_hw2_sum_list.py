test_num = int(input())
for i in range(test_num):
    n_list = input().split()
    n_list = [int (i) for i in n_list]
    print(sum(n_list))