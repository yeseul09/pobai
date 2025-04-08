# 세금징수

test_num = int(input())
money_list = [50000, 10000, 5000, 1000, 500, 100]
for _ in range(test_num):
    money = int(input())
    count = 0
    for m in money_list:
        count += money // m
        money %= m
    print(count)