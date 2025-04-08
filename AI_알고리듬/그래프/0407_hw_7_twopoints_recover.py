# 가장 가파른 두 점

def find_s(p, q):
    s = abs((p[1] - q[1])/(p[0] - q[0]))
    return s

test_num = int(input())
for i in range(test_num):
    max_s = -1
    max_point = []
    point_list = []
    point_num = int(input())
    for j in range(point_num):
        p = list(map(int, input().split()))
        point_list.append(p)
    point_list.sort()
    
    for j in range(1, point_num):
        s = find_s(point_list[j - 1], point_list[j])
        if s > max_s:
            max_s = s
            max_point = point_list[j - 1] + point_list[j]
    print(*max_point)