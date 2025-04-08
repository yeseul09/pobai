# 가장 가파른 두 점

def find_s(p, q):
    s = abs((p[1] - q[1])/(p[0] - q[0]))
    return s

test_num = int(input())
for i in range(test_num):
    max_s = 0
    max_point = []
    point_list = []
    point_num = int(input())
    for j in range(point_num):
        p = list(map(int, input().split()))
        point_list.append(p)
    point_list = sorted(point_list, reverse = False)
    for j in range(len(point_list) - 1):
        for k in range(j+1, len(point_list)):
            s = find_s(point_list[j], point_list[k])
            if s > max_s:
                max_point = point_list[j] + point_list[k]
                max_s = s
    print(*max_point)