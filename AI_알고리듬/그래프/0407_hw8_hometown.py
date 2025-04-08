# 마을회관 건설
test_num = int(input())
for _ in range(test_num):
    n_list = list(map(int, input().split()))
    n = len(n_list)
    median = n_list[n//2]
    sum_dist = sum(abs(dist - median) for dist in n_list)
    print(sum_dist)