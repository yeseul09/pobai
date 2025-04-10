# 숫자 주고 이진탐색

# min, max 비교후 min보다 작거나 max보다 높으면 각 값 반환
# 만약 같은 숫자가 나오면(차이가 0인 값이 있으면) 반환
# 이진탐색중 값이 2개만 남아있을때 위아래값의 차를 구한 후 차가 작은쪽 반환

def binary_search(n_list, key, start, end):
    mid = (start + end) // 2

    if n_list[mid] == key:
        return n_list[mid]
    elif n_list[mid] < key:
        start = mid
    else:
        end = mid

    # 마지막 두 개만 남았을 때
    if end - start == 1:
        prev_diff = abs(key - n_list[start])
        next_diff = abs(key - n_list[end])
        if prev_diff == 0:
            return n_list[start]
        if next_diff == 0:
            return n_list[end]
        if prev_diff <= next_diff:
            return n_list[start]
        else:
            return n_list[end]

    return binary_search(n_list, key, start, end)


test_num = int(input())
for _ in range(test_num):
    compare_list = list(map(int, input().split()))
    target_list = list(map(int, input().split()))
    
    for target in target_list:
        if target <= compare_list[0] : # min값보다 작을 경우
            print(compare_list[0], end=' ')
            continue
        if target >= compare_list[-1]: # max값보다 클 경우
            print(compare_list[-1], end=' ')
            continue
        print(binary_search(compare_list, target, 0, len(compare_list) - 1), end = ' ')