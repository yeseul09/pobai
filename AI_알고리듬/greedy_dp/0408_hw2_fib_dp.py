# 피보나치 수열 (DP)

test_num = int(input())

for _ in range(test_num):
    input_num = int(input())
    fib = [0] * (input_num + 1)
    for i in range(1, input_num+1):
        if i == 1 or i == 2:
            fib[i] = 1
        else:
            fib[i] = fib[i-1] + fib[i-2]
    print(fib[input_num])