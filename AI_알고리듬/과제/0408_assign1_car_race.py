# 두 바퀴 레이스
test_num = int(input())
for _ in range(test_num):
    car_list = list(map(int, input().split()))
    check_set = set()
    first_list = []
    second_list = []
    
    print_char = "NO"
    for i in car_list:
        if i in check_set:
            second_list.append(i)
        else:
            first_list.append(i)
            check_set.add(i)
    if list(first_list) != second_list:
        print_char = "YES"
    print(print_char)   