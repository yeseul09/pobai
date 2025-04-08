# 세계 암기대회

test_num = int(input())
for _ in range(test_num):
    n, m = map(int, input().split())
    opm = [[] for _ in range(n)]
    for i in range(n):
        opm[i] = list(map(int, input().split()))
    mpm = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                mpm[i][j] = opm[i][j]
            elif i == 0 and j > 0:
                mpm[i][j] = opm[i][j] + mpm[i][j-1]
            elif i> 0 and j == 0:
                mpm[i][j] = opm[i][j] + mpm[i-1][j]
            elif i > 0 and j > 0:
                mpm[i][j] = opm[i][j] + min(mpm[i-1][j], mpm[i][j-1], mpm[i-1][j-1])
    print(mpm[n-1][m-1])