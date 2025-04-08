# 하노이탑
def hanoi(n, start, end, mid):
    #print(n, start, end, mid)
    # 원판이 하나일때
    if n <= 1:
        print(start , " -> " , end)
        return
    # 원판이 여러개일때 - n-1개의 원판을 두번째 기둥으로 이동)
    
    hanoi(n-1, start, mid, end) # n-1개의 원판을 첫번째에서 두번째 기둥으로 이동
    print(start , " -> " , end)
    hanoi(n-1, mid, end, start) # n-1개의 원판을 두번째에서 세번째로 이동

test_num = int(input())
for i in range(test_num):
    n_hanoi = int(input())
    hanoi(n_hanoi, 'A', 'C', 'B')

