# 이진탐색
def binary_search(n_list, key, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if n_list[mid] == key:
        return mid
    elif n_list[mid] < key:
        start = mid + 1
    else:
        end = mid - 1

    return binary_search(n_list, key, start, end)
        
test_num = int(input())
for i in range(test_num):
    n_list = list(map(int, input().split()))
    key_list = list(map(int, input().split()))
    answer = []

    for i in key_list:
        answer.append(binary_search(n_list, i, 0, len(n_list) -1))
    print(*answer)